from pathlib import Path
import yaml


class Skill:
    def __init__(self, path: Path, metadata: dict):
        self.path = path
        self.metadata = metadata

    @classmethod
    def load(cls, path):
        path = Path(path)

        metadata_file = path / "metadata.yaml"

        if not metadata_file.exists():
            raise FileNotFoundError(metadata_file)

        metadata = yaml.safe_load(
            metadata_file.read_text(encoding="utf-8")
        )

        return cls(path, metadata)

    @property
    def name(self):
        return self.metadata["name"]

    @property
    def version(self):
        return self.metadata["version"]

    @property
    def author(self):
        return self.metadata["author"]

    @property
    def description(self):
        return self.metadata["description"]

    @property
    def license(self):
        return self.metadata["license"]