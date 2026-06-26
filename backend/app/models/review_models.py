from pydantic import BaseModel

class ReviewReq(BaseModel):
    code : str

class ReviewRes(BaseModel):
    review : str
