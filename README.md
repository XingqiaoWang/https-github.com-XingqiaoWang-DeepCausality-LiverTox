# Introduction

This repository contains software and data for "DeepCausality: A General AI-powered Causal Inference Framework for Free Text – A Case Study of LiverTox".
The paper describes a general causal inference framework named DeepCausality to empirically estimate the causal factors for suspected endpoints embedded in the free text. The proposed DeepCausality seamlessly incorporates AI-powered language models, named  d entity recognition and Judea Pearl’s Do-calculus, into a general framework for causal inference to fulfill different domain-specific applications.
1. ALBERT: [github.com/google-research/albert](https://github.com/google-research/albert);
2. And Judea Pearl’s Do-calculus. 


# Requirements and setup

The proposed DeepCausality framework was exemplified based on a BioBERT (BioBERT, https://github.com/dmis-lab/biobert)
and BERN under 
Python 3.6 
TensorFlow version 1.15

# Data

The dataset we used in this program is LiverTox database (https://www.ncbi.nlm.nih.gov/books/NBK547852/)
For convience, you can get the preprocessed dataset from

# Reproducing the Analgesics-induced acute liver failure experiments

The default settings for the code match the settings used in the software.

1. You'll run from `src` code as 
`./Analgesics-induced_acute_liver_failure/data_processing.sh`
Before doing this, you'll need to put the datset.csv file to `dat/Analgesics-induced_acute_liver_failure/dataset/` directory.
2. Then you'll run `./Analgesics-induced_acute_liver_failure/run_ALBERT.sh`
Before doing this, you'll need to change `ALBERT_BASE_DIR=../ALBERT/model` to `ALBERT_BASE_DIR=[PATH to ALBERT MODEL]`
3. Finally, you'll run `./Analgesics-induced_acute_liver_failure/run_casual_inference.sh`, and you can find the causal results csv files in the `dat/Analgesics-induced_acute_liver_failure\causal_result`


# Reproducing the Tramadol-related_mortalities experiment

1. You'll run from `src` code as 
`./Tramadol-related mortalities/data_processing.sh`
Before doing this, you'll need to put the datset.csv file to `dat/Tramadol-related mortalities/dataset/` directory.
2. Then you'll run `./Tramadol-related mortalities/run_ALBERT.sh`
Before doing this, you'll need to change `ALBERT_BASE_DIR=../ALBERT/model` to `ALBERT_BASE_DIR=[PATH to ALBERT MODEL]`
3. Finally, you'll run `./Tramadol-related mortalities/run_casual_inference.sh`, and you can find the causal results csv files in the `dat/Tramadol-related mortalities\causal_result`

# Other FAERS dataset
Instructions for running other experiments are essentially the same as for Analgesics-induced acute liver failure


