import sys


def run(message: str) -> int:
    print(message)
    return 0


def main():
    message = "Hello Henrique"
    sys.exit(run(message))


if __name__ == "__main__":
    main()
