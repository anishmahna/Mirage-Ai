# Mirage AI – Adversarial Image Cloaking Tool

Mirage AI is a deep learning–based adversarial image cloaking system designed to protect
faces and artworks from unauthorized AI model training. The system applies imperceptible
perturbations to images that preserve human visual quality while causing modern computer
vision models to misclassify or fail recognition.

This project focuses on defensive and privacy-preserving AI, addressing growing concerns
around data misuse, facial privacy, and intellectual property protection in the age of
large-scale AI training.

---

## Problem Statement

Modern AI systems can scrape and train on publicly available images without consent.
This creates serious privacy and intellectual property risks for individuals and artists.

Mirage AI mitigates this by generating adversarially cloaked images that:
- Appear unchanged to humans
- Break recognition and classification by AI models

---

## Key Features

- Adversarial Image Cloaking using imperceptible perturbations
- Implements FGSM, PGD, and One-Pixel Attacks
- Targets state-of-the-art vision models:
  - ResNet
  - FaceNet
  - CLIP
- Supports face protection and digital art protection
- Flask-based API for real-time cloaking
- Modular and extensible architecture

---

## System Architecture

1. Input Image (Face or Artwork)
2. Target Vision Model (ResNet / FaceNet / CLIP)
3. Adversarial Attack Engine
4. Cloaked Image Output
5. Evaluation using evasion metrics

---

## Technology Stack

- Python
- PyTorch
- Adversarial Machine Learning
- CNNs and Vision Transformers
- Flask (API)
- NumPy, OpenCV

---

## Evaluation Metrics

- Evasion Rate (percentage of misclassified samples)
- Visual Similarity (human-perceptible quality)
- Model Robustness Comparison across architectures

---

## Results Summary

The system achieves high evasion effectiveness across multiple vision models, with an
average evasion rate of approximately 94% under both white-box and black-box attack
settings.

---

## Ethical Considerations

This project is developed strictly for research, privacy protection, and defensive AI
purposes. It does not promote malicious use of adversarial techniques.

---

## Future Enhancements

- Support for video-based cloaking
- Adaptive adversarial attacks
- Integration with watermarking techniques
- Robustness evaluation against adversarial defenses

