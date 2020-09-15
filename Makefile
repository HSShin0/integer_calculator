format:
		black .
		isort .

test:
		flake8 .
		mypy .
		pylint *.py

install:
		conda env create --file ./environment.yml
