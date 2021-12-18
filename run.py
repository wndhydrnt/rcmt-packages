from rcmt import Run
from rcmt.matcher import FileExists, RepoName

with Run(
    name="python",
    auto_merge=True,
) as run:
    run.add_matcher(FileExists("pyproject.toml"))
    run.add_matcher(RepoName("^github.com/wndhydrnt/.+$"))

    run.add_package("python-dev-env")
