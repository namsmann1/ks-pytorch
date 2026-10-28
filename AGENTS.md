# Repository Guidelines

## Project Structure & Module Organization

This repository contains a Norwegian PyTorch crash course for beginners.

- `oppgaver/`: six numbered student notebooks, from tensor basics to Fashion-MNIST classification and an open bonus project.
- `solutions/`: matching notebooks with solution code and written answers; filenames must match `oppgaver/`.
- `src/pytorch_101/utils/`: shared Fashion-MNIST loading and random-seed helpers.
- `scripts/kontroller_notatboker.py`: notebook validation and execution.
- `README.md`: setup and course sequence.
- `data/` and `outputs/`: ignored datasets and executed notebooks. `.devcontainer/` provides the development environment.

## Build, Test, and Development Commands

Use Python 3.12 and run commands from the repository root:

```bash
make deps              # Install locked dependencies and the local package with uv
uv run jupyter lab     # Open the notebooks locally
make kontroller        # Validate notebook structure, syntax, and solution parity
make kjor-losninger    # Execute all solutions in fresh kernels
```

Solution execution downloads Fashion-MNIST if necessary and writes results to `outputs/solutions/`.

## Coding Style & Naming Conventions

Use four-space indentation and descriptive `snake_case` names in Python. Use English names for variables, functions, parameters, and result dictionary keys. Keep instructional text, comments, and printed messages in Norwegian; use the same English identifiers in Markdown code references. Preserve numbered filenames such as `01_tensorer.ipynb`.

## Testing Guidelines

There is no standalone test suite or coverage threshold. Use the notebook checker and full solution execution for course changes.

Update student and solution notebooks together. Preserve corresponding cell IDs, metadata, and shared content. Student code cells marked `kursrolle: oppgave` contain comments only; solutions contain executable code. Written answer cells use `kursrolle: svar` and begin with `**Mitt svar:**`.

Keep committed notebooks free of outputs and execution counts. Inspect changed figures and check that optional exercises are not prerequisites for required tasks.

## Commit & Pull Request Guidelines

Existing commit subjects are short, informal action phrases such as `add tasks v1`; no formal convention is established. Write concise, descriptive subjects identifying the change.
