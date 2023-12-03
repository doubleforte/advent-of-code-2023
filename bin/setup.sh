#!/bin/sh

pipenv sync --dev
pipenv run pre-commit install

mkdir -p ./data/day01/example-input
