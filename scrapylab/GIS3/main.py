import requests
import os
import multiprocessing
from tqdm import tqdm

# --- Step 1: Configuration ---
# Replace with your own API Key and CSE ID
API_KEY = "AIzaSyC6gjuxkdjaUikBQvQmmw0znnH2cqtsko0"
CSE_ID = "d1708bc81dc91464b"

# The search term you want to find images for
SEARCH_QUERY = "ripe whole avocado -site:cartoonstock.com"
# -----------------------------

def fetch_image_urls(api_key, cse_id, query, num_images=100):
    """
    Fetches a list of image URLs from the Google CSE API.
    This part is done sequentially as it's fast.
    """
    print(f"Searching for images of: '{query}'")
    urls = []
    pages = num_images // 10

    for i in range(pages):
        start_index = i * 10 + 1
        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                'key': api_key,
                'cx': cse_id,
                'q': query,
                'searchType': 'image',
                'num': 10,
                'start': start_index,
                'imgSize': 'large'
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            search_results = response.json()

            items = search_results.get("items", [])
            for item in items:
                urls.append(item['link'])

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {i + 1}: {e}")
            continue
        except KeyError:
            print(f"Could not find 'items' on page {i + 1}. The query may have less than {num_images} results.")
            break

    print(f"Found {len(urls)} image URLs.")
    return urls

# --- THIS IS THE CORRECTED FUNCTION ---
def download_single_image(image_url, index, download_dir, query):
    """
    Worker function to download a single image.
    Now accepts four separate arguments.
    """
    try:
        image_response = requests.get(image_url, timeout=15)
        image_response.raise_for_status()

        # Determine file extension
        file_extension = os.path.splitext(image_url)[1].lower()
        if file_extension not in ['.jpg', '.jpeg', '.png', '.gif']:
            file_extension = '.jpg'

        file_name = f"{query.replace(' ', '_')}_{index}{file_extension}"
        file_path = os.path.join(download_dir, file_name)

        with open(file_path, 'wb') as f:
            f.write(image_response.content)
        return f"Successfully downloaded {file_name}"
    except requests.exceptions.RequestException as e:
        return f"Failed to download {image_url}: {e}"
    except Exception as e:
        return f"An unexpected error occurred for {image_url}: {e}"

def main():
    """
    Main function to orchestrate fetching and parallel downloading.
    """
    if API_KEY == "YOUR_API_KEY" or CSE_ID == "YOUR_CSE_ID":
        print("Please replace 'YOUR_API_KEY' and 'YOUR_CSE_ID' with your actual credentials.")
        return

    # 1. Fetch all URLs first
    image_urls = fetch_image_urls(API_KEY, CSE_ID, SEARCH_QUERY)

    if not image_urls:
        print("No images to download. Exiting.")
        return

    # 2. Prepare for download
    download_dir = SEARCH_QUERY.replace(" ", "_")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print(f"Created directory: {download_dir}")

    # 3. Create a list of tasks for the process pool
    tasks = [(url, i + 1, download_dir, SEARCH_QUERY) for i, url in enumerate(image_urls)]

    # 4. Use a multiprocessing Pool to download images in parallel
    num_processes = min(multiprocessing.cpu_count(), len(tasks))
    print(f"\nStarting download of {len(tasks)} images using {num_processes} processes...")

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = list(tqdm(pool.starmap(download_single_image, tasks), total=len(tasks)))

    success_count = sum(1 for r in results if r.startswith("Success"))
    print(f"\nDownload complete. {success_count} out of {len(image_urls)} images were saved to the '{download_dir}' folder.")

if __name__ == '__main__':
    main()
