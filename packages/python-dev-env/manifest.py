from rcmt.package import Manifest
from rcmt.package.action import Own, Merge, Seed

with Manifest(name="python-dev-env") as manifest:
    manifest.add_action(Merge(selector="pyproject.toml", source="pyproject.toml"))
    manifest.add_action(Seed(target=".gitignore", source=".gitignore"))
