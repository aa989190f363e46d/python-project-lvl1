publish:
	 poetry publish -r pypi-test

install:
	@poetry install

test:
	poetry run pytest hexlet_python_package tests

lint:
	poetry run flake8 hexlet_python_package

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install lint selfcheck check build