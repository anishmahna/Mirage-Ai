"""
run_cloak.py

Demo script for adversarial image cloaking.
"""

import torch
from models.resnet import load_resnet
from cloaking.cloak_image import cloak_image


def main():
    model = load_resnet()

    image = torch.rand((1, 3, 224, 224))
    label = torch.tensor([0])

    cloaked = cloak_image(model, image, label)
    print("Cloaked image generated successfully.")


if __name__ == "__main__":
    main()
