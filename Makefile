.DEFAULT_GOAL := help

H ?= 127.0.0.1
P ?= 8080

help:
	@echo "Commands:"
	@echo "\tmake help"
	@echo "\tmake run H=... P=..."
	@echo "\tmake i L=..."
	@echo "\tmake ui L=..."

run:
	@echo "Server started"
	PYTHONPATH=src uvicorn src.main:app --reload --host ${H} --port ${P}

i:
	@echo "Install package ${L}"
	poetry add ${L}

ui:
	@echo "Uninstall package ${L}"
	poetry remove ${L}