# Problem Statement

Given a body of english language text, determine the estimated time required to read it.

# Assumption

Since most of the article time prediction involves static time calculation using [Word per minute](https://www.wikiwand.com/en/Words_per_minute)
collecting data was a challenge by itself. So we have used a dynamic dataset which involves synopsis of books of several genre with reading time
specific to individual. This dataset can be a biased as it is a personalised effort. On an average the estimated word count per minute is 190.
In general while calculating static reading time, people use 275 WPM to 220 WPM.

# Algorithms

We have considered two algorithms linear regression and random forest regression, though r2-score of random forest regression was high, it seemed to overfit, hence we have taken linear regression in account to predict time taken to read a particular text.

# Further scope

We can also work on more feature extraction such as :
    1. Topic type using text classification
    2. Number of punctuation
    3. Complexity of sentence
    4. Effect of word predictability of sentence in reading time is logarithmic.[source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3709001/)

# Prerequisites

```sh
>  pip install -r requirements.txt --no-index --find-links file:///tmp/packages
```

# Usage

``` sh
> cd src
> python app.py
```
