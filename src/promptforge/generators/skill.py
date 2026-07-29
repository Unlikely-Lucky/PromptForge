from pathlib import Path


TEMPLATE_DIR = Path("templates") / "skill"


def load_template(filename):
    """Load a template file from the templates directory."""
    template_path = TEMPLATE_DIR / filename

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {filename}")

    return template_path.read_text(encoding="utf-8")


def create_skill(
    name,
    description="Describe this skill",
    author="Unknown",
    license_name="MIT",
):
    """Create a new PromptForge skill."""

    skills_dir = Path("skills")
    skill_dir = skills_dir / name

    if skill_dir.exists():
        raise FileExistsError(f"Skill '{name}' already exists.")

    skill_dir.mkdir(parents=True)

    for template in TEMPLATE_DIR.glob("*.tpl"):
        content = load_template(template.name)

        content = content.format(
            name=name,
            description=description,
            author=author,
            license=license_name,
        )

        output_file = skill_dir / template.stem
        output_file.write_text(content, encoding="utf-8")

    print(f"✅ Created skill: {name}")