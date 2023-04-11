# Deep learning approaches to the phylogenetic placement of novel fossil pollen
Code for a variety of pollen recognition tasks, including classification, novelty detection, and phylogenetic placement on a reference evolutionary tree. 

<p align="center">
  <img src="https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/blob/main/Figs/Pipeline_MLP_Combined.png" width = 950 title="hover text">
  
<p align="center">
  <img src="https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/blob/main/Figs/Confusion_Matrices_Averaged_Fused_Models_Arial_F.png" width = 950 title="hover text">
  
<p align="center">
  <img src="https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/blob/main/Figs/Novelty_Placement_Combined_Figures_F_Sp.png" title="hover text">

# Abstract
Phylogenetic interpretation of pollen morphology is hindered by our inability to recognize the evolutionary history embedded in pollen features. Deep learning offers potential tools for connecting morphology to phylogeny. Using deep neural networks, we developed an explicitly phylogenetic toolkit for analyzing the overall shape, internal structure, and texture of a pollen grain. Our analysis pipeline both classifies pollen specimens and determines the optimal threshold of classification uncertainty for identifying a specimen as novel. Features of novel specimens are passed to a multi-layer perceptron network trained to transform these features into predicted phylogenetic distances from known taxa. We used these predicted distances to place the specimen in a phylogeny. We trained and evaluated our models using optical superresolution micrographs of 34 species of the Bombacoideae subfamily (Malvaceae) and 30 Podocarpus species. With these models, we placed 23 fossil specimens in their respective phylogenies. Our results demonstrate that the phylogenetic history encoded in pollen morphology can be recognized by neural networks and that deep-learned features can be used in phylogenetic placement. Our approach makes cryptic extinction and speciation events - events that are masked by the limited taxonomic resolution of the fossil pollen record - visible with pollen data and allows molecular phylogenies to be calibrated using this extensive microfossil record.

# Significance Statement 
Pollen features have limited homology across clades, which makes interpretating morphology in a phylogenetic framework challenging and circumscribes evolutionary and paleoecological interpretations of this global, abundant, and temporally expansive terrestrial fossil record. Our analysis uses learned features from deep neural networks to quantify morphological differences among pollen taxa, discover novel morphotypes, and place fossil specimens on a phylogeny. Our approach fundamentally changes how fossil pollen morphology can be interpreted, allowing greater evolutionary inference from fossil pollen specimens. Our analysis framework, however, is not specific to pollen and can be generalized to other taxa and other forms of phenotypic data.

# Main Structure 
There are five folders in this repository:
1. [Training and classification](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/00_Training_and_Classification): Scripts for training the three main models described in the paper using three modalities: maximum intensity projection (MIP) images, cross-sectional images, and patches.
2. [Novelty detection experiment](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/01_Novelty_Detection_Experiment): Script for detecting novel pollen morphotypes, based on the model's uncertainty (inferred from Shannon entropy) when encountering an unknown pollen specimen. The folder also contains a script for computing the optimal entropy threshold.
3. [Phylogenetic placement experiment](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/02_Phylogenetic_Placement_Experiment): Script for training and evaluating phylogenetically-informed neural networks. The experiment is conducted using a simulated dataset with pseudo-novel taxa, which are placed on a reference phylogenetic tree. 
4. [Fossil analysis](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/03_Fossil_Analysis): Script for placing novel fossil types on a reference phylogenetic tree. 
5. [Morphological visualization](https://github.com/madaime2/Novel_Pollen_Phylogenetic_Placement/tree/main/04_Morphological_Visualization): Script for visualizing the most phylogenetically informative cross-sectional images and patches.

# Hardware Specifications
Experiments were conducted on an NVIDIA GeForce RTX3090 GPU card with 24 GB of memory and an NVIDIA A100 SXM4 card with 40 GB of memory. We used the [PyTorch toolbox](https://pytorch.org/) for training neural networks.
