# Inference is Everything: Recasting Semantic Resources into a Unified Evaluation Framework
Authors: Aaron Steven White, Kevin Duh, Pushpendre Rastogi, Benjamin Van Durme

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
  + Definite Pronoun Resolution (DPR) dataset
+ Convert to text-hypothesis pairs with entailed/not-entailed labels.
