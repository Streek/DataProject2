# Emergency Messages Classifier

## Abstract

This project is a very simple machine learning classifier using TF-IDF and a few other components to classify text messages that were sent during emergency situations. These situations could be fires, floods, etc. I am attempting to classify the text messages based on 36 unique criteria.

Once classified I have a web app that you can use to write a unique message which is then processed by the same classifier. This will produce a result which will show boolean values for each category.

## Files

In the code base you'll see a few python files, a frontend folder, data folder, and pickles folder.

- The python files are used to store (in a database), train, process, and host the api for the web front-end
- The frontend folder is a node project which has a react frontend that simply interacts with the python API.
- The data folder holds the messages.csv and categories.csv files which hold the raw data we use to process these messages.
- The pickles folder holds the pickle binaries for the algorithms saved, for use with the API.

## The Data

The data is split between two files one being and ID and message, the other being an ID and 36 categories. I have to ingest the files, split the categories, create a data frame of the merged data, and then save that data to a SQLite database for use by the ML script. The data is useful but incomplete, some categories have really bad numbers for training and other categories are simply unreliable.

Spending time on and doing additional work on the tokenizer more or working with another single to multi-out algorithm may result in better results. This is especially true if we start to ignore the useless or unreliable data. In a perfect world I would have much more data to work off of. More data, especially with categories that are underrepresented would make the results far better.

F1 scoring is all over due to the imbalanced data, recall on some categories is great, others require specific wording to get a category to flip. My focus was on the process, data, code, etc. not on the outcome of the algorithm. I believe this could be greatly improved at some point.

## Screenshots of the App

<img width="1515" alt="image" src="https://user-images.githubusercontent.com/55346/168404777-9a701805-09da-4ed6-9b62-46b5164d0fab.png">
<img width="1516" alt="image" src="https://user-images.githubusercontent.com/55346/168404787-555bc5b8-930c-4979-9a99-965447fc9ff0.png">
<img width="699" alt="image" src="https://user-images.githubusercontent.com/55346/168404802-344fedb2-a51a-406e-bc6a-f8801ed12ba0.png">

## Visualization

Info about the viz

## Running the Code

The app needs the following steps done to work properly. You will need Python3 and Node > 10 to run this code.

1. Process the raw data using the `process_data.py` file.
2. Train the ML algorithm by running the `train_classifier.py` file.
3. Run the API backend using the `run.py` file.
4. While the API is running, `CD into the frontend` folder and run `npm run start`

Convenience Methods have been provided using a `Makefile`
| Command | Action |
|--|--|
| make setup | Installs Pipfile, package.json and setups up env for python and node. |
| make process | Runs the process_data.py script in the pipenv. |
| make train | Runs the train_classifier.py script in the pipenv. |
| make api | Runs the API backend via run.py. |
| make web | This will cd into frontend and start the react client. |

If you run the commands in the order above, you should have a fully functional Web front-end and trained ML classifier available at [http://localhost:3000](http://localhost:3000)
