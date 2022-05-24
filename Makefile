setup: Pipfile
	pipenv install
	npm install --prefix ./frontend

process: process_data.py
	pipenv run python process_data.py data/messages.csv data/categories.csv database.db

train: train_classifier.py
	pipenv run python train_classifier.py database.db

api: run.py
	pipenv run python run.py

web:
	npm run start --prefix ./frontend
