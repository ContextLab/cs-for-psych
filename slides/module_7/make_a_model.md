---
marp: true
title: Make a model!
description: Introduction to model design and implementation
url: https://github.com/ContextLab/storytelling-with-data
theme: cdl-theme
transition: fade 0.25s
class:
  - lead  
---

# Make a model!
## Jeremy R. Manning
### PSYC 132: Introduction to Programming for Psychological Scientists

---

# What *is* a model (and what do "models" *do*)?

- Capture key attributes of a system or phenomenon (laws of physics, communication patterns, etc.)
- Predict something we can't directly observe (the past, future, hidden states, etc.)
- Simulate some process

---

# What do (real) models "look" like?

- A physical thing in the real world (e.g., a mouse brain is "model" of a human brain)
- A system of differential equations that describe how different variables in a system interact
- A computer program that acts like a "machine" that tries to replicate behavior(s) of the "real" system

---

# What do ("fake") models "look" like?

- Regressions, ANOVAs, statistical tests
- Technically these are "models," but they're not particularly satisfying to build, and in most cases we don't think these approaches "work" anything like what we're trying to explain in the real world

---

# Model *input*

A model's inputs are usually one or more datasets, usually in the form of tables of numbers, that describe the behaviors of different equations or processes encompassed by the model.

![width:700px](https://media.tenor.com/cLnzRPB0jEAAAAAC/ally-sheedy-short-circuit.gif)

---

# Model *output*

The output of a model is usually (also) one or more tables of numbers that describe the behaviors of the equations or processes encompassed by the model


![width:500px](https://miro.medium.com/v2/resize:fit:1400/1*bhFifratH9DjKqMBTeQG5A.gif)

---

# The model "game"

Take in some numbers and give out some (usually different) numbers.

![width:500px](https://cdn-wordpress-info.futurelearn.com/info/wp-content/uploads/1-3-IPO-Football-1.gif)

---

# Why is this interesting/useful?

In the "real world," important stuff happens. In models, we're only pushing numbers around. So...who cares?

---

# The "star trek" version of building a model:

- Scan every molecule in the system
- Input all of the (true) rules of the universe
- Churn through some computations and get out the answer to whatever your question was

![200px](https://i.gifer.com/IQta.gif)

---

# How modeling works in the "real" world:

  - Make up the components of the system you care about
  - Make up some  rules about how the system works
  - Churn through some computations and see how the system behaves

  ![200px](https://media3.giphy.com/media/l0IylOPCNkiqOgMyA/giphy.gif?cid=6c09b952j9guhob9b92sykuu5jcyirwlzzldx25tyj2u64ci&ep=v1_gifs_search&rid=giphy.gif&ct=g)

  ---

  # But...(!!)

- Think about how you'd *represent* a "star trek" style "every molecule" dataset.  Probably...with numbers!
- Think about how you'd write down the rules of the system.  Maybe with equations?  Functions?

---

# So what are models *really* doing?

Computers (and math) can only tell us about the world in the first place by using and manipulating numbers.  For a computer, reality *is* numbers.  *To a computer, there's no distinction between a thing in the real world and the measurement or representation of that thing!*

---

# So what are models *really* doing?

When a number changes in a model, if that number is attached to something you think is meaningful, from the perspective of the computer *it's as though reality itself is changing.* You are the god of your simulated (model) universe.

![width:500px](https://media.tenor.com/D2ZlkeUWSk4AAAAd/zenitsu-god-mode.gif)

---

> All models are wrong, but some are useful
--George Box (1976)

---

# How can you get started?

- What do you want to model?
- How are you going to model it?
  - What are the components/processes in the model's scope?
  - What are the "rules" of the model?
  - How will you get out an "answer" or characterize the model's behaviors?