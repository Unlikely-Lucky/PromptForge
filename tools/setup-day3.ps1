# PromptForge Day 3 Setup

$docs = @(
    "docs\skill-specification.md",
    "docs\architecture.md",
    "docs\style-guide.md",
    "docs\glossary.md"
)

$skillFiles = @(
    "skills\writing\README.md",
    "skills\writing\SKILL.md",
    "skills\writing\prompt.md",
    "skills\writing\examples.md",
    "skills\writing\eval.md",
    "skills\writing\metadata.yaml",
    "skills\writing\CHANGELOG.md"
)

New-Item -ItemType Directory -Force -Path "skills\writing" | Out-Null

foreach ($file in $docs + $skillFiles) {
    if (-not (Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "Created $file"
    }
}

Write-Host ""
Write-Host "✅ Day 3 scaffold created successfully!"