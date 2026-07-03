from fastapi import UploadFile

from app.models.review_models import ProjectFile

IGNORED_PATHS = {
    "venv",
    "__pycache__",
    ".git",
    "node_modules",
    "dist",
    "build",
}


async def read_python_files(files: list[UploadFile]) -> list[ProjectFile]:
    python_files = []

    for file in files:
        file_path = file.filename or ""

        if any(folder in file_path.split("/") for folder in IGNORED_PATHS):
            continue

        if not file_path.endswith(".py"):
            continue

        content = await file.read()

        if not content:
            continue

        python_files.append(
            ProjectFile(
                path=file_path,
                content=content.decode("utf-8", errors="ignore"),
            )
        )

    return python_files