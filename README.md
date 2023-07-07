# Deep learning approaches to the phylogenetic placement of extinct pollen morphotypes
Code for a variety of pollen recognition tasks, including classification, novelty detection, and phylogenetic placement in a reference evolutionary tree. 

<p align="center">
  <img src="https://github.com/paleopollen/Novel_Pollen_Phylogenetic_Placement/blob/main/Figures/Pipeline_and_MLP.png" width = 950 title="hover text">
  
<p align="center">
  <img src="https://github.com/paleopollen/Novel_Pollen_Phylogenetic_Placement/blob/main/Figures/Images_and_Confusion_Matrix_Podocarpus.png" width = 850 title="hover text">
  
<p align="center">
  <img src="https://github.com/paleopollen/Novel_Pollen_Phylogenetic_Placement/blob/main/Figures/ROC_and_MCC_Podocarpus.png" title="hover text">

# Abstract
The phylogenetic interpretation of pollen morphology is limited by our inability to recognize the evolutionary history embedded in pollen features. Deep learning offers tools for connecting morphology to phylogeny. Using neural networks, we developed an explicitly phylogenetic toolkit for analyzing the overall shape, internal structure, and texture of a pollen grain. Our analysis pipeline classifies pollen specimens and determines whether a testing specimen is from any novel species based on uncertainty estimate. Features of novel specimens are passed to a multi-layer perceptron network trained to transform these features into predicted phylogenetic distances from known taxa. We used these predicted distances to place specimens in a phylogeny using Bayesian inference. We trained and evaluated our models using optical superresolution micrographs of 30 _Podocarpus_ species. We then used trained models to place nine fossil _Podocarpidites_ specimens within the phylogeny. We demonstrate that the phylogenetic history encoded in pollen morphology can be recognized by neural networks and that deep-learned features can be used in phylogenetic placement. Our approach makes extinction and speciation events that would otherwise be masked by the limited taxonomic resolution of the fossil pollen record visible to palynological analysis.

# Significance Statement 
Machine learned features from deep neural networks can do more than categorize and classify biological images. We demonstrate that these features can also be used to quantify morphological differences among pollen taxa, discover novel morphotypes, and place fossil specimens on a phylogeny using Bayesian inference. Deep learning can be used to characterize and identify and morphological features with evolutionary significance. These features can then be used to infer phylogenetic distance. This approach fundamentally changes how fossil pollen morphology can be interpreted, allowing greater evolutionary inference of fossil pollen specimens. The analysis framework, however, is not specific to pollen and can be generalized to other taxa and other biological images.

# Main Structure 
There are five folders in this repository:
1. [Training and classification](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/00_Training_and_Classification): Scripts for training the three main models described in the paper using three modalities: maximum intensity projection (MIP) images, cross-sectional images, and patches.
2. [Novelty detection experiment](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/01_Novelty_Detection_Experiment): Script for detecting novel pollen morphotypes, based on the model's uncertainty (inferred from Shannon entropy) when encountering an unknown pollen specimen. The folder also contains a script for computing the optimal entropy threshold.
3. [Phylogenetic placement experiment](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/02_Phylogenetic_Placement_Experiment): Script for training and evaluating phylogenetically-informed neural networks. The experiment is conducted using a simulated dataset with pseudo-novel taxa, which are placed on a reference phylogenetic tree. 
4. [Fossil analysis](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/03_Fossil_Analysis): Script for placing novel fossil types on a reference phylogenetic tree. 
5. [Morphological visualization](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/04_Morphological_Visualization): Script for visualizing the most phylogenetically informative cross-sectional images and patches.

# Hardware Specifications
Experiments were conducted on an NVIDIA GeForce RTX3090 GPU card with 24 GB of memory and an NVIDIA A100 SXM4 card with 40 GB of memory. We used the [PyTorch toolbox](https://pytorch.org/) for training neural networks.
