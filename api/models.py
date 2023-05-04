from typing import Union
from pydantic import BaseModel, validator


class Image(BaseModel):
    content: str
    minimum_possibility: Union[int, None] = None

    @validator("content")
    def replace_prefix(cls, v):
        return v.replace("data:image/jpeg;base64,", "")
