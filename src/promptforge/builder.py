from pathlib import Path
import zipfile
import yaml


def build_skill(skill_name: str):
    """Package a PromptForge skill into a ZIP archive."""

    skill_dir = Path("skills") / skill_name

    if not skill_dir.exists():
        print(f"Error: Skill '{skill_name}' does not exist.")
        return

    metadata_file = skill_dir / "metadata.yaml"

    if not metadata_file.exists():
        print("Error: metadata.yaml not found.")
        return

    metadata = yaml.safe_load(
        metadata_file.read_text(encoding="utf-8")
    )

    version = metadata.get("version", "0.0.0")

    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)

    zip_path = dist_dir / f"{skill_name}-{version}.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for file in skill_dir.iterdir():
            archive.write(file, arcname=file.name)

    print()
    print(f"✓ Built {zip_path}")