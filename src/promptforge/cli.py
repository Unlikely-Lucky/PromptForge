import argparse

from . import __version__
from .generators.skill import create_skill
from .validators.skill import validate_all


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

    # -------------------------
    # new command
    # -------------------------
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

    # -------------------------
    # validate command
    # -------------------------
    subparsers.add_parser(
        "validate",
        help="Validate all skills",
    )

    args = parser.parse_args()

    try:
        if args.command == "new":
            if args.resource == "skill":
                create_skill(args.name)

        elif args.command == "validate":
            validate_all()

        else:
            parser.print_help()

    except FileExistsError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()