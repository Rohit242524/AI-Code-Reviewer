from fastapi import APIRouter
router = APIRouter()

from backend.app.models.review_models import( ReviewReq , ReviewRes)

@router.post("/review", response_model = ReviewRes)
def reviewCode(request: ReviewReq):
    return ReviewRes(
        review = "testing response from reviewcode function"
    )