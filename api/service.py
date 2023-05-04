import os
from datetime import datetime
import base64
from imageai.Detection import ObjectDetection
from .models import Image


class ImageHandler:
    """
    Class to do all operations with images
    """

    def create_temp_image(self, imageb64: str, target_folder: str) -> str:
        imgdata = base64.b64decode(imageb64)
        filename = target_folder + "/image{:%Y%m%d%H%M%S}.jpg".format(datetime.now())
        with open(filename, "wb") as f:
            f.write(imgdata)
        return filename

    def find_objects(self, image: Image):
        execution_path = os.getcwd()
        image_name = self.create_temp_image(
            image.content, os.path.join(execution_path, "api", "images_processed")
        )

        detector = ObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath(os.path.join(execution_path, "yolov3.pt"))
        detector.loadModel()
        detections = detector.detectObjectsFromImage(
            input_image=image_name,
            output_image_path="{}_new.jpg".format(image_name[: image_name.find(".")]),
            minimum_percentage_probability=image.minimum_possibility or 50,
        )

        # for eachObject in detections:
        #     print(
        #         eachObject["name"],
        #         " : ",
        #         eachObject["percentage_probability"],
        #         " : ",
        #         eachObject["box_points"],
        #     )
        #     print("--------------------------------")
