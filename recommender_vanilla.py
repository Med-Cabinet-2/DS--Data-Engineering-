import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer


### Import and shape data
path_base = 'gitstuff/buildweek2/DS--Data-Engineering-/'
df = pd.read_csv(path_base + 'data/cannabis.csv')

## select subset with high rating
good_enough = df[df['Rating'] >= 4.0]

## replace blank flavor with ""
good_enough = df.replace(np.nan, '', regex=True)

def clean_string(strng):
    """Remove commas and parentheses."""
    s = strng.replace(","," ") # comma-> space
    s = s.replace("("," ") # (-> space
    s = s.replace(")"," ") # (-> space
    s = s.lower()
    return s


## Clean and concatenate som fields to build strings for creating an embedding.
cols = ['Type', 'Effects', 'Flavor', 'Description']
for col in cols:
    good_enough[col] = good_enough[col].apply(clean_string)
good_enough['text'] = good_enough['Type'] + " " + good_enough['Effects'] + " " + good_enough['Flavor']

## Define a function to create a list of docs to be used to create a sparse matrix.
def gather_docs(df):
    """ Produces List of Documents from a dataframe.
    df: a Pandas dataframe that has the column 'text'.
    Returns a list of strings. 
    """
    docs = list(df['text'])
    return docs

docs = gather_docs(good_enough)


## Instantiate vectorizer
vect = CountVectorizer(stop_words='english', max_features=1000)

## Fit Vectorizer
vect.fit(docs)

## Create a sparse document-term matrix
dtm = vect.transform(docs)

## Make a dataframe of a condensed version of the DTM, using feature names
dtm = pd.DataFrame(dtm.todense(), columns=vect.get_feature_names())

## Instantiate Nearestneighbors
nn = NearestNeighbors(n_neighbors=5, algorithm='kd_tree')

## Fit on Document-Term Matrix
nn.fit(dtm)


def recommend(txt):
    """ Receives a string containing strain, effects, and flavors, and 
    returns a 2-tuple of (array of scores, array of indexes) describing
    the best matches among strains modeled."""
    
    clean_text = clean_string(txt)
    transformed_text = vect.transform([clean_text])
    return nn.kneighbors(transformed_text.todense())