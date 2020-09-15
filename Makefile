format:
		black .
		isort .

lint:
		env PYTHONPATH=. pytest --pylint --mypy --flake8 --ignore tests

test:
		env PYTHONPATH=. pytest tests --cov=src --cov-report term-missing --cov-report html

install:
		conda env create --file ./environment.yml
