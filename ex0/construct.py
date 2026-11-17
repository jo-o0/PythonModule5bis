import sys
import os
import site


def is_virtual() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_virtual():
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print("Current Python", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("\nSUCCESS: You are in an isolated environment!\n")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:", site.getsitepackages()[0])
    else:
        print("\nMATRIX STATUS: You are plugged in\n")
        print("Current Python", sys.executable)
        print("Virtual Environment: None detected")
        print("WARNING: You are in the global environment\n"
              "The machines can see everything you install!!\n")
        print("To enter the construct run: "
              "python3 -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              r"matrix_env\Scripts\activate # On Windows"
              "\n\nThen run this program again.")


if __name__ == "__main__":
    main()
