from pathlib import Path


TEMPLATE_DIR = Path("templates") / "skill"


def load_template(filename, template_dir=TEMPLATE_DIR):
    """Load a template file from the templates directory."""
    template_path = template_dir / filename

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {filename}")

    return template_path.read_text(encoding="utf-8")


def create_skill(
    name,
    description="Describe this skill",
    author="Unknown",
    license_name="MIT",
    skills_dir=Path("skills"),
    template_dir=TEMPLATE_DIR,
):
    """Create a new PromptForge skill."""

    skill_dir = skills_dir / name

    if skill_dir.exists():
        raise FileExistsError(f"Skill '{name}' already exists.")

    skill_dir.mkdir(parents=True)

    for template in template_dir.glob("*.tpl"):
        content = load_template(template.name, template_dir)

        content = content.format(
            name=name,
            description=description,
            author=author,
            license=license_name,
        )

        output_file = skill_dir / template.stem
        output_file.write_text(content, encoding="utf-8")

    print(f"✅ Created skill: {name}")