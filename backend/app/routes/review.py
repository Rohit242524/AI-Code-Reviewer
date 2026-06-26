from fastapi import APIRouter
router = APIRouter()

from app.models.review_models import ReviewReq, ReviewRes
from app.services.gemini_service import gen_review


@router.post("/review", response_model = ReviewRes)
def reviewCode(request: ReviewReq):
    review = gen_review(request.code)
    return ReviewRes(
        review = review
    )