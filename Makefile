.PHONY: deps

deps:
	uv sync --locked --all-extras
