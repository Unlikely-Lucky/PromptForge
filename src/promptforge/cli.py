import argparse

from . import __version__

from .commands.new import run as new_command
from .commands.validate import run as validate_command
from .commands.list import run as list_command
from .commands.info import run as info_command


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

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="{new,validate,list,info}",
    )

    # ======================================================
    # NEW
    # ======================================================
    new_parser = subparsers.add_parser(
        "new",
        help="Create new PromptForge resources",
    )

    new_parser.add_argument(
        "resource",
        choices=["skill"],
        help="Resource type",
    )

    new_parser.add_argument(
        "name",
        nargs="?",
        help="Name of the skill",
    )

    new_parser.set_defaults(func=new_command)

    # ======================================================
    # VALIDATE
    # ======================================================
    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate all skills",
    )

    validate_parser.set_defaults(func=validate_command)

    # ======================================================
    # LIST
    # ======================================================
    list_parser = subparsers.add_parser(
        "list",
        help="List all available skills",
    )

    list_parser.set_defaults(func=list_command)

    # ======================================================
    # INFO
    # ======================================================
    info_parser = subparsers.add_parser(
        "info",
        help="Show information about a skill",
    )

    info_parser.add_argument(
        "name",
        help="Skill name",
    )

    info_parser.set_defaults(func=info_command)

    # ======================================================
    # RUN
    # ======================================================
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()