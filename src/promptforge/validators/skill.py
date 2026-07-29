from pathlib import Path

REQUIRED_FILES = {
    "README.md",
    "SKILL.md",
    "prompt.md",
    "examples.md",
    "eval.md",
    "metadata.yaml",
    "CHANGELOG.md",
}


def validate_skill(path: Path) -> list[str]:
    errors = []

    for filename in REQUIRED_FILES:
        if not (path / filename).exists():
            errors.append(f"Missing: {filename}")

    return errors


def validate_all():
    skills_dir = Path("skills")

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