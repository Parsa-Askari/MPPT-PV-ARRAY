import torch
import torch.nn as nn
from Models_9Classes import *

## load Encoder
encoder_param_path = "../Best Models/resnet_86_85.pth"
class_count=9
# For 9 class : class_count=9

device= "cuda" if torch.cuda.is_available() else "cpu"

encoder_model=ResnetModel(latent_dim=1000)
encoder_model.load_state_dict(torch.load(encoder_param_path,
                                         weights_only=True,
                                         map_location=torch.device(device)))


encoder_model.set_classification_mode(True)
## load Classifier
encoder_param_path="../Best Models/classifier_86_85.pth"
classifier_model=Classifier(
    encoder=encoder_model,
    input_dim=2048,
    latent_dim=512,
    train_encoder=False,
    class_count=class_count)

classifier_model.load_state_dict(torch.load(encoder_param_path,
                                            weights_only=True,
                                            map_location=torch.device(device)))