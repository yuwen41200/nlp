# Inference is Everything: Recasting Semantic Resources into a Unified Evaluation Framework
Authors: Aaron Steven White, Kevin Duh, Pushpendre Rastogi, Benjamin Van Durme

## Why Choose This Paper?
+ I also spend lots of time studying philosophy.
+ "Inference" is also important in *logic*, *epistemology*, and *philosophy of language*.
+ I hope this paper can benefit my studies in both computer science and philosophy.

## Introduction
+ Mission: Recognizing textual entailment (RTE)
  + Evaluate performance of textual inference.
+ Significant Datasets
  + Stanford Natural Language Inference (SNLI) dataset
    + large enough
    + semantic properties not clarified
  + FraCaS dataset
    + specify semantic properties
    + too small
+ Problem: Getting a score is not enough.
  + How to know what types of semantics are a model good/bad at?

## Prior Work
+ Transform natural language sentences into their logical forms.
  + declarative, interpretable logical forms
  + vector space representations + neural networks
    + Hard to understand their behaviors and find errors.
+ Textual Entailment

## Data Creation
+ Construct a unified dataset based on 3 existing datasets featuring 3 different types of semantics.
  + Semantic Proto-Roles v1 (SPR) dataset
    + relations between arguments and predicates
  + FrameNet Plus (FN+) dataset
    + trigger phrase-paraphrase pairs of sentences
  + Definite Pronoun Resolution (DPR) dataset
    + DPR problems (What does this pronoun refer to?) and solutions
+ Convert to text-hypothesis pairs with entailed/not-entailed labels.
+ Validate the new dataset.

## Experiments
+ Using a popular LSTM-based neural RTE model.
+ Train a model on one dataset, and test it on another.
  + Choose from 4 datasets: SPR, FN+, DPR, SNLI.
  + DPR is the most difficult semantics for a model to capture.
  + Performance is fairly good when the training dataset and the testing dataset are the same.
  + SNLI trained model does not perform well except tested on the same dataset.

## Future Work
+ Use this strategy for WSD and PP attachment resolution.
