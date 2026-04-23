# Pequod — build targets.
#
#   make specimen   Regenerate specimen/specimen.pdf from specimen.typ
#   make cvd        Run the colourblindness check on pequod.json
#   make clean      Remove generated artefacts

SHELL := /bin/bash

.PHONY: specimen cvd clean help

help:
	@echo "Pequod build targets:"
	@echo "  make specimen   Regenerate specimen/specimen.pdf from specimen.typ"
	@echo "  make cvd        Run the CVD simulation on pequod.json"
	@echo "  make clean      Remove generated artefacts"

specimen: specimen/specimen.pdf

specimen/specimen.pdf: specimen/specimen.typ
	typst compile $< $@

cvd:
	python3 scripts/cvd_check.py

clean:
	rm -f specimen/specimen.pdf
