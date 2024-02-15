print("Standart YOLO prediction.. Please wait the libraries are loading at the moment...")
import time
import os
import torch
import cv2

from Constants import *
from ultralytics import YOLO

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 0)
font_thickness = 2
    
image_folders = [folder[-1] for folder in os.listdir('./') if folder.startswith('Diagnose_Result_')]
FINDING_FOLDER_COUNT = 1+int(max(image_folders)) if image_folders else 1
image_path = './Diagnose_Result_'+str(FINDING_FOLDER_COUNT)+'/'

os.mkdir(image_path)
os.mkdir(image_path+'Originals/')

def capture_from_webcam():
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Couldn't open webcam.")
        return

    start_time = time.time()
    count = 0
    countdown = 3  

    while count < num_images_:
        ret, frame = cap.read()
        
        cv2.putText(frame, f"Frame no -> {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        elapsed_time = int(time.time() - start_time)
        countdown_text = f"Countdown: {countdown - elapsed_time}"
        cv2.putText(frame, countdown_text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Inference Frame', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        if elapsed_time > interval_:
            image_name = f"Inference_{count}.png"
            cv2.imwrite(image_path + 'Originals/' + image_name, frame)
            print(f"Captured image: {image_name}")

            start_time = time.time()
            count += 1
            elapsed_time = 0

    cap.release()
    time.sleep(1)
    cv2.destroyAllWindows()
    

def move_images(root_path, destination_path):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    file_counter = 1


    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                source_file_path = os.path.join(root, file)
                destination_file_name = f"{file_counter}_{file}"
                destination_file_path = os.path.join(destination_path, destination_file_name)
                os.rename(source_file_path, destination_file_path)
                file_counter += 1

def get_predicts(results):
    class_counts = {}

    for result in results:
        for box in result.boxes:
            class_id = result.names[box.cls[0].item()]

            if class_id in class_counts:
                class_counts[class_id] += 1
            else:
                class_counts[class_id] = 1
        

def execute():
    
    
    capture_from_webcam()

    RBC_WBC          = YOLO(RBC_WBC_path)
    Leukocytes       = YOLO(Leukocytes_path)
    Eritrocytes      = YOLO(Eritrocytes_path)
    Platelets        = YOLO(Platelets_path)

    model_list = [RBC_WBC, Leukocytes, Eritrocytes, Platelets]

    preds = []
    for model in model_list: 
        results = model.predict(image_path+'Originals/', save=True, show_conf= False)
        preds.append(get_predicts(results))

    root_path = './runs/'
    move_images(root_path, image_path)
    
    
    for root, dirs, files in os.walk('./runs/', topdown=False):
        for dir_name in dirs:
            os.rmdir(os.path.join(root, dir_name))
            
    os.rmdir('./runs/')


   

