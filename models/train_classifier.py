import sys
import pickle
import re
import pandas as pd
import numpy as np
from sqlalchemy import create_engine 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import classification_report
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import nltk
nltk.download(['punkt', 'wordnet'])
url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

def load_data(database_filepath):
# load data from database

    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql("SELECT * FROM disaster_response", engine)
    X = df.message.values
    Y = df[df.columns[4:]].drop(columns = 'child_alone').values #child_alone column dosen't contain information
    categories = (df[df.columns[4:]].drop(columns = 'child_alone')).columns 
    
    return X,Y,categories

def tokenize(text):    
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    pipeline = Pipeline([('vect', CountVectorizer(tokenizer=tokenize)), 
                                ('tfidf', TfidfTransformer()), 
                                ('clf', MultiOutputClassifier(KNeighborsClassifier()))])
    return pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    pass


def save_model(model, model_filepath):
    pickle.dump(model, open('{}'.format(model_filepath), 'wb'))
    pass


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()