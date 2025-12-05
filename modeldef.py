import torch
import torch.nn as nn
import torch.optim as optim
class BasicFeatureBasedClassifier(nn.Module):
    def __init__(self, input_features, num_classes):
        super(BasicFeatureBasedClassifier, self).__init__()
        self.layer1 = nn.Linear(input_features, 64) 
        self.relu1 = nn.ReLU()
        self.layer2 = nn.Linear(64, 48)
        self.relu2 = nn.ReLU()
        self.layer3 = nn.Linear(48, 128)
        self.relu3 = nn.ReLU()
        self.output_layer = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu1(x)
        x = self.layer2(x)
        x = self.relu2(x)
        x = self.layer3(x)
        x = self.relu3(x)
        x = self.output_layer(x)
        return x
    
def load_model(model_path, input_features, num_classes):
    model = BasicFeatureBasedClassifier(input_features, num_classes)
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model