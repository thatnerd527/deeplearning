{
  description = "A development environment with Python";

  inputs = {
    # Pin a specific version of Nixpkgs if desired, or use 'nixos-unstable'
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      # Systems to support
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      # Helper function to generate a set for each system
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;

      # Helper to instantiate nixpkgs for a specific system
      nixpkgsFor = system: import nixpkgs { inherit system; };
    in
    {

      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgsFor system;
        in
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              python313
              python313Packages.pip
              python313Packages.virtualenv
              gnumake
              gcc # or pkgs.clang
              pkg-config # helps find system libraries
              nodejs_24
              yarn-berry_3
            ];

            # Optional: Shell hook to print a welcome message or run setup commands
            shellHook = ''
              export PATH="$PWD/node_modules/.bin:$PATH"
              # Create venv if it doesn't exist
              if [ ! -d ".venv" ]; then
                echo "Creating new virtual environment..."
                python -m venv .venv
              fi

              # Activate the virtual environment
              source .venv/bin/activate

              # Optional: Set a local pip cache to avoid cluttering your real home dir
              export PIP_CACHE_DIR=$(pwd)/.pip_cache
            '';
          };
        }
      );
    };
}
