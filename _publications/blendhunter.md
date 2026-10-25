---
title: "Deep transfer learning for blended source identification in galaxy survey data"
authors: "Samuel Farrens, Alice Lacan, Axel Guinot, A. Z. Vitorelli"
venue: "Astronomy & Astrophysics, vol. 657, A98"
year: 2022
date: 2022-01-01
type: "journal"
doi: "10.1051/0004-6361/202141166"
link: "https://doi.org/10.1051/0004-6361/202141166"
abstract: "We present BLENDHUNTER, a proof-of-concept deep-transfer-learning-based approach for the automated and robust identification of blended sources in galaxy survey data. We take the VGG-16 network with pre-trained convolutional layers and train the fully connected layers on parametric models of COSMOS images. We test the efficacy of the transfer learning by taking the weights learned on the parametric models and using them to identify blends in more realistic Canada-France Imaging Survey (CFIS)-like images. We compare the performance of this method to SEP (a Python implementation of SEXTRACTOR) as a function of noise levels and the separation between sources. We find that BLENDHUNTER outperforms SEP by ∼15% in terms of classification accuracy for close blends (< 10 pixel separation between sources) regardless of the noise level used for training. Additionally, the method provides consistent results to SEP for distant blends (≥10 pixel separation between sources) provided the network is trained on data with noise that has a relatively close standard deviation to that of the target images. The code and data have been made publicly available to ensure the reproducibility of the results. "
---
