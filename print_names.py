import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python names_cli.py name1 name2 ...")
        return

    names = sys.argv[1:]  # Get all command-line arguments except the script name
    print("Names entered:", ", ".join(names))

if __name__ == "__main__":
    main()
