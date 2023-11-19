---
layout: post
title: "Bayesian Methods"
date: 2023-11-19
tags: [bayesian methods, statistics]
---

# Bayesian Methods

---

- [Bayesian Methods](#bayesian-methods)
  - [Introduction](#introduction)
  - [Bayesian Inference](#bayesian-inference)
  - [References](#references)
  

## Introduction
Bayesian methods are a set of statistical techniques that are based on the idea of using prior knowledge to make predictions about future events. They are often used in machine learning and artificial intelligence to make predictions about the future based on past data. Bayesian methods are also used in statistics to estimate parameters of a probability distribution.

> **NOTE:**
> If Bayesian inference is the destination, there are 2 paths: Math analysis or probabilistic programming.


## Bayesian Inference

  - Bayesian inference is simply updating your beliefs after considering new evidence.
  - We update our beliefs about an outcome, but rarely can we be absolutely sure unless we rule out all other alternatives.
  - Differs from more traditional statistical inference by preserving uncertainty.
  - Frequentists use the term probability to describe the long-run frequency of events, whereas Bayesians use probability to describe the degree of belief, or confidence, in an event occurring.
  - If frequentist and Bayesian inference were programming functions, with inputs being
statistical problems, frequentist inference function would return a number, representing an estimate (typically a summary statistic like the sample average), whereas the Bayesian function would return probabilities.
  - Bayesian methods complement frequentist techniques by solving problems that these approaches cannot, or by illuminating the underlying system with more flexible modeling.
  
Bayes’ Theorem, after its discoverer Thomas Bayes:

P(A|X) ∝ P(X|A)P(A)

Here, ∝ means “is proportional to”.

- Bayesian methodology returns a distribution.





## References
- Book:  [Bayesian Methods for Hackers](https://dataorigami.net/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
- GitHub: [Bayesian Methods for Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)