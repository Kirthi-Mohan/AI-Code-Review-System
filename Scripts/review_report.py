
from AI_Code_Review.scripts.code_parser import parse_file
from AI_Code_Review.scripts.ai_suggestions import suggest_improvements
from AI_Code_Review.scripts.lint_checker import run_pylint_safe
import datetime, os

def build_report(file_path: str, include_ai: bool = True) -> str:
    parsed, code = parse_file(file_path)
    pylint_text = run_pylint_safe(file_path)
    ai_text = suggest_improvements(code) if include_ai else "AI suggestions disabled."

    report = f"""# AI Code Review Report
File: {file_path}
Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Code Structure
- Functions: {[f['name'] for f in parsed['functions']]}
- Classes:   {[c['name'] for c in parsed['classes']]}
- Imports:   {parsed['imports']}

## Pylint Findings
{pylint_text}

## AI Suggestions
{ai_text}
"""
    return report

def save_report(report_text: str, out_dir: str = 'AI_Code_Review/reports', filename: str = None) -> str:
    os.makedirs(out_dir, exist_ok=True)
    if not filename:
        filename = f'report_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.md'
    path = os.path.join(out_dir, filename)
    with open(path, "w") as f:
        f.write(report_text)
    return path
