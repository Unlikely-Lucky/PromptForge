from ..generators.skill import create_skill
from ..utils import validate_skill_name


def run(args):
    try:

        if args.name:

            valid, message = validate_skill_name(args.name)

            if not valid:
                print(f"Error: {message}")
                return

            name = args.name

        else:

            while True:
                name = input("Skill name: ").strip()

                valid, message = validate_skill_name(name)

                if valid:
                    break

                print(f"Error: {message}")

        description = input("Description: ").strip()

        while not description:
            print("Description cannot be empty.")
            description = input("Description: ").strip()

        author = input("Author: ").strip()

        while not author:
            print("Author cannot be empty.")
            author = input("Author: ").strip()

        license_name = input("License [MIT]: ").strip()

        if not license_name:
            license_name = "MIT"

        create_skill(
            name=name,
            description=description,
            author=author,
            license_name=license_name,
        )

    except FileExistsError as e:
        print(f"Error: {e}")

    except KeyboardInterrupt:
        print("\nOperation cancelled.")