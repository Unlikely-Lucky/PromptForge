from pathlib import Path
import zipfile
import tempfile
import shutil
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


def install_skill(zip_path: str):
    archive_path = Path(zip_path)

    if not archive_path.exists():
        print(f"Error: '{zip_path}' does not exist.")
        return

    if archive_path.suffix != ".zip":
        print("Error: Only .zip packages are supported.")
        return

    print(f"Installing {archive_path.name}...")

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)

        with zipfile.ZipFile(archive_path, "r") as archive:
            archive.extractall(temp_dir)

        files = {file.name for file in temp_dir.iterdir()}

        missing = REQUIRED_FILES - files

        if missing:
            print("Error: Invalid PromptForge package.")
            print("Missing files:")

            for item in sorted(missing):
                print(f"  - {item}")

            return

        metadata = yaml.safe_load(
            (temp_dir / "metadata.yaml").read_text(encoding="utf-8")
        )

        skill_name = metadata["name"]

        destination = Path("skills") / skill_name

        if destination.exists():
            print(f"Error: Skill '{skill_name}' is already installed.")
            return

        shutil.copytree(temp_dir, destination)

    print("✓ Package verified")
    print(f"✓ Installed to {destination}")