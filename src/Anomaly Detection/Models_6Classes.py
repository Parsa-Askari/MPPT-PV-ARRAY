class ResnetModel(nn.Module):
    def __init__(self,latent_dim=128,classification_mode=False):
        super(ResnetModel,self).__init__()
        self.classification_mode=classification_mode
        resnet=models.resnet50(weights="DEFAULT")
        self.model=nn.Sequential(*list(resnet.children())[:-2])
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.flatten=nn.Flatten(1)
        self.projection_head=nn.Sequential(
            nn.Linear(2048, 2048),
            nn.ReLU(inplace=True),
            nn.Linear(2048, latent_dim)
        )
        # self.model=resnet
    def set_classification_mode(self,mode=True):
        self.classification_mode=mode
    def forward(self,x):
        z=self.model(x)
        z=self.avgpool(z)
        z=self.flatten(z)
        if(not self.classification_mode):
            z=self.projection_head(z)
        return z
        # return z

class BaseClassifier(nn.Module):
    def __init__(self,encoder,classifier,train_encoder):
        super().__init__()
        self.encoder=encoder
        self.classifier=classifier
        self.train_encoder=train_encoder
    def train(self,mode=True):
        self.classifier.train(mode)
        if(self.train_encoder):
            self.encoder.train(mode)
        else:
            self.encoder.eval()
        return self
    def forward(self,x):
        if(self.train_encoder):
            embs=self.encoder(x)
        else:
            with torch.no_grad():
                embs=self.encoder(x)
        return self.classifier(embs)
        
class Classifier(BaseClassifier):
    def __init__(self,encoder,class_count,input_dim=2048,latent_dim=128,train_encoder=False):
        encoder=encoder
        classifier=nn.Sequential(
            nn.Linear(input_dim, input_dim),     
            nn.BatchNorm1d(input_dim),
            nn.ReLU(inplace=True),
            nn.Dropout(0.2),
            nn.Linear(input_dim, 12)

        )
        super().__init__(encoder,classifier,train_encoder)
        if(not self.train_encoder):
            for p in self.encoder.parameters():
                p.requires_grad = False
