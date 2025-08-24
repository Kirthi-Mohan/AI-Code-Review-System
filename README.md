# AI Code Review Project

This project parses Python code, runs pylint, and gives AI-powered improvement suggestions.

## Structure

- **data/sample_code/** : Sample Python code.
- **scripts/** : Code parser, AI suggestion generator, report builder.
- **reports/** : Saved AI code review reports (optional).

## Usage

1. Import and run `review_report.build_report(file_path)`.
2. Get a Markdown report with code structure, pylint results, and AI suggestions.
