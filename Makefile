# Pequod — build targets.
#
#   make specimen   Regenerate specimen/specimen.pdf from specimen.typ
#   make cvd        Run the colourblindness check on pequod.json
#   make clean      Remove generated artefacts

SHELL := /bin/bash

.PHONY: specimen cvd r-data r-check vsix vsce-publish py-data py-build py-test py-publish tw-test tw-pack tw-publish clean help

help:
	@echo "Pequod build targets:"
	@echo "  make specimen      Regenerate specimen/specimen.pdf from specimen.typ"
	@echo "  make cvd           Run the CVD simulation on pequod.json"
	@echo "  make r-data        Regenerate r/R/palettes-data.R from pequod.json"
	@echo "  make r-check       R CMD check the R package"
	@echo "  make vsix          Build the VS Code extension as a .vsix"
	@echo "  make vsce-publish  Publish the VS Code extension to the marketplace"
	@echo "  make py-data       Regenerate python/src/pequod/_data.py from pequod.json"
	@echo "  make py-build      Build the Python sdist + wheel"
	@echo "  make py-test       Run the Python test suite"
	@echo "  make py-publish    Upload the Python package to PyPI"
	@echo "  make tw-test       Run the Tailwind plugin tests"
	@echo "  make tw-pack       Pack the Tailwind plugin as an npm tarball"
	@echo "  make tw-publish    Publish the Tailwind plugin to npm"
	@echo "  make clean         Remove generated artefacts"

specimen: specimen/specimen.pdf

specimen/specimen.pdf: specimen/specimen.typ
	typst compile $< $@

cvd:
	python3 scripts/cvd_check.py

r-data:
	cd r && Rscript data-raw/generate_palettes.R

r-check:
	cd r && R CMD build . && R CMD check pequod_*.tar.gz

vsix:
	cd vscode && npx --yes @vscode/vsce package --no-dependencies

vsce-publish:
	cd vscode && npx --yes @vscode/vsce publish --no-dependencies

py-data:
	cd python && python3 data-raw/generate_data.py

py-build:
	cd python && rm -rf dist build *.egg-info && python3 -m build

py-test:
	cd python && python3 -m pytest

py-publish:
	cd python && python3 -m twine upload dist/*

tw-test:
	cd tailwind && node --test test.js

tw-pack:
	cd tailwind && npm pack

tw-publish:
	cd tailwind && npm publish

clean:
	rm -f specimen/specimen.pdf
	rm -f r/pequod_*.tar.gz
	rm -rf r/pequod.Rcheck
	rm -f vscode/*.vsix
	rm -rf python/dist python/build python/*.egg-info python/.pytest_cache
	rm -f tailwind/*.tgz
