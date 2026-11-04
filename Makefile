.PHONY: env format test clean verify-proofs

PYTHON = venv/bin/python
PIP = venv/bin/pip

env:
	@echo "Initializing localized studio environment..."
	python3 -m venv venv
	$(PIP) install --upgrade pip
	$(PIP) install -e .[dev]
	@echo "Environment ready. Run 'source venv/bin/activate'"

format:
	$(PYTHON) -m black src/ tests/

test:
	$(PYTHON) -m pytest tests/

verify-proofs:
	@if command -v lake > /dev/null; then \
		echo "Building Lean 4 formal verification environment..."; \
		lake build; \
	else \
		echo "Lean 4 (lake) not found. Skipping mathematical verification stubs."; \
	fi

clean:
	rm -rf venv/
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
