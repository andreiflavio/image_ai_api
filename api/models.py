from typing import Union
from pydantic import BaseModel, validator, Field


class Image(BaseModel):
    content: str = Field(description="Must be an image in base 64 format.")
    minimum_possibility: Union[int, None] = None

    @validator("content")
    def replace_prefix(cls, v):
        return v.replace("data:image/jpeg;base64,", "")
