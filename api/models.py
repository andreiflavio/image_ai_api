from typing import Union
from pydantic import BaseModel

class Image(BaseModel):
    content: str
    minimum_possibility: Union[int, None] = None