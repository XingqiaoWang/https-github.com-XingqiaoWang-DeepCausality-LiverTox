# Introduction

This repository contains software and data for "DeepCausality: A General AI-powered Causal Inference Framework for Free Text – A Case Study of LiverTox".
The paper describes a general causal inference framework named DeepCausality to empirically estimate the causal factors for suspected endpoints embedded in the free text. The proposed DeepCausality seamlessly incorporates AI-powered language models, named  d entity recognition and Judea Pearl’s Do-calculus, into a general framework for causal inference to fulfill different domain-specific applications.
1. ALBERT: [github.com/google-research/albert](https://github.com/google-research/albert);
2. And Judea Pearl’s Do-calculus. 


# Requirements and setup

The proposed DeepCausality framework was exemplified based on BioBERT (BioBERT, https://github.com/dmis-lab/biobert)
Python 3.6 
TensorFlow version 1.15

# Data

The dataset we used in this program is LiverTox database (https://www.ncbi.nlm.nih.gov/books/NBK547852/)
For each drug record, the information was organized based on different sections, including Introduction, Background, Hepatotoxicity, Mechanism of Liver Injury, Outcome and Management, Case reports, Chemical and Product Information, and References. For each drug record, we extracted the sentences from four sections, Introduction, Background, Hepatotoxicity, and Mechanism of Liver Injury, which are the major sections that describe the synthesized knowledge on hepatoxicity. The DILI Likelihood score is embedded in the hepatoxicity section. Each sentence is labeled with the DILI likelihood score of the corresponding drug record.
For convience, you can get the preprocessed dataset from https://drive.google.com/drive/folders/1P6C0JIA2D0lUPMJeH8RkdbJTgsLAgTMz?usp=share_link.

# Name entity recognition

we used biomedical entity recognition and a multi-type normalization tool (BERN) to extract biomedical-related terms, including gene/protein, disease, drug/chemical, species information, and genetic variants. BERN (BERN https://github.com/dmis-lab/bern). The BERN is a series of BioBERT-named entity recognition models with probability-based decision rules to recognize and discover different biomedical entities, accessible through https://bern.korea.ac.kr.
For convience, you can get the BERN results from https://drive.google.com/drive/folders/1P6C0JIA2D0lUPMJeH8RkdbJTgsLAgTMz?usp=share_link.

# Reproducing the LiverTox experiments

The default settings for the code match the settings used in the software.

1. You'll run from `src` code as 
`./Analgesics-induced_acute_liver_failure/data_processing.sh`
Before doing this, you'll need to put the datset.csv file to `dat/Analgesics-induced_acute_liver_failure/dataset/` directory.
2. Then you'll run `./Analgesics-induced_acute_liver_failure/run_ALBERT.sh`
Before doing this, you'll need to change `ALBERT_BASE_DIR=../ALBERT/model` to `ALBERT_BASE_DIR=[PATH to ALBERT MODEL]`
3. Finally, you'll run `./Analgesics-induced_acute_liver_failure/run_casual_inference.sh`, and you can find the causal results csv files in the `dat/Analgesics-induced_acute_liver_failure\causal_result`



