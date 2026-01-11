"""
cloak_image.py

Applies adversarial cloaking to an input image
using FGSM and a target vision model.
"""

import torch
import torch.nn.functional as F


def cloak_image(model, image, label, epsilon=0.03):
    """
    Generates an adversarially cloaked image.

    Args:
        model (torch.nn.Module): Target model
        image (torch.Tensor): Input image (1 x C x H x W)
        label (torch.Tensor): Ground truth label
        epsilon (float): FGSM strength

    Returns:
        torch.Tensor: Cloaked image
    """
    image.requires_grad = True
    output = model(image)
    loss = F.cross_entropy(output, label)

    model.zero_grad()
    loss.backward()

    gradient = image.grad.data
    from attacks.fgsm import fgsm_attack
    cloaked_image = fgsm_attack(image, epsilon, gradient)

    return cloaked_image
