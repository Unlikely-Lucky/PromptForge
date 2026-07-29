# PromptForge Skill Specification (PFSS)

**Version:** 1.0.0  
**Status:** Draft

---

# 1. Purpose

A PromptForge Skill is a reusable, documented capability for an AI system.

Unlike a single prompt, a skill contains documentation, implementation guidance,
examples, evaluation criteria, and metadata so it can be reused, reviewed, and
improved over time.

---

# 2. Required Structure

Every skill MUST follow this structure.

skills/
└── <skill-name>/
    ├── README.md
    ├── SKILL.md
    ├── prompt.md
    ├── examples.md
    ├── eval.md
    ├── metadata.yaml
    └── CHANGELOG.md

---

# 3. Required Files

README.md
: Overview for users.

SKILL.md
: Full specification of the skill.

prompt.md
: Core prompt or instruction set.

examples.md
: Input/output examples.

eval.md
: Evaluation criteria and test cases.

metadata.yaml
: Machine-readable metadata.

CHANGELOG.md
: Version history.

---

# 4. Design Principles

Every PromptForge skill should be:

- Reusable
- Modular
- Well documented
- Versioned
- Testable
- Provider agnostic

---

# 5. Versioning

Semantic Versioning (SemVer) is recommended.

Major.Minor.Patch

Example:

1.0.0

---

# 6. Compatibility

Skills should avoid provider-specific behavior whenever possible.

Compatibility examples:

- OpenAI
- Anthropic
- Google
- Local LLMs

---

# 7. Contribution Requirements

Every contribution must include:

- Documentation
- Examples
- Metadata
- Evaluation

Incomplete skills should not be merged.

---

# 8. Future Extensions

Future versions may support:

- Dependencies
- Skill composition
- Tool integration
- Validation schema
- Skill registry