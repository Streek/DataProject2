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

Here's a break down of the file tree.

```
📦data-science-proj2
 ┣ 📂data #storage for datafiles
 ┃ ┣ 📜categories.csv
 ┃ ┗ 📜messages.csv
 ┣ 📂frontend #the front-end react app
 ┃ ┣ 📂public #public files
 ┃ ┃ ┣ 📂plots #the plot images
 ┃ ┃ ┃ ┣ 📜aid_centers.png
 ┃ ┃ ┃ ┣ 📜aid_centers_cv.png
 ┃ ┃ ┃ ┣ 📜aid_related.png
 ┃ ┃ ┃ ┣ 📜aid_related_cv.png
 ┃ ┃ ┃ ┣ 📜buildings.png
 ┃ ┃ ┃ ┣ 📜buildings_cv.png
 ┃ ┃ ┃ ┣ 📜child_alone.png
 ┃ ┃ ┃ ┣ 📜child_alone_cv.png
 ┃ ┃ ┃ ┣ 📜clothing.png
 ┃ ┃ ┃ ┣ 📜clothing_cv.png
 ┃ ┃ ┃ ┣ 📜cold.png
 ┃ ┃ ┃ ┣ 📜cold_cv.png
 ┃ ┃ ┃ ┣ 📜death.png
 ┃ ┃ ┃ ┣ 📜death_cv.png
 ┃ ┃ ┃ ┣ 📜direct_report.png
 ┃ ┃ ┃ ┣ 📜direct_report_cv.png
 ┃ ┃ ┃ ┣ 📜earthquake.png
 ┃ ┃ ┃ ┣ 📜earthquake_cv.png
 ┃ ┃ ┃ ┣ 📜electricity.png
 ┃ ┃ ┃ ┣ 📜electricity_cv.png
 ┃ ┃ ┃ ┣ 📜fire.png
 ┃ ┃ ┃ ┣ 📜fire_cv.png
 ┃ ┃ ┃ ┣ 📜floods.png
 ┃ ┃ ┃ ┣ 📜floods_cv.png
 ┃ ┃ ┃ ┣ 📜food.png
 ┃ ┃ ┃ ┣ 📜food_cv.png
 ┃ ┃ ┃ ┣ 📜hospitals.png
 ┃ ┃ ┃ ┣ 📜hospitals_cv.png
 ┃ ┃ ┃ ┣ 📜infrastructure_related.png
 ┃ ┃ ┃ ┣ 📜infrastructure_related_cv.png
 ┃ ┃ ┃ ┣ 📜medical_help.png
 ┃ ┃ ┃ ┣ 📜medical_help_cv.png
 ┃ ┃ ┃ ┣ 📜medical_products.png
 ┃ ┃ ┃ ┣ 📜medical_products_cv.png
 ┃ ┃ ┃ ┣ 📜military.png
 ┃ ┃ ┃ ┣ 📜military_cv.png
 ┃ ┃ ┃ ┣ 📜missing_people.png
 ┃ ┃ ┃ ┣ 📜missing_people_cv.png
 ┃ ┃ ┃ ┣ 📜money.png
 ┃ ┃ ┃ ┣ 📜money_cv.png
 ┃ ┃ ┃ ┣ 📜offer.png
 ┃ ┃ ┃ ┣ 📜offer_cv.png
 ┃ ┃ ┃ ┣ 📜other_aid.png
 ┃ ┃ ┃ ┣ 📜other_aid_cv.png
 ┃ ┃ ┃ ┣ 📜other_infrastructure.png
 ┃ ┃ ┃ ┣ 📜other_infrastructure_cv.png
 ┃ ┃ ┃ ┣ 📜other_weather.png
 ┃ ┃ ┃ ┣ 📜other_weather_cv.png
 ┃ ┃ ┃ ┣ 📜refugees.png
 ┃ ┃ ┃ ┣ 📜refugees_cv.png
 ┃ ┃ ┃ ┣ 📜related.png
 ┃ ┃ ┃ ┣ 📜related_cv.png
 ┃ ┃ ┃ ┣ 📜request.png
 ┃ ┃ ┃ ┣ 📜request_cv.png
 ┃ ┃ ┃ ┣ 📜search_and_rescue.png
 ┃ ┃ ┃ ┣ 📜search_and_rescue_cv.png
 ┃ ┃ ┃ ┣ 📜security.png
 ┃ ┃ ┃ ┣ 📜security_cv.png
 ┃ ┃ ┃ ┣ 📜shelter.png
 ┃ ┃ ┃ ┣ 📜shelter_cv.png
 ┃ ┃ ┃ ┣ 📜shops.png
 ┃ ┃ ┃ ┣ 📜shops_cv.png
 ┃ ┃ ┃ ┣ 📜storm.png
 ┃ ┃ ┃ ┣ 📜storm_cv.png
 ┃ ┃ ┃ ┣ 📜tools.png
 ┃ ┃ ┃ ┣ 📜tools_cv.png
 ┃ ┃ ┃ ┣ 📜transport.png
 ┃ ┃ ┃ ┣ 📜transport_cv.png
 ┃ ┃ ┃ ┣ 📜water.png
 ┃ ┃ ┃ ┣ 📜water_cv.png
 ┃ ┃ ┃ ┣ 📜weather_related.png
 ┃ ┃ ┃ ┗ 📜weather_related_cv.png
 ┃ ┃ ┣ 📜favicon.ico
 ┃ ┃ ┣ 📜index.html #default html incase react doesnt load
 ┃ ┃ ┣ 📜logo192.png
 ┃ ┃ ┣ 📜logo512.png
 ┃ ┃ ┣ 📜manifest.json
 ┃ ┃ ┗ 📜robots.txt #for search engines
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📜App.css #css file, uses tailwind
 ┃ ┃ ┣ 📜App.js #main app
 ┃ ┃ ┣ 📜App.test.js #testing framework
 ┃ ┃ ┣ 📜index.css #default file
 ┃ ┃ ┣ 📜index.js #default js file
 ┃ ┃ ┣ 📜logo.svg #the logo
 ┃ ┃ ┣ 📜reportWebVitals.js #heartbeat type info
 ┃ ┃ ┣ 📜setupTests.js #run tests
 ┃ ┃ ┗ 📜table.js #the table component
 ┃ ┣ 📜.gitignore #the gitignore file
 ┃ ┣ 📜package-lock.json #the lock file for packages
 ┃ ┣ 📜package.json #the raw package
 ┃ ┣ 📜postcss.config.js #postcss config
 ┃ ┗ 📜tailwind.config.js #tailwinds config file
 ┣ 📂pickles
 ┃ ┗ 📜.keep #no pickles are included due to size
 ┣ 📜.gitignore
 ┣ 📜Makefile #shortcuts
 ┣ 📜Pipfile #the list of packages for python
 ┣ 📜Pipfile.lock #the auth list of packages
 ┣ 📜Procfile #for remote server deployment
 ┣ 📜development.db #the database
 ┣ 📜nltk.txt #the nltk packages to download
 ┣ 📜process_data.py #process data here
 ┣ 📜readme.md #readme markdown for github
 ┣ 📜run.py #run the api
 ┗ 📜train_classifier.py #train the classifier
```

## The Data

The data is split between two files one being and ID and message, the other being an ID and 36 categories. I have to ingest the files, split the categories, create a data frame of the merged data, and then save that data to a SQLite database for use by the ML script. The data is useful but incomplete, some categories have really bad numbers for training and other categories are simply unreliable.

Spending time on and doing additional work on the tokenizer more or working with another single to multi-out algorithm may result in better results. This is especially true if we start to ignore the useless or unreliable data. In a perfect world I would have much more data to work off of. More data, especially with categories that are underrepresented would make the results far better.

F1 scoring is all over due to the imbalanced data, recall on some categories is great, others require specific wording to get a category to flip. My focus was on the process, data, code, etc. not on the outcome of the algorithm. I believe this could be greatly improved at some point.

## Screenshots of the App

<img width="1515" alt="image" src="https://user-images.githubusercontent.com/55346/168404777-9a701805-09da-4ed6-9b62-46b5164d0fab.png">
<img width="1516" alt="image" src="https://user-images.githubusercontent.com/55346/168404787-555bc5b8-930c-4979-9a99-965447fc9ff0.png">
<img width="699" alt="image" src="https://user-images.githubusercontent.com/55346/168404802-344fedb2-a51a-406e-bc6a-f8801ed12ba0.png">

## Running the Code

The app needs the following steps done to work properly. You will need Python3 and Node > 10 to run this code.

1. Process the raw data using `pipenv run python process_data.py` file directly or by calling `make process`.
2. Train the ML algorithm by running the `pipenv run python train_classifier.py` file directly or by calling `make train`.
3. Run the API backend using the `pipenv run python run.py` file directly or by calling `make api`.
4. While the API is running, `CD into the ./frontend` folder and run `npm run start` file directly or by calling `make web` from the root.

Convenience Methods have been provided using a `Makefile`
| Command | Action |
|--|--|
| make setup | Installs Pipfile, package.json and setups up env for python and node. |
| make process | Runs the process_data.py script in the pipenv. |
| make train | Runs the train_classifier.py script in the pipenv. |
| make api | Runs the API backend via run.py. |
| make web | This will cd into frontend and start the react client. |

If you run the commands in the order above, you should have a fully functional Web front-end and trained ML classifier available at [http://localhost:3000](http://localhost:3000)
