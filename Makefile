.PHONY: build deploy

build:
	python setup.py sdist bdist_wheel

deploy:build
	twine upload --skip-existing dist/*
