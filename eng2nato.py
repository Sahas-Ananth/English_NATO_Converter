#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from io import StringIO

from typing_extensions import TextIO

__version__ = "0.1"


def transform(text: str | list[str], mapping: dict[str, str], sep: str = " "):
    """Transforms each character in the input text based on the provided mapping.

    Args:
        text: Input string or list of strings to be transformed.
        mapping: Dictionary used for character transformation.
        sep: Separator for joining transformed characters.

    Returns:
        Transformed string.
    """
    return sep.join(mapping.get(char, char) for char in text)


def input_handler() -> tuple[TextIO, bool]:
    """Handles input from both Stdin, FileIO, and CLI arguments.

    Returns:
        Tuple containing Input Stream and decode flag.
    """
    parser = argparse.ArgumentParser(
        description="""Convert normal English to NATO phonetic alphabet or decode
                       from NATO back to English. Useful for clear communication.""",
    )
    _ = parser.add_argument(
        "string", type=str, nargs="*", help="The string to convert.", default=[]
    )
    _ = parser.add_argument(
        "-d",
        "--decode",
        action="store_true",
        help="Decode Flag to convert from NATO back to English.",
    )
    _ = parser.add_argument(
        "-i",
        "--input",
        nargs="?",
        default=None,
        type=str,
        help="Path to input file. If empty, Defaults to stdin.",
    )
    args = parser.parse_args()
    if args.string:  # pyright: ignore[reportAny]
        return (
            StringIO(" ".join(args.string)),  # pyright: ignore[reportAny]
            args.decode,  # pyright: ignore[reportAny]
        )

    # Colors for Error printing.
    CRED2 = "\33[91m"
    CEND = "\33[0m"
    if args.input:  # pyright: ignore[reportAny]
        try:
            return open(args.input, "r"), args.decode  # pyright: ignore[reportAny]
        except FileNotFoundError:
            sys.exit(
                f"{CRED2}Error: File '{args.input}' not found!{CEND}"  # pyright: ignore[reportAny]
            )
        except IOError as e:
            sys.exit(
                f"{CRED2}Error reading file '{args.input}': {e}{CEND}"  # pyright: ignore[reportAny]
            )

    return sys.stdin, args.decode  # pyright: ignore[reportAny]


def main():
    ENG_TO_NATO_MAP: dict[str, str] = {
        "a": "Alfa",
        "b": "Bravo",
        "c": "Charlie",
        "d": "Delta",
        "e": "Echo",
        "f": "Foxtrot",
        "g": "Golf",
        "h": "Hotel",
        "i": "India",
        "j": "Juliett",
        "k": "Kilo",
        "l": "Lima",
        "m": "Mike",
        "n": "November",
        "o": "Oscar",
        "p": "Papa",
        "q": "Quebec",
        "r": "Romeo",
        "s": "Sierra",
        "t": "Tango",
        "u": "Uniform",
        "v": "Victor",
        "w": "Whiskey",
        "x": "Xray",
        "y": "Yankee",
        "z": "Zulu",
        " ": "(space)",
    }
    stream, decode = input_handler()
    mapping = (
        {v.lower(): k for k, v in ENG_TO_NATO_MAP.items()}
        if decode
        else ENG_TO_NATO_MAP
    )
    sep = "" if decode else " "

    with stream:
        for line in stream:
            line_content = line.strip().lower()
            input_text = line_content.split() if decode else line_content
            print(transform(input_text, mapping, sep))


if __name__ == "__main__":
    main()
