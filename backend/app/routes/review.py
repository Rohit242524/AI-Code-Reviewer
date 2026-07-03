from fastapi import APIRouter

from app.models.review_models import ReviewReq, ReviewRes
from app.services.gemini_service import gen_review
from app.services.input_validator import validate_input

router = APIRouter()


@router.post("/review", response_model=ReviewRes)
def reviewCode(request: ReviewReq):
    validation = validate_input(request.code)

    if not validation["valid"]:
        return validation

    review = gen_review(request.code)

    return ReviewRes(
        review=review
    )