# Pequod — build targets.
#
#   make specimen   Regenerate specimen/specimen.pdf from specimen.typ
#   make cvd        Run the colourblindness check on pequod.json
#   make clean      Remove generated artefacts

SHELL := /bin/bash

.PHONY: specimen cvd r-data r-check vsix vsce-publish clean help

help:
	@echo "Pequod build targets:"
	@echo "  make specimen      Regenerate specimen/specimen.pdf from specimen.typ"
	@echo "  make cvd           Run the CVD simulation on pequod.json"
	@echo "  make r-data        Regenerate r/R/palettes-data.R from pequod.json"
	@echo "  make r-check       R CMD check the R package"
	@echo "  make vsix          Build the VS Code extension as a .vsix"
	@echo "  make vsce-publish  Publish the VS Code extension to the marketplace"
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

clean:
	rm -f specimen/specimen.pdf
	rm -f r/pequod_*.tar.gz
	rm -rf r/pequod.Rcheck
	rm -f vscode/*.vsix
