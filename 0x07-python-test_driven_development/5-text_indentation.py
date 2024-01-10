#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    f = 0
    while f < len(text) and text[f] == ' ':
        f += 1

    while f < len(text):
        print(text[f], end="")
        if text[f] == "\n" or text[f] in ".?:":
            if text[f] in ".?:":
                print("\n")
            f += 1
            while f < len(text) and text[f] == ' ':
                f += 1
            continue
        f += 1
