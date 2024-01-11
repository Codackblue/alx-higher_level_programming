#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Script is about to be executed.")
    read_file("my_file_0.txt")
    print("Script execution completed.")
