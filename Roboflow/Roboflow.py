import os
from roboflow import Roboflow

rf = Roboflow(api_key=os.environ["x0mRwD2ree3UvNxKtppV"])
#https://universe.roboflow.com/4564-sdivc/helmet-etb3q
project = rf.workspace("4564-sdivc").project("helmet-etb3q")  # cambia si usas otro dataset
dataset = project.version(1).download("yolov8")  # revisa la versión disponible
