import torch
import torch.nn as nn
from Models_6Classes import *

## load Encoder
encoder_param_path = "../Best Models/resnet_98_92.pth"
class_count=6

device= "cuda" if torch.cuda.is_available() else "cpu"

encoder_model=ResnetModel(latent_dim=1000)
encoder_model.load_state_dict(torch.load(encoder_param_path,
                                         weights_only=True,
                                         map_location=torch.device(device)))

# encoder_model.set_classification_mode(False)
# For 9 class
encoder_model.set_classification_mode(True)
## load Classifier
encoder_param_path="../Best Models/classifier_98_92.pth"
classifier_model=Classifier(
    encoder=encoder_model,
    input_dim=1000, 
    latent_dim=512,
    train_encoder=False,
    class_count=class_count)

classifier_model.load_state_dict(torch.load(encoder_param_path,
                                            weights_only=True,
                                            map_location=torch.device(device)))