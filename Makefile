setup: Pipfile
	pipenv install

process: process_data.py
	pipenv run python process_data.py

train: train_classifier.py
	pipenv run python train_classifier.py

api: run.py
	pipenv run python run.py

web:
	cd frontend
	npm run start --prefix ./frontend
