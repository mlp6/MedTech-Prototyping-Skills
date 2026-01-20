# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Duke BME 254L MedTech Prototyping Skills course website, built with Quarto. The site contains lecture materials, lab assignments, and resources for teaching medical device prototyping skills including CAD (Onshape), electronic design automation (KiCad), microcontroller firmware (Arduino), and version control (git).

## Build Commands

```bash
# Render all Quarto documents to HTML
make all
# or directly:
quarto render

# Clean generated HTML and auxiliary files
make clean

# Preview site locally with live reload
quarto preview
```

## Environment Setup

```bash
# Create conda environment with Python 3.11 and data science packages
conda env create -f environment.yml
conda activate medtech-prototyping-skills
```

## Architecture

### Content Structure

- `lectures/` - Learning modules as QMD files, rendered as both slides (RevealJS) and notes (HTML)
- `labs/` - Hands-on lab assignments with step-by-step instructions
- `resources/` - Reference materials, PDFs, and guides
- `kicad/` - Example KiCad projects (voltage divider, RC circuits, active LPF)
- `modules/` - Git submodules linking to external content repositories

### Key Configuration Files

- `_quarto.yml` - Main Quarto config: site navigation, theme, sidebar structure
- `lectures/_metadata.yml` - Lecture-specific metadata for dual output (slides + notes)
- `environment.yml` - Conda environment specification
- `.github/workflows/publish.yml` - GitHub Actions deployment to GitHub Pages

### Navigation

Sidebar navigation is controlled entirely via `_quarto.yml`. Content is organized into sections: Course Information, Learning Modules, Labs, and Resources.

## Deployment

The site auto-deploys to GitHub Pages via GitHub Actions on push to main. The workflow uses Quarto 1.7.31 with TinyTeX for PDF generation.

## Content Conventions

- QMD files use Quarto markdown with YAML front matter
- Lectures use `format: live-html` for notes and `format: live-revealjs` for slides
- Images stored in `lectures/images/` and `labs/images/`
- The site uses Atkinson Hyperlegible font and a11y-light code theme for accessibility
