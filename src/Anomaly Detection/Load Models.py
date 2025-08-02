import torch
import torch.nn as nn
## load Encoder
encoder_param_path = "../Best Models/resnet_86_85.pth"
encoder_model=ResnetModel(latent_dim=1000)
encoder_model.load_state_dict(torch.load(encoder_param_path,weights_only=True))

## load Classifier
encoder_param_path="../Best Models/classifier_86_85.pth"
classifier_model=Classifier(
    encoder=encoder_model,
    input_dim=2048,
    latent_dim=512,
    train_encoder=False,
    class_count=9)
classifier_model.load_state_dict(torch.load(encoder_param_path,weights_only=True))