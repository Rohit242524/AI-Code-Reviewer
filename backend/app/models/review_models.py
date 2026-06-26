from pydantic import BaseModel

class ReviewReq(BaseModel):
    code : str

class ReviewRes(BaseModel):
    summary : str
    issues : list[str]
    suggestions : list[str]
