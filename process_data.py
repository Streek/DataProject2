# import libraries
import pandas as pd  # for the dataframes
from sqlalchemy import create_engine  # database


class ProcessData():
    def load_dataset(self):
        '''
        This function loads the CSV files into a dataframe
        '''
        # load the dataset from csv_files
        messages = pd.read_csv('data/messages.csv')
        categories = pd.read_csv('data/categories.csv')

        return messages, categories

    def merge_dataset(self, messages, categories):
        '''
        This function merges the two datasets into a dataframe
        '''
        # Merge the messages and categories datasets using the common id
        df = messages.merge(categories, on='id')

        # Assign this combined dataset to `df`, which will be cleaned in the following steps
        return df

    def build_categories(self, df):
        '''
        This function splits the categories column into 36 separate columns
        '''
        # Split the values in the `categories` column
        categories = df['categories'].str.split(';', expand=True)

        # Use the first row of categories dataframe to create column names for the categories data.
        row = categories.iloc[0]

        # Rename columns of `categories` with new column names.
        category_colnames = row.apply(lambda x: x[:-2])
        categories.columns = category_colnames

        # Iterate through the category columns in df to keep only the last character of each string
        for column in categories:
            # set each value to be the last character of the string
            categories[column] = categories[column].str[-1]

            # convert column from string to numeric
            categories[column] = categories[column].astype(int)

        # Drop the categories column from the df dataframe since it is no longer needed.
        df.drop('categories', axis=1, inplace=True)

        # Concatenate df and categories data frames
        df = pd.concat([df, categories], axis=1)

        return df

    def clean_data(self, df):
        '''
        This function cleans the dataframe
        '''
        # Check how many duplicates are in this dataset.
        df.duplicated().sum()

        # - Drop the duplicates.
        df.drop_duplicates(inplace=True)

        # - Confirm duplicates were removed.
        if df.duplicated().sum() > 0:
            raise ValueError('Duplicates still remain in the dataset.')

        return df

    def save_to_database(self, df):
        '''
        This function saves the dataframe to a database
        '''
        engine = create_engine('sqlite:///development.db')
        # delete database if it exists
        engine.execute('DROP TABLE IF EXISTS cleaned_data')
        df.to_sql('cleaned_data', engine, index=False)

    def get_list_of_categories(self, df):
        '''
        This function returns a list of all the categories
        '''
        # Get the list of all the categories
        categories = df.columns[4:]

        return categories


if __name__ == '__main__':
    print('===============\nProcessing data...\n===============')
    # build the class and run the functions
    process_data = ProcessData()
    messages, categories = process_data.load_dataset()
    df = process_data.merge_dataset(messages, categories)
    df = process_data.build_categories(df)
    df = process_data.clean_data(df)
    process_data.save_to_database(df)
    print('\n=====\nData has been cleaned and saved to the database.\n=====')
