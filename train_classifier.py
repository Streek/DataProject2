# import libraries
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

import pandas as pd  # for the dataframes

import pickle

from sqlalchemy import create_engine

# download needed libraries
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


class TrainClassifier():
    def load_data(self):
        '''
        This function loads data from the database and returns our feature and target data
        '''
        engine = create_engine('sqlite:///development.db')
        df = pd.read_sql_table('cleaned_data', engine)

        # Define feature and target variables X and Y
        X = df['message']
        Y = df.iloc[:, 4:]

        return X, Y

    def tokenizer(self, text):
        '''
        This function tokenizes the text
        '''
        tokens = word_tokenize(text)
        lemmatizer = WordNetLemmatizer()

        clean_tokens = []
        for tok in tokens:
            clean_tok = lemmatizer.lemmatize(tok).lower().strip()
            clean_tokens.append(clean_tok)

        return clean_tokens

    def build_pipeline(self):
        '''
        This function builds the pipeline
        '''
        pipeline = Pipeline([
            ('vect', CountVectorizer(tokenizer=self.tokenizer)),
            ('tfidf', TfidfTransformer()),
            ('clf', MultiOutputClassifier(
                RandomForestClassifier(n_jobs=-1, random_state=42)))
        ])

        return pipeline

    def train_pipeline(self, pipeline, X, Y):
        '''
        This function trains the pipeline
        '''
        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, random_state=42, test_size=0.45)

        pipeline.fit(X_train, Y_train)

        return X_train, X_test, Y_train, Y_test

    def test_pipeline(self, pipeline, X_test, Y_test, Y_train):
        '''
        This function tests the pipeline
        '''
        y_pred = pipeline.predict(X_test)

        for column in Y_test.columns:
            print(column)
            # get all data for the column in y_pref
            y_pred_column = y_pred[:, Y_train.columns.get_loc(column)]

            print(classification_report(
                Y_test[column], y_pred_column, digits=1, zero_division=0))

        print(y_pred.shape)

        return y_pred

    def save_model(self, name, pipeline, clean=True):
        '''
        This function saves the model
        '''
        # remove stop_words_ on pipeline

        if clean:
            pipeline.named_steps['vect'].stop_words_ = None
            pipeline.named_steps['tfidf'].stop_words_ = None
            pipeline.named_steps['clf'].stop_words_ = None
            pipeline.named_steps['clf'].estimator.stop_words_ = None
        pickle.dump(pipeline, open('./pickles/'+name+'.pkl', 'wb'), protocol=2)

    def train_grid_search(self, pipeline, X_train, Y_train):
        '''
        This function trains the grid search
        '''
        parameters = {
            'clf__estimator__n_estimators': [50, 100, 200],
            'clf__estimator__min_samples_split': [2, 3, 4]
        }

        cv = GridSearchCV(pipeline, param_grid=parameters, n_jobs=-1)
        cv.fit(X_train, Y_train)

        breakpoint()
        return cv.best_estimator_

    def test_grid_search(self, cv, X_test, Y_test):
        '''
        This function tests the grid search
        '''
        y_pred = cv.predict(X_test)

        for column in Y_test.columns:
            print(column)
            # get all data for the column in y_pref
            y_pred_column = y_pred[:, Y_train.columns.get_loc(column)]

            print(classification_report(
                Y_test[column], y_pred_column, digits=1, zero_division=0))

        print(y_pred.shape)

        return y_pred


if __name__ == '__main__':
    print('===============\nTrain and Test Model Process...\n===============')
    # build the class and run the functions
    train_classifier = TrainClassifier()
    X, Y = train_classifier.load_data()
    pipeline = train_classifier.build_pipeline()
    print('===\nTraining  Model...\n===')
    X_train, X_test, Y_train, Y_test = train_classifier.train_pipeline(
        pipeline, X, Y)
    print('===\nTesting Model...\n===')
    train_classifier.test_pipeline(pipeline, X_test, Y_test, Y_train)
    train_classifier.save_model("pipeline", pipeline)
    print('===\nTraining GridSearch Model...\n===')
    cv = train_classifier.train_grid_search(pipeline, X_train, Y_train)
    print('===\nTesting GridSearch Model...\n===')
    train_classifier.test_grid_search(cv, X_test, Y_test)
    train_classifier.save_model("cv", cv, False)
    print('===============\n COMPLETE\n===============')
