from pydantic import BaseModel, field_validator
from typing import Literal


class Question(BaseModel):
    type: Literal["technical", "behavioral", "situational"]
    question: str

    @field_validator("type", mode="before")
    def normalize_type(cls, v):

        mapping = {
            "situational_judgment": "situational",
            "situational judgement": "situational",
            "judgment": "situational",
            "situational_judgment_question": "situational"
        }

        return mapping.get(v, v)