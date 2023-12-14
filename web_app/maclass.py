import torch


class QualityPredictor(torch.nn.Module):
    def __init__(self, input_shape):
        super(QualityPredictor, self).__init__()

        self.linear1 = torch.nn.Linear(8, 20)
        self.relu1 = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(20, 1)
        self.relu2 = torch.nn.ReLU()

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu1(x)
        x = self.linear2(x)
        x = self.relu2(x)
        return x
