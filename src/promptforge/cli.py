import argparse

from . import __version__
from .generators.skill import create_skill


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

    try:
        if args.command == "new":
            if args.resource == "skill":
                create_skill(args.name)
        else:
            parser.print_help()

    except FileExistsError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()