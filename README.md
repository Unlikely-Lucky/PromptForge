# PromptForge

> Build, package, and share reusable AI Prompt Skills.

PromptForge is an open-source command-line tool for creating, validating, packaging, installing, and managing reusable AI Prompt Skills.

Instead of keeping prompts scattered across notes, documents, or chat histories, PromptForge helps organize them into structured, version-controlled skills that can be reused across projects and shared with others.

Whether you're a prompt engineer, AI developer, or researcher, PromptForge provides a consistent workflow for developing and maintaining prompt-based systems.

## ✨ Features

- Create new Prompt Skills from templates
- Validate skill structure and metadata
- Build distributable ZIP packages
- Install packaged skills
- Uninstall installed skills
- View detailed skill information
- List installed skills
- Modular command-based CLI

## Goals

- Create reusable AI skills
- Improve prompt quality
- Standardize AI workflows
- Encourage community collaboration
- Build evaluation-driven prompt engineering

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Unlikely-Lucky/PromptForge.git
cd PromptForge
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**

```powershell
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install PromptForge:

```bash
pip install -e .
```

### 🚀 Quick Start

```bash
# Create a new Prompt Skill
promptforge new skill

# Validate your skills
promptforge validate

# Build a distributable package
promptforge build reply

# Install a package
promptforge install dist/reply-0.1.0.zip

# List installed skills
promptforge list

# View skill information
promptforge info reply
```

## CLI Commands

| Command                         | Description               |
| ------------------------------- | ------------------------- |
| `promptforge new skill`         | Create a new Prompt Skill |
| `promptforge validate`          | Validate installed skills |
| `promptforge list`              | List installed skills     |
| `promptforge info <skill>`      | Show skill details        |
| `promptforge build <skill>`     | Build a ZIP package       |
| `promptforge install <package>` | Install a package         |
| `promptforge uninstall <skill>` | Remove a skill            |


## Repository Structure

```
PromptForge/
├── src/
│   └── promptforge/
│       ├── commands/
│       ├── services/
│       ├── validators/
│       ├── generators/
│       ├── templates/
│       └── cli.py
├── skills/
├── tests/
├── README.md
├── LICENSE
└── pyproject.toml
```

## Roadmap

See ROADMAP.md

## Contributing

See CONTRIBUTING.md

## License

MIT