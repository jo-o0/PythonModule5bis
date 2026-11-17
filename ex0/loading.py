import sys
import importlib.metadata


def show_instructions() -> None:
    print("\nPip vs Poetry")
    print("requirements.txt declares what to install;"
          " pip resolves it at install time.")
    print("pyproject.toml declares the same constraints, "
          "and Poetry pins the resolve")
    print("versions in poetry.lock so every install is identical.")
    print("\nUse one of the options below:")
    print("* 'pip install -r requirements.txt' and run again")
    print("* 'poetry install' and 'poetry run python loading.py'")
    sys.exit(1)


def check_pandas() -> None:
    try:
        version = importlib.metadata.version("pandas")
        if version == "2.1.0":
            print("[OK] pandas (2.1.0) - Data manipulation ready")
        else:
            print(f"[KO] pandas version: {version}."
                  "Version '2.1.0' needed")
    except importlib.metadata.PackageNotFoundError:
        print("[KO] pandas package not found")


def check_numpy() -> None:
    try:
        version = importlib.metadata.version("numpy")
        if version == "1.25.0":
            print("[OK] numpy (1.25.0) - Numerical Computation ready")
        else:
            print(f"[KO] numpy version: {version}."
                  "Version '1.25.0' needed")
    except importlib.metadata.PackageNotFoundError:
        print("[KO] numpy package not found")
        show_instructions()


def check_dependencies() -> None:
    check_pandas()
    check_numpy()


def main() -> None:
    print("\n* LOADING STATUS...LOADING PROGRAMS...\n")
    try:
        check_dependencies()
    except Exception:
        sys.exit(1)
    print("\nAll dependencies installed correctly")
    print("\nPip vs Poetry")
    print("requirements.txt declares what to install;"
          " pip resolves it at install time.")
    print("pyproject.toml declares the same constraints, "
          "and Poetry pins the resolve")
    print("versions in poetry.lock so every install is identical.")
    print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
