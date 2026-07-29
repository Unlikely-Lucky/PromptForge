import argparse
from . import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="promptforge",
        description="PromptForge CLI",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"PromptForge {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    new_parser = subparsers.add_parser(
        "new",
        help="Create resources",
    )

    new_parser.add_argument(
        "resource",
        choices=["skill"],
        help="Resource type",
    )

    new_parser.add_argument(
        "name",
        help="Name of the resource",
    )

    args = parser.parse_args()

    if args.command == "new":
        print(f"Creating {args.resource}: {args.name}")
    else:
        parser.print_help()