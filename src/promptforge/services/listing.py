from pathlib import Path


def list_skills():
    """List all available PromptForge skills."""

    skills_dir = Path("skills")

    if not skills_dir.exists():
        print("No skills directory found.")
        return

    skills = sorted(
        item.name
        for item in skills_dir.iterdir()
        if item.is_dir()
    )

    if not skills:
        print("No skills found.")
        return

    print("Available Skills")
    print("=" * 16)
    print()

    for skill in skills:
        print(f"✓ {skill}")

    print()
    print(f"Total: {len(skills)} skill{'s' if len(skills) != 1 else ''}")