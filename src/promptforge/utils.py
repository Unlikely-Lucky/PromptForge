import re
from pathlib import Path


SKILL_NAME_PATTERN = re.compile(r"^[a-z][a-z0-9_-]*$")


def validate_skill_name(name: str):
    """
    Validate a PromptForge skill name.

    Rules:
    - starts with a lowercase letter
    - contains only lowercase letters, numbers, underscores, and hyphens
    """

    if not name:
        return False, "Skill name cannot be empty."

    if not SKILL_NAME_PATTERN.fullmatch(name):
        return (
            False,
            "Use lowercase letters, numbers, '-' or '_' only, and start with a letter.",
        )

    if (Path("skills") / name).exists():
        return False, f"Skill '{name}' already exists."

    return True, ""