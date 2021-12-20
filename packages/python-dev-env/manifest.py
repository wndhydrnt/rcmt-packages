import os.path
import subprocess
import sys

from ruamel.yaml import YAML
from rcmt.package import Manifest
from rcmt.package.action import Merge, Seed, Action


class Dependabot(Action):
    def apply(self, pkg_path: str, repo_path: str, tpl_data: dict) -> None:
        cfg_path = os.path.join(repo_path, ".github", "dependabot.yml")
        if os.path.exists(cfg_path) is False:
            return None

        yaml = YAML()
        with open(cfg_path, "r") as cfg_file:
            cfg = yaml.load(cfg_file)

        if "updates" not in cfg:
            return None

        for entry in cfg["updates"]:
            if entry["package-ecosystem"] != "pip":
                continue

            entry["ignore"] = [
                {"dependency-name": "black"},
                {"dependency-name": "isort"},
                {"dependency-name": "mypy"},
            ]

        with open(cfg_path, "w") as cfg_file:
            yaml.dump(cfg, cfg_file)


class Poetry(Action):
    def apply(self, pkg_path: str, repo_path: str, tpl_data: dict) -> None:
        args = ["/home/rcmt/.local/bin/poetry", "update", "black", "isort", "mypy"]
        result = subprocess.run(args, cwd=repo_path, stdout=sys.stdout, stderr=sys.stderr)
        if result.returncode != 0:
            raise RuntimeError(f'Command "poetry update" exited with code {result.returncode}')


with Manifest(name="python-dev-env") as manifest:
    manifest.add_action(Merge(selector="pyproject.toml", source="pyproject.toml"))
    manifest.add_action(Dependabot())
    manifest.add_action(Poetry())
    manifest.add_action(Seed(target=".gitignore", source=".gitignore"))
