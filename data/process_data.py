import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    #import and merge dataset
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories,on = 'id')
    
    return df


def clean_data(df):
    #manually get dummy variables for categories
    
    #1.Split categories into separate category columns
    categories = df['categories'].str.split(pat = ';' , expand = True)
    row =  categories.iloc[1] 
    category_colnames = row.apply(lambda x: x[:-2])
    categories.columns = category_colnames
    
    #2.Convert category values to just numbers 0 or 1
    for column in categories:
        categories[column] = categories[column].astype(str).str[-1:].astype(int)
        
    
    #3.Replace categories column in df with new category columns
    df = df.drop(columns = 'categories')
    df = pd.concat([df,categories], axis = 1 )
    
    #remove duplicates
    df = df.drop_duplicates('message')
    
    return df


def save_data(df, database_filename):
    
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('disaster_response', engine, index=False)
    pass  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()