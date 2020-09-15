format:
		black .
		isort .

test:
		pytest --pylint --mypy --flake8

install:
		conda env create --file ./environment.yml
