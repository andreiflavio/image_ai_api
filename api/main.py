from models import Image
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/objects")
async def detect(image: Image):
    '''
    This endpoint will process an image in base 64 and find objects within that.
    '''
    # TODO - Call the grpc service to process that image
    return image