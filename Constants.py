device = 'cpu' #torch.device("cuda" if torch.cuda.is_available() else "cpu") # In raspberry it's just cpu

model_root = "./models/"

inference_model_path = "./models/voltran_640.onnx"

RBC_WBC_path          = model_root+ 'RBC_WBC_Count.pt'
Leukocytes_path       = model_root+ 'Leucocyte.pt'       
Eritrocytes_path      = model_root+ 'Eritrocyte_Anomalies.pt'
Platelets_path        = model_root+ 'Platelet.pt'

#Diagnose with Camera -> the interval of the screenshots and number of inference 
interval_   = 2
num_images_ = 5




