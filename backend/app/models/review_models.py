from pydantic import BaseModel


class ProjectFile(BaseModel):
    path: str
    content: str


class SkippedFile(BaseModel):
    path: str
    reason: str