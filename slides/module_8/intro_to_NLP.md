---
marp: true
title: A quick introduction to natural language processing in Python
description: Introduce some NLP models and approaches
url: https://github.com/ContextLab/storytelling-with-data
theme: cdl-theme
transition: fade 0.25s
class:
  - lead  
---

![bg opacity:0.1](https://uploads-ssl.webflow.com/614c82ed388d53640613982e/635bcc3c2b1b16702f8917c9_634fd7afbe19224c4a7a4a0e_6320786b1cfec14310b5f181_natural-language-processing--NLP-.png)

# A quick introduction to natural language processing in Python
## Jeremy R. Manning
PSYC 132: Introduction to Programming for Psychological Scientists

---

![bg opacity:0.1](https://uploads-ssl.webflow.com/614c82ed388d53640613982e/635bcc3c2b1b16702f8917c9_634fd7afbe19224c4a7a4a0e_6320786b1cfec14310b5f181_natural-language-processing--NLP-.png)

# What is natural language processing?

- Branch of computational linguistics
- Use computational approaches to process, analyze, and understand language

---

# Early tasks

![width:1000px](https://byteiota.com/wp-content/uploads/2021/01/POS-Tagging-800x400.jpg)

---

# Early tasks

![width:1000px](https://wisdomml.in/wp-content/uploads/2022/08/stem_feats.jpg)

---

# Early tasks: automatic summarization

![width:1000px](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/180981i9EA877DDFF97D50D/image-size/large?v=v2&px=999)

---

# But how can we get at the *meaning* of natural language?

---

# Text embedding models

- Preprocess some text to make a "training corpus"
- Train a model to parse the documents in the corpus
- Goal: generate "feature vectors" (for words, phrases, documents, etc.) that capture semantic properties of the text

---

# Latent semantic analysis

![width:800px](https://i.ytimg.com/vi/M1duqgg8-IM/maxresdefault.jpg)

---

# Latent Dirichlet Allocation (LDA)

![width:600px](https://community.alteryx.com/t5/image/serverpage/image-id/124666i826A507A4B5E3107?v=v2)

---

# Word2vec

![width:1000px](https://miro.medium.com/v2/resize:fit:678/1*5F4TXdFYwqi-BWTToQPIfg.jpeg)

---

# Consider the following phrases:
- My dog ate my homework

- My homework ate my dog

---

### Bag of words vs. context-sensitive models

- BoW models (e.g., LSA, LDA, word2vec) don't care about word order
- C-S models "care" about *context* and *grammar* by picking up on word order effects

---

# Universal Sentence Encoder

![width:1000px](https://learnopencv.com/wp-content/uploads/2018/11/Universal-Sentence-Encoder.png)

---

# Transformers

![width:850px](https://miro.medium.com/v2/resize:fit:1400/1*iy12bH-FiUNOy9-0bULgSg.png)

---

# Transfomers

1. Tokenize text into smaller units (words/sub-words)
2. Embed tokens (ignoring order)
3. Update the embeddings to include position information (add features)
4. Update the embneddings using the encoder and decoder layers:
  a. The encoder processes the inputs
  b. The decoder generates outputs

---

# Transformers

- Initially used for "sequence-to-sequence" tasks (e.g., translation)
- Now the basis of most state-of-the-art NLP models

---

# Generative Pretrained Transformer (GPT)

- Variant of transformers
- "Regular" transformers have both an encoder and decoder; GPT only has the decoder part
- The goal is to predict the next token in a sequence, given the previous context
- The model is "pre-trained" on a large corpus of text to learn which tokens are likely to follow which other tokens
- The model can then be "fine-tuned" on specific tasks
- Goal: text completion, translation, summarization, etc.

---

# NLP in practice

- Natural Language Toolkit (NLTK) implements lots of basic text processing tasks like tokenization, lemmatization, part of speech tagging, etc.
- Scikit-learn has some basic models, like LDA
- For fancier models the best place to look is Hugging Face

---

# NLTK

Implements lots of fundemantal "traditional" computational linguistics tasks
```python
import nltk

sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)

tagged = nltk.pos_tag(tokens)
```


---

### Hugging Face

![width:1000px](https://huggingface.co/front/assets/activity-feed.png)

---

# `transformers` library (by Hugging Face)

Direct interactions with text and models

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForMaskedLM.from_pretrained("bert-base-uncased")
```

---

# `pydata-wrangler` library

Wrapper for `scikit-learn` and Hugging Face models, focused on computing text embeddings

```python
import datawrangler as dw

bert = {'model': 'TransformerDocumentEmbeddings',
        'args': ['bert-base-uncased'],
        'kwargs': {}}
bert_embeddings = dw.wrangle(my_text,
                             text_kwargs={'model': bert})
```

---

# What's next?

The best way to learn is to *do*: pick a task and have fun with it!