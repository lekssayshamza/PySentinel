from pysentinel.scanner import scan_target
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m pysentinel <URL>")
        sys.exit(1)

    scan_target(sys.argv[1])


if __name__ == "__main__":
    main()
