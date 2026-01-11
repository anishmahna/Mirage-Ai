"""
fgsm.py

Implements Fast Gradient Sign Method (FGSM)
for adversarial image cloaking.
"""

import torch


def fgsm_attack(image, epsilon, gradient):
    """
    Performs FGSM attack on an input image.

    Args:
        image (torch.Tensor): Original image
        epsilon (float): Perturbation strength
        gradient (torch.Tensor): Gradient of loss w.r.t image

    Returns:
        torch.Tensor: Adversarial (cloaked) image
    """
    sign_gradient = gradient.sign()
    perturbed_image = image + epsilon * sign_gradient
    perturbed_image = torch.clamp(perturbed_image, 0, 1)
    return perturbed_image
