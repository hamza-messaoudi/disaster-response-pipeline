# disaster-response-pipeline
This project is a part of the [Udacity Data Science Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025), the used dataset was provided by [Figure Eight](https://www.figure-eight.com/) (acquired by Appen Ltd.).
## Motivation behind the project

> This is one of the most important problems that we're trying to solve in Data Science and Machine Learning right now.
> So following a disaster, typically you will get millions and millions of communications either direct or via social media right at the > time when disaster response organizations have the least capacity to filter and then pull out the messages which are the most 
> important.
> 
> Often it really is only one in every thousand messages that might be relevant to the disaster response professionals.
> So, the way that disasters are typically responded to, is that different organizations will take care of different parts of the
> problem.
> So one organization will care about water, another will care about blocked roads, another will care about medical supplies.
> So, when you look at the data, you'll see that these are the categories that we have pulled out for each of these datasets.
> So, we actually used Figure Eight for many of the disasters from which these messages are taken then combined these datasets and 
> relabeled them so that they're consistent labels across the different disasters, and this is to investigate the different trends that > we might be able to find and to build supervised Machine Learning models.
> 
> Machine Learning models that can help us respond to future disasters. One of my favorite parts about this project is how meaningful 
> the work is.
> Think about the benefits this solution brings to people affected by natural disasters around the world.
> - Robert Munro, CTO, Figure Eight


## About this app

A tidy example of a disaster response pipeline. Using a data set of real tweets, direct messages and news headlines. 
Below are a few screenshots of the web app.


![alt text](https://github.com/hamza-messaoudi/disaster-response-pipeline/blob/master/screenshots/disaster-response-project1.png "Dataset")

![alt text](https://github.com/hamza-messaoudi/disaster-response-pipeline/blob/master/screenshots/disaster-response-project2.png "Classifier")

---
## Components and Functionality

### 1. ETL Pipeline

A data cleaning pipeline in a Python script, process_data.py, that:

⋅⋅* Loads the messages and categories datasets
⋅⋅* Merges the two datasets
⋅⋅* Cleans the data
⋅⋅* Stores it in a SQLite database

```
- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to
```

### 2. ML Pipeline

A machine learning pipeline in a Python script, train_classifier.py, that:

⋅⋅* Loads data from the SQLite database
⋅⋅* Splits the dataset into training and test sets
⋅⋅* Builds a text processing and machine learning pipeline
⋅⋅* Trains and tunes a model using GridSearchCV
⋅⋅* Outputs results on the test set
⋅⋅* Exports the final model as a pickle file

```
- models
|- train_classifier.py
|- classifier.pkl  # saved model 
```
### 3. Flask Web App

We are providing much of the flask web app for you, but feel free to add extra features depending on your knowledge of flask, html, css and javascript. For this part, you'll need to:

Modify file paths for database and model as needed
Add data visualizations using Plotly in the web app. One example is provided for you
```
- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

```

---
## How to run this app

To run this app first clone repository and then open a terminal to the app folder.

```
git clone https://github.com/hamza-messaoudi/disaster-response-pipeline.git

```

Install the requirements:

```
pip install -r requirements.txt
```
Run the app:

```
python run.py
```
You can run the app on your browser at [http://0.0.0.0:3001/](http://0.0.0.0:3001/)

---
## Resources

This project is a part of the [Udacity Data Science Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025).
The used dataset was provided by [Figure Eight](https://www.figure-eight.com/) (acquired by Appen Ltd.).
