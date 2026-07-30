from pathlib import Path
import shutil


def uninstall_skill(skill_name: str):
    skill_dir = Path("skills") / skill_name

    if not skill_dir.exists():
        print(f"Error: Skill '{skill_name}' is not installed.")
        return

    shutil.rmtree(skill_dir)

    print(f"✓ Removed {skill_dir}")