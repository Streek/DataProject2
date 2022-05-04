setup: Pipfile
	pipenv install
	npm install --prefix ./frontend

process: process_data.py
	pipenv run python process_data.py

train: train_classifier.py
	pipenv run python train_classifier.py

api: run.py
	pipenv run python run.py

web:
	npm run start --prefix ./frontend
