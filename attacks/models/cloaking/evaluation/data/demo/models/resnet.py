"""
resnet.py

Loads a pretrained ResNet model to be used as a target (victim) model
for adversarial image cloaking experiments.
"""

import torchvision.models as models


def load_resnet():
    """
    Loads a pretrained ResNet-50 model in evaluation mode.

    Returns:
        model (torch.nn.Module): Pretrained ResNet model
    """
    model = models.resnet50(pretrained=True)
    model.eval()
    return model
