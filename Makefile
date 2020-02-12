publish:
	 poetry publish -r pypi-test

install:
	poetry install

test:
	poetry run pytest brain_games tests

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

.PHONY: install lint selfcheck check build