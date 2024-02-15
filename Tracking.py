print("Tracking for Analysis.. Libraries are loading. Please wait")
import subprocess
import os
model_path = "./models/voltran_640.onnx"
def execute():
    yolo_command = f'yolo predict model={model_path} source=0 show=True device=cpu save=False'
    subprocess.run(yolo_command, shell=True, check=True)
    