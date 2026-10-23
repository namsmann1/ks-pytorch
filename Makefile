.PHONY: deps kontroller kjor-losninger

deps:
	uv sync --locked --all-extras

kontroller:
	uv run python scripts/kontroller_notatboker.py

kjor-losninger:
	uv run python scripts/kontroller_notatboker.py --kjor
