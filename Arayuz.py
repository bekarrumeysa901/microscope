import tkinter as tk
from tkinter import ttk
import os

def Yolo_Camera_Inference():
    import Diagnose_with_Camera as Yolo
    try:
        Yolo.execute()
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    
def Just_Track():
    import Tracking as Track
    try:
        Track.execute()
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    
def Inference():
    import Yolo_Inference as Inference
    try:
        Inference.execute()
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        return

def interface():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    main_window = tk.Tk()
    main_window.title("Main Page")

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    window_width_percentage = 37.5
    window_height_percentage = 45

    window_width = int((window_width_percentage / 100) * screen_width)
    window_height = int((window_height_percentage / 100) * screen_height)

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    main_window.resizable(width=False, height=False)

    style = ttk.Style()
    style.configure("TButton", padding=(10, 5), relief="flat")

    yolo_camera_button = ttk.Button(main_window, text="           Camera Inference             ", \
                                    command=lambda: [main_window.destroy(), Yolo_Camera_Inference(), interface()])
    
    Track_button = ttk.Button(main_window, text="   Just Tracking With Camera   ", \
                              command=lambda: [main_window.destroy(), Just_Track(), interface()])
    
    Inference_button = ttk.Button(main_window, text="  Specific Folder or Image Inference     ", \
                              command=lambda: [main_window.destroy(), Inference(), interface()])
    
    Quit = ttk.Button(main_window, text="        Quit to Terminal               ", command= lambda: [exit()])
    
    yolo_camera_button.place(x=70,y=50)
    Track_button.place(x=330,y=50)
    Inference_button.place(x=50, y= 200)
    Quit.place(x=330, y=200)
    
    main_window.mainloop()


interface()
