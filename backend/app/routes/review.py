from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse

from app.services.file_reader import read_python_files
from app.services.gemini_service import gen_review, gen_project_review
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
            gen_review(code),
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