# Book Scraping and Clustering
Case Study for Patika Global Technology

* **Author:** Bora Boyacıoğlu
* **GitHub:** https://github.com/boraboyacioglu-itu
* **E-Mail:** boraboyacioglu@icloud.com

## Contents

The repository consists of two main Jupyter Notebooks and a Python script:

1. **```main.ipynb```:** To run the entire program. Includes a mirror of book scraping, the main model, as well as the alternative one. Some analyses like book counts, names, or averages are also found.
2. **```demos.ipynb```:** Consists of four models, based on NLP or embeddings, have been tried on this notebook. Each method try also explains the results, and evaluates them.
3. **```get_books.py```:** To parse all the books in the give webpage.

## How to Run?

Before running anything, make sure to have installed the required libraries. This can be done by running the script: ```python3 -m pip install -r requirements.txt``` on the main directory. The main libraries are noted as:

* AnsiLib
* bs4
* hdbscan
* numpy
* requests
* scikit-learn
* sentence_transformers
* urllib

First of all, to parse all the info from all of the books available on the website, run: ```python3 get_books.py```. This saves the results in ```books.json```, which is already included in this repository.

Later, all the tried models can be found in the Jupyter Notebook ```demos.ipynb```.

But the main process (including parsing) happens by directly running ```main.ipynb```.

## Sample Results

### Sentence Embeddings & K-Means Clustering

#### Cluster 48:
1. when love and jealousy collide on the slopes, winter break turns deadly...
2. in a kingdom by the seain a secret world where halfangel warriors ...
3. pestered by her close new jersey family, stephanie plum offers to catch...
4. the 1 new york times bestselling author of the sea haven novels...
5. yuki cross has no memory of her past prior to the moment...

### HDBSCAN

#### Cluster 12:
1. the zombie apocalypse has never been more surreal! a mentally unhinged manga...
2. the zombie war came unthinkably close to eradicating humanity. max brooks, driven...
3. diary of a minecraft zombie has a fresh new look! ever wonder...