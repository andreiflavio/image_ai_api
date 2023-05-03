import os
from imageai.Detection import ObjectDetection
from .models import Image


class ImageHandler:
    def create_temp_image(self):
        pass

    def remove_temp_image(self):
        pass

    def find_objects(self, image: Image):
        pass

        # execution_path = os.getcwd()

        # detector = ObjectDetection()
        # detector.setModelTypeAsYOLOv3()
        # detector.setModelPath(os.path.join(execution_path, "yolov3.pt"))
        # detector.loadModel()
        # detections = detector.detectObjectsFromImage(
        #     input_image=os.path.join(execution_path, "image2.jpg"),
        #     output_image_path=os.path.join(execution_path, "image2new.jpg"),
        #     minimum_percentage_probability=30,
        # )

        # for eachObject in detections:
        #     print(
        #         eachObject["name"],
        #         " : ",
        #         eachObject["percentage_probability"],
        #         " : ",
        #         eachObject["box_points"],
        #     )
        #     print("--------------------------------")
