# Table of contents
0. [Orientation](#orientation)
1. [Course setup and Python basics](#module-1-course-setup-and-python-basics)
2. [Beyond the basics](#module-2-beyond-the-basics)
3. [Find your inner hacker](#module-3-find-your-inner-hacker)
4. [External libraries](#module-4-external-libraries)
5. [Generating meaningful data](#module-5-generating-meaningful-data)
6. [Interrogating your data](#module-6-interrogating-your-data)
7. [Models](#module-7-models)
8. [Timeseries analysis](#module-8-timeseries-analysis)
9. [Natural language processing](#module-9-natural-language-processing)
10. [Advanced topics](#module-10-advanced-topics)

## Orientation

**Start here!**  The materials for each module below are organized sequentially.  Work your way from module to module (and from top to bottom within each module).  Take notes on questions, comments, concerns, etc. so that you can bring them up for discussion during our class meetings.  Several items are marked as optional; they may be skipped if desired, but they are included for students who wish to gain additional exposure to the material.

- [Welcome message](https://youtu.be/UjHUfUCpTQU)
- [Lecture 1 recording (W21)](https://youtu.be/XPsoY9R7dVs): orientation, overview, and "the sandwich exercise"
- [Fostering a programming mindset](https://github.com/ContextLab/cs-for-psych/blob/master/slides/module_0/programming_mindset.md)

## Module 1: Course setup and Python basics

- [Introduction and Overview](https://colab.research.google.com/github/ContextLab/cs-for-psych/blob/master/slides/module_1/introduction_and_overview.ipynb)
- [Introduction to Jupyter Notebooks and Python](https://colab.research.google.com/github/ContextLab/cs-for-psych/blob/master/slides/module_1/intro_to_python.ipynb)
- [Assignment 1: Hello, world!](https://github.com/ContextLab/psyc32-hello-world) [[Accept assignment](https://classroom.github.com/a/xjc-u-1F)]

## Module 2: Beyond the basics
- [Interactive programs](https://colab.research.google.com/github/ContextLab/cs-for-psych/blob/master/slides/module_2/interactive_programming.ipynb)
- [Control flow and order of operations](https://colab.research.google.com/github/ContextLab/cs-for-psych/blob/master/slides/module_2/control_flow_and_ooo.ipynb)
- [Dictionaries and classes](https://colab.research.google.com/github/ContextLab/cs-for-psych/blob/master/slides/module_2/dictionaries_and_classes.ipynb)
- [Variable scope and passing by value vs. reference](https://colab.research.google.com/github/ContextLab/cs-for-psych/blob/master/slides/module_2/scope_and_passing_by_value_vs_reference.ipynb)
- [Writing Pythonic code: list comprehensions, generators, and iterators](https://colab.research.google.com/github/ContextLab/cs-for-psych/blob/master/slides/module_2/pythonic_code.ipynb)
- [Assignment 2: Chess puzzle solver](https://github.com/ContextLab/psyc32-n-queens) [[Accept assignment](https://classroom.github.com/a/nHf5amef)]

## Module 3: Find your inner hacker
- Recursion (source: [Hany Farid's *Learn to Code in Python* course](https://farid.berkeley.edu/downloads/tutorials/learnPython/)):
  - [Factorial](https://drive.google.com/file/d/1n2vX-cH7JCAEX7AYCgVbBux6V-xJ52wd/view)
  - [List reversal](https://drive.google.com/file/d/1jBbKrTOn3KmipNOWWcmSv601hkJeTizp/view?usp=sharing)
  - [List sum](https://drive.google.com/file/d/1kFyKqe5OIiJZ6WWS_JypRF5xedcyijrp/view?usp=sharing) ([associated code](https://drive.google.com/file/d/1CCYpy7pThwP2FLGVBHdANEL1uF03Dnif/view?usp=sharing))
  - [Towers of Hanoi](https://drive.google.com/file/d/15SEWU23_iQD80Vs5vbkefdyiegnWoTyO/view?usp=sharing)
- Whirlwind tour of searching, sorting, and data structures (source: [Hany Farid's *Learn to Code in Python* course](https://farid.berkeley.edu/downloads/tutorials/learnPython/)):
  - [Linear and binary search](https://drive.google.com/file/d/1EukvYAyuyVnMJoYJGEO-qF7f2oy2jroX/view?usp=sharing)
  - Sorting (**optional**):
    - [Selection sort](https://drive.google.com/file/d/1LahEi_vWr1U7gWFNT4SwAh1tzAc8gXn-/view?usp=sharing)
    - [Insertion sort](https://drive.google.com/file/d/13BSt9rPYvd1txaXqgHPvM0-CA2tHqQEm/view?usp=sharing)
    - [Merge sort](https://drive.google.com/file/d/1nrzVsPfblxft36pc44M3TrVqDaHsnCd3/view?usp=sharing)
    - [Quick sort](https://drive.google.com/file/d/1NJWiskxYLYL6F4i_-wjDQU59vhdYzIT4/view?usp=sharing)
  - Data structures (**optional**):
    - [Linked lists](https://drive.google.com/file/d/1pdff_xyC8VSU_QX8_POLNlo88Wf317Sx/view?usp=sharing) (note: you may find it useful to view [this video](https://drive.google.com/file/d/1bGmFBsp7-kqSPcu1j2hXMM2GgZ7WiULE/view?usp=sharing) first)
    - [Doubly linked lists](https://drive.google.com/file/d/1WQ957ItVBXgUovedipVywUz8QNY1neLP/view?usp=sharing)
    - [Hashing](https://drive.google.com/file/d/1DYNmUGr2mnaoflaWAecdN0aYRl5HjBsd/view?usp=sharing) (note: you may find it useful to view [this video](https://drive.google.com/file/d/1yTw3wdLTHcsQkjnwwCb9FZp3PPf_xtZu/view?usp=sharing) first)
    - Graphs:
      - [Overview](https://drive.google.com/file/d/1Phf9dveviodykjUzwCzkR2nFMqyWqiwo/view?usp=sharing)
      - [Representing graphs](https://drive.google.com/file/d/1tRRVLJyeuemjMNMyS690lz4IPpYB-IWv/view?usp=sharing)
      - [Breadth-first search](https://drive.google.com/file/d/1tRRVLJyeuemjMNMyS690lz4IPpYB-IWv/view?usp=sharing)
    - [Queues and stacks](https://drive.google.com/file/d/13fnBkyRSHuTWwVkJuOZuXL072rrHl5tC/view?usp=sharing)
    - [Binary search trees](https://drive.google.com/file/d/1LuGuXDga4OtbHfdAvQSoBseQmCBYNMkh/view?usp=sharing)
- Lambda functions, and mapping
- Debugging
- Unit tests
- Optimization
- Writing maintainable and shareable code
- [Assignment 3: ELIZA](https://github.com/ContextLab/psyc32-eliza) [[Accept assignment](https://classroom.github.com/a/05_59FMz)]

## Module 4: External libraries
- [Modules and Packages](https://jakevdp.github.io/WhirlwindTourOfPython/13-modules-and-packages.html) (from [Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/index.html) by Jake VanderPlas)
- [Numpy](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html) and [Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.00-introduction-to-pandas.html) (from [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/index.html) by Jake VanderPlas)
- [Data visualization overview](https://github.com/ContextLab/cs-for-psych/blob/master/slides/module_4/data_visualization.ipynb)
- More details on plotting libraries: [Matplotlib](https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html) and [Seaborn](https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html) (from [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/index.html) by Jake VanderPlas)
- [Visualizing high-dimensional data with Hypertools](https://hypertools.readthedocs.io/en/latest/tutorials.html) (source: [hypertools.readthedocs.io](https://hypertools.readthedocs.io/))
- [Scikit-learn](https://jakevdp.github.io/PythonDataScienceHandbook/05.02-introducing-scikit-learn.html) (from [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/index.html) by Jake VanderPlas)
- A (shallow) introduction to deep learning with [Tensorflow](https://www.tensorflow.org/tutorials/quickstart/beginner) (source: [tensorflow.org](https://www.tensorflow.org/)) and [PyTorch](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) (Source: [pytorch.org](https://pytorch.org/))
- [PyTest](https://github.com/ContextLab/CDL-tutorials/tree/master/testing) (Source: [CDL tutorials](https://github.com/ContextLab/CDL-tutorials))
  - [More in-depth PyTest tutorial](https://www.youtube.com/watch?v=LX2ksGYXJ80) (source: [SciPy 2019 tutorials](https://www.youtube.com/redirect?v=LX2ksGYXJ80&redir_token=QUFFLUhqbFVjTkw0a3djNGx3SnlrdlRsOFVteDU0cmpYd3xBQ3Jtc0tsWkEyeXpHODd4SXJyRWpXUHlOcFhTSEVXUGt4SFpUUmpQOW5sT05GOGVxeTRaaUFQZi15OXFnV3ozTHh4ZWNoSHU5V0lkd0E0UUo2THZ5TnV3YVdvQWxlelVHZW1QYlFlN1JfbGFVZEJDRGdQX0N6MA%3D%3D&event=video_description&q=https%3A%2F%2Fwww.scipy2019.scipy.org%2Ftutorial-participant-instructions))
- Assignment 4: Web scraping and data wrangling

## Module 5: Generating meaningful data
- Experimental design
- **Optional:** [PsychoPy](https://www.psychopy.org/gettingStarted.html) (Source: [psychopy.org](https://www.psychopy.org/)) and [OpenSesame](https://osdoc.cogsci.nl/3.2/tutorials/beginner/) (Source: [osdoc.cogsci.nl](https://osdoc.cogsci.nl/))
- jsPsych
  - [Basics](https://www.jspsych.org/tutorials/hello-world/) (source: [jspsych.org](https://www.jspsych.org/))
  - [Simple reaction time task](https://www.jspsych.org/tutorials/rt-task/) (source: [jspsych.org](https://www.jspsych.org/))
  - [Sample experiments from Experiment Factory](https://expfactory.github.io/)
- Assignment 5: 50-participant challenge!

## Module 6: Interrogating your data
- Basic statistical tests
- Permutation tests and Monte Carlo simulation
- Regression
- Dimensionality reduction
- [Introduction to Quail](https://cdl-quail.readthedocs.io/en/latest/tutorial.html) (Source: [cdl-quail.readthedocs.io](https://cdl-quail.readthedocs.io/))
- Assignment 6: Report your experimental results

## Module 7: Models
- Building your first model
- Model fitting
- Evaluating and comparing models
- Example models: reinforcement learning, temporal context model
- Assignment 7: Model your data

## Module 8: Timeseries analysis
- Autocorrelation
- Frequency transforms
- [Dynamic correlations](https://timecorr.readthedocs.io/en/latest/tutorials.html) (Source: [timecorr.readthedocs.io](https://timecorr.readthedocs.io/))
- Assignment 8: Working with brain data

## Module 9: Natural language processing
- Tokenization, stemming, and lemmatization and parse trees
- Word embedding models
- Context-sensitive text models
- Assignment 9: Thought trajectories

## Module 10: Advanced topics
- Graphs and networks
- [High-order correlations with TimeCorr](https://timecorr.readthedocs.io/en/latest/tutorials.html) (Source: [timecorr.readthedocs.io](https://timecorr.readthedocs.io/))
- Prediction
- [Writing your own library](https://github.com/ContextLab/CDL-tutorials/blob/master/packages/README.md) (Source: [CDL-tutorials](https://github.com/ContextLab/CDL-tutorials))
- Assignment 10: Pip, pip, hooray!
