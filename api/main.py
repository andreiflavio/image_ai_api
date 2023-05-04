from .models import Image
from .service import ImageHandler
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/objects")
async def detect(image: Image) -> str:
    """
    This endpoint will process an image in base 64 and find objects within that.
    """
    service = ImageHandler()
    result = service.find_objects(image)
    return result
