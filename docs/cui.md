# CUI (Concept unique identifier)

## What is CUI?

In the Unified Medical Language System (UMLS) of the National Library of Medicine (NLM) the concept unique identifier (CUI) is an 8-character identifier beginning with the letter "C" and followed by 7 digits. Each concept is assigned such a CUI. The CUI has no intrinsic meaning but remains constant through time and across versions. (NCI Thesaurus)

## What is CUI2Vec

Cui2Vec is a new set of embeddings for medical concepts learned using an extremely large collection of multimodal medical data.
[See this paper.](https://arxiv.org/abs/1804.01486)

## How does Hephaestus use CUI2Vec

Hephaestus uses Cui2Vec for various concept similarity searches,
by mapping OMOP CDM concepts to CUIs and back.

* Create tables using instructions here: https://github.com/E-Health/OHDSIconceptid2cui
* Cui.init_model() downloads and builds [Cui2Vec](https://arxiv.org/abs/1804.01486) model.
* Find similar concepts, outliers and calculate distances.
* Cui2Vec for noisy labeling and anchor learning.
* [See Also: AMPHRODITE R Package](https://github.com/OHDSI/Aphrodite)
