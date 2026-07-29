from pathlib import Path


TEMPLATE_DIR = Path("templates") / "skill"


def load_template(filename: str) -> str:
    template = TEMPLATE_DIR / filename

    if not template.exists():
        raise FileNotFoundError(f"Missing template: {filename}")

    return template.read_text(encoding="utf-8")


def create_skill(name: str) -> None:
    root = Path("skills") / name

    if root.exists():
        raise FileExistsError(f"Skill '{name}' already exists.")

    root.mkdir(parents=True)

    for template in TEMPLATE_DIR.glob("*.tpl"):
        content = load_template(template.name)

        content = content.format(name=name)

        output_file = root / template.stem

        output_file.write_text(
            content,
            encoding="utf-8",
        )

    print(f"✓ Created skill: {root}")