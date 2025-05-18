# main.py
import sys

try:
    import numpy as np
except ModuleNotFoundError:
    np = None
    print("Numpy is not installed. Continuing without it.")


def main():
    """Entry point for the MatchaMe demo script."""
    print("Conda environment is working!")
    print(f"Python executable: {sys.executable}")
    if np is not None:
        print(f"Numpy version: {np.__version__}")
    else:
        print("Numpy not available")


if __name__ == "__main__":
    main()
