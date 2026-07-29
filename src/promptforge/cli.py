import argparse

from . import __version__

from .commands.new import run as new_command
from .commands.validate import run as validate_command
from .commands.list import run as list_command
from .commands.info import run as info_command
from .commands.build import run as build_command
from .commands.install import run as install_command


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
        metavar="{new,validate,list,info,build,install}",
    )

    # ---------------- NEW ----------------

    new_parser = subparsers.add_parser(
        "new",
        help="Create a new resource",
    )

    new_parser.add_argument(
        "resource",
        choices=["skill"],
    )

    new_parser.add_argument(
        "name",
        nargs="?",
    )

    new_parser.set_defaults(func=new_command)

    # ---------------- VALIDATE ----------------

    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate skills",
    )

    validate_parser.set_defaults(func=validate_command)

    # ---------------- LIST ----------------

    list_parser = subparsers.add_parser(
        "list",
        help="List installed skills",
    )

    list_parser.set_defaults(func=list_command)

    # ---------------- INFO ----------------

    info_parser = subparsers.add_parser(
        "info",
        help="Show skill information",
    )

    info_parser.add_argument(
        "name",
    )

    info_parser.set_defaults(func=info_command)

    # ---------------- BUILD ----------------

    build_parser = subparsers.add_parser(
        "build",
        help="Build a PromptForge package",
    )

    build_parser.add_argument(
        "name",
    )

    build_parser.set_defaults(func=build_command)

    # ---------------- INSTALL ----------------

    install_parser = subparsers.add_parser(
        "install",
        help="Install a PromptForge package",
    )

    install_parser.add_argument(
        "package",
        help="Path to .zip package",
    )

    install_parser.set_defaults(func=install_command)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()