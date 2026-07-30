from pathlib import Path
import yaml


def show_skill_info(skill_name: str):
    """Display metadata for a PromptForge skill."""

    skill_dir = Path("skills") / skill_name

    if not skill_dir.exists():
        print(f"Error: Skill '{skill_name}' does not exist.")
        return

    metadata_file = skill_dir / "metadata.yaml"

    if not metadata_file.exists():
        print("Error: metadata.yaml not found.")
        return

    try:
        metadata = yaml.safe_load(
            metadata_file.read_text(encoding="utf-8")
        ) or {}
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return

    print("Skill Information")
    print("=" * 18)
    print()

    print(f"Name        : {metadata.get('name', '-')}")
    print(f"Version     : {metadata.get('version', '-')}")
    print(f"Author      : {metadata.get('author', '-')}")
    print(f"Description : {metadata.get('description', '-')}")
    print(f"License     : {metadata.get('license', '-')}")