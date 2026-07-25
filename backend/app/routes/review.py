from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse

from app.services.github_service import github_service

from app.services.file_reader import read_python_files
from app.services.gemini_service import (
    stream_review,
    generate_review,
    gen_project_review,
)
from app.services.input_validator import validate_input, validate_project

router = APIRouter()


@router.post("/review")
async def review_code(
    files: list[UploadFile] | None = File(None),
    code: str | None = Form(None),
):

    if code:
        validation = validate_input(code)

        if not validation["valid"]:
            return validation

        return StreamingResponse(
            stream_review(code),
            media_type="text/plain",
        )

    if files:
        python_files = await read_python_files(files)

        validation = validate_project(python_files)

        if not validation["valid"]:
            return validation

        return StreamingResponse(
            gen_project_review(python_files),
            media_type="text/plain",
        )

    return {
        "valid": False,
        "message": "Please upload a project folder or paste Python code."
    }

@router.post("/review/github")
async def review_and_post(
    code: str = Form(...),
):
    validation = validate_input(code)

    if not validation["valid"]:
        return validation

    review = generate_review(code)

    github_service.post_issue_comment(
        owner="Rohit242524",
        repo="KrishiMitra",
        pr_number=1,
        review=review,
    )

    return {
        "success": True,
        "message": "Review posted to GitHub successfully."
    }