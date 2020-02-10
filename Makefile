install:
	poetry install

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	 poetry publish -r pypi-test