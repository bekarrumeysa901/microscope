import os
from tkinter import Tk,filedialog
from Constants import inference_model_path 

def move_png_files(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".png"):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                os.rename(source_path, destination_path)
                print(f"Moved {file} to {destination_folder}")
                
def execute():
    root = Tk()
    root.withdraw()  
    current_directory = os.getcwd()
    print("Please select the files for get Inference results..")
    file_paths = filedialog.askopenfilenames(title="Select File(s)", \
                                             filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")], initialdir=current_directory)

    print("Libraries loading please wait..")
    from ultralytics import YOLO

    model = YOLO(inference_model_path)
    for file in file_paths:
        model.predict(file, save=True, show_conf=False)
    
    
    source_folder = "./runs/detect/predict"
    destination_folder = "./runs/"

    image_folders = [folder[-1] for folder in os.listdir('./') if folder.startswith('Inference_Results_')]
    FINDING_FOLDER_COUNT = 1 + int(max(image_folders)) if image_folders else 1

    move_png_files(source_folder, destination_folder)

    os.rmdir('./runs/detect/predict/')
    os.rmdir('./runs/detect/')
    os.rename("./runs", 'Inference_Results_'+str(FINDING_FOLDER_COUNT))
