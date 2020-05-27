.SILENT:
.DEFAULT_GOAL := help

PROJECT := linkcentralizer

## Run aplication localy
run:
	docker-compose up

## Restart thenapplication
restart:
	docker-compose restart

## Build aplication compose
build:
	docker-compose build

## Execute application tests
tests:
	echo Test!

## Print help message
help:
	echo HELP! I need somebody HELP!
