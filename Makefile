install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=sicp --cov-report xml

lint:
	poetry run flake8 sicp

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

isort:
	poetry run isort sicp

.PHONY: install test lint selfcheck check build