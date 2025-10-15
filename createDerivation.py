import hashlib
import os
#make a function that is able to create variations of the dataset, so the function will accept the dataset, then a filtering function, then a map function, the filtering function will filter the dataset based on a condition, the parameter that it accepts is the file_path column, and returns a boolean. The map function will accept the file_path column and return a byte array representing the file. Now this function itself should return a path to a csv that can be read. The function will store variations of the csv file and images by hashing them. The columns of the csv files should be the same, but the rows may be different to the original dataset
def create_dataset_variation(
    df,
    filter_fn,
    map_fn,
    base_dir=None,
    variation_tag=None,
    num_workers=None,
):
    """
    Create a dataset variation by filtering rows based on file_path and mapping files to new byte content.
    - df: pandas DataFrame with at least a 'file_path' column. Other columns are preserved.
    - filter_fn(path: str) -> bool
    - map_fn(path: str) -> bytes  (returns the file content to save)
    Returns: absolute path to the generated CSV file.
    """
    assert "file_path" in df.columns, "Input DataFrame must contain 'file_path' column."

    # Use existing STEPS dir if available
    base_dir = base_dir or os.path.join(STEPS if "STEPS" in globals() else "./steps", "variations")
    os.makedirs(base_dir, exist_ok=True)

    def _func_hash(fn):
        try:
            code = getattr(fn, "__code__", None)
            if code:
                payload = code.co_code + bytes(str(code.co_consts), "utf-8")
            else:
                payload = bytes(repr(fn), "utf-8")
        except Exception:
            payload = bytes(repr(fn), "utf-8")
        return hashlib.sha256(payload).hexdigest()

    # Build a signature for this variation
    dataset_fp_hash = hashlib.sha256(
        "\n".join(sorted(df["file_path"].astype(str).tolist())).encode("utf-8")
    ).hexdigest()
    cols_sig = "|".join([str(c) for c in df.columns])
    filter_hash = _func_hash(filter_fn)
    map_hash = _func_hash(map_fn)
    tag = variation_tag or ""
    signature = f"v1|{cols_sig}|{dataset_fp_hash}|{filter_hash}|{map_hash}|{tag}"
    var_hash = hashlib.sha256(signature.encode("utf-8")).hexdigest()[:16]

    # Prepare directories
    var_dir = os.path.join(base_dir, f"var_{var_hash}")
    images_dir = os.path.join(var_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    # Filter rows
    mask = df["file_path"].map(lambda p: bool(filter_fn(p)))
    out_df = df[mask].copy()

    # If nothing to process, still produce an empty CSV with same columns
    csv_path = os.path.abspath(os.path.join(var_dir, f"{var_hash}.csv"))
    if out_df.empty:
        out_df.to_csv(csv_path, index=False)
        print(f"No rows passed filter. Wrote empty CSV to {csv_path}")
        return csv_path

    # Worker to transform and save files deterministically by content hash
    def _worker(item):
        idx, row = item
        src = row["file_path"]
        try:
            data = map_fn(src)
            if not isinstance(data, (bytes, bytearray)):
                # Fallbacks if a path/string/None is returned by mistake
                if isinstance(data, str) and os.path.isfile(data):
                    print(f"Warning: map_fn returned a string path instead of bytes for {src}. Reading file content from {data}.")
                    with open(data, "rb") as f:
                        data = f.read()
                else:
                    print(f"Warning: map_fn returned a string path instead of bytes for {src}. Reading file content from {data}.")
                    with open(src, "rb") as f:
                        data = f.read()
            data = bytes(data)
            content_hash = hashlib.sha256(data).hexdigest()[:32]
            ext = os.path.splitext(src)[1] or ".bin"
            out_name = f"{content_hash}{ext}"
            out_path = os.path.join(images_dir, out_name)
            if not os.path.exists(out_path):
                with open(out_path, "wb") as f:
                    f.write(data)
            return idx, os.path.abspath(out_path)
        except Exception:
            return idx, None

    # Parallel map
    from concurrent.futures import ThreadPoolExecutor  # already imported earlier; safe local import if not
    max_workers = num_workers or min(32, (os.cpu_count() or 4))
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        for r in ex.map(_worker, out_df.iterrows()):
            results.append(r)

    # Update file paths, drop failures
    failed = [i for i, p in results if p is None]
    if failed:
        out_df = out_df.drop(index=failed)
    for i, p in results:
        if p is not None:
            out_df.at[i, "file_path"] = p

    # Save CSV
    os.makedirs(var_dir, exist_ok=True)
    out_df.to_csv(csv_path, index=False)
    print(f"Wrote {len(out_df)} rows to {csv_path} (variation {var_hash})")
    return csv_path
