from pathlib import Path
import zipfile
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


def build_skill(skill_name: str):
    """Package a PromptForge skill into a ZIP archive."""

    skill_dir = Path("skills") / skill_name

    if not skill_dir.exists():
        print(f"Error: Skill '{skill_name}' does not exist.")
        return

    # ---------- Check required files ----------

    missing = []

    for filename in REQUIRED_FILES:
        if not (skill_dir / filename).exists():
            missing.append(filename)

    if missing:
        print("Error: Skill is incomplete.")
        print()

        for file in missing:
            print(f"  Missing: {file}")

        return

    # ---------- Read metadata ----------

    metadata_file = skill_dir / "metadata.yaml"

    metadata = yaml.safe_load(
        metadata_file.read_text(encoding="utf-8")
    )

    # ---------- Validate metadata ----------

    required_fields = [
        "name",
        "version",
        "author",
        "description",
        "license",
    ]

    for field in required_fields:
        if field not in metadata or not metadata[field]:
            print(f"Error: metadata.yaml is missing '{field}'.")
            return

    # ---------- Verify metadata name ----------

    if metadata["name"] != skill_name:
        print()
        print("Error: metadata.yaml does not match the folder name.")
        print(f"Folder   : {skill_name}")
        print(f"Metadata : {metadata['name']}")
        print()
        print("Fix metadata.yaml before building.")
        return

    version = metadata["version"]

    # ---------- Build package ----------

    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)

    zip_path = dist_dir / f"{skill_name}-{version}.zip"

    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED,
    ) as archive:

        for file in skill_dir.iterdir():
            archive.write(
                file,
                arcname=file.name,
            )

    print()
    print("✓ Validation passed")
    print(f"✓ Built {zip_path}")