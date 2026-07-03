from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.review_models import ReviewReq
from app.services.gemini_service import gen_review
from app.services.input_validator import validate_input

router = APIRouter()


@router.post("/review")
def review_code(request: ReviewReq):

    validation = validate_input(request.code)

    if not validation["valid"]:
        return validation

    return StreamingResponse(
        gen_review(request.code),
        media_type="text/plain"
    )