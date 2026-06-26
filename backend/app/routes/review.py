from fastapi import APIRouter

from backend.app.models.review_models import ReviewReq, ReviewRes
from backend.app.services.gemini_service import gen_review

router = APIRouter()


@router.post("/review", response_model=ReviewRes)
def reviewCode(request: ReviewReq):

    review = gen_review(request.code)

    return ReviewRes(
        review=review
    )