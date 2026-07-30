from pathlib import Path
import yaml

REQUIRED_FILES = {
    "README.md",
    "SKILL.md",
    "prompt.md",
    "examples.md",
    "eval.md",
    "metadata.yaml",
    "CHANGELOG.md",
}

REQUIRED_METADATA = {
    "name",
    "version",
    "author",
    "description",
    "license",
}


def validate_skill(path: Path) -> list[str]:
    errors = []

    # Check required files
    for filename in REQUIRED_FILES:
        if not (path / filename).exists():
            errors.append(f"Missing file: {filename}")

    metadata_file = path / "metadata.yaml"

    if metadata_file.exists():
        try:
            metadata = yaml.safe_load(
                metadata_file.read_text(encoding="utf-8")
            ) or {}

            for field in REQUIRED_METADATA:
                value = metadata.get(field)

                if value is None:
                    errors.append(f"Missing field: {field}")
                elif isinstance(value, str) and value.strip() == "":
                    errors.append(f"Empty field: {field}")

        except Exception as e:
            errors.append(f"Invalid metadata.yaml ({e})")

    return errors


def validate_all(skills_dir=Path("skills")):

    if not skills_dir.exists():
        print("No skills directory found.")
        return 1

    print("PromptForge Validation Report")
    print("=" * 30)
    print()

    validated = 0
    total_errors = 0

    for skill in sorted(skills_dir.iterdir()):
        if not skill.is_dir():
            continue

        errors = validate_skill(skill)

        if errors:
            print(f"✗ {skill.name}")
            for error in errors:
                print(f"   {error}")
            total_errors += len(errors)
        else:
            print(f"✓ {skill.name}")

        validated += 1

    print()
    print(f"Validated: {validated} skills")
    print(f"Errors: {total_errors}")

    return 0 if total_errors == 0 else 1