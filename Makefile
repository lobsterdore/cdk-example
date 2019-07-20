.DEFAULT_GOAL := help

VENV_DIR:=.venv
PATH:=${PWD}/${VENV_DIR}/bin:$(shell printenv PATH)
PYTHONEXE=$(shell which python3)
export PATH
SHELL:=env PATH=$(PATH) /bin/bash

.PHONY: clean
## Remove All virtualenvs
clean:
	@rm -rf
	@rm -rf ${PWD}/${VENV_DIR} build dist *.egg-info .eggs .pytest_cache .coverage
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

## Install deps
deps: deps_python deps_docker

deps_docker:
	cd docker/cdk && docker build . -t cdk-example

deps_python:
	test -d ${PWD}/${VENV_DIR} || \
		python3 -m venv --copies .venv
	python -m pip install -r requirements.txt

help:
	@awk -v skip=1 \
		'/^##/ { sub(/^[#[:blank:]]*/, "", $$0); doc_h=$$0; doc=""; skip=0; next } \
		 skip  { next } \
		 /^#/  { doc=doc "\n" substr($$0, 2); next } \
		 /:/   { sub(/:.*/, "", $$0); \
		 printf "\033[34m%-30s\033[0m\033[1m%s\033[0m %s\n\n", $$0, doc_h, doc; skip=1 }' \
		${MAKEFILE_LIST}
