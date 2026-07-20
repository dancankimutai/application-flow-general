from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


REQUIRED_SOURCE_FILES = [
    "tailored-resume.md",
    "cover-email.md",
    "application-notes.md",
]

PLACEHOLDER_TERMS = [
    "Full Name",
    "email@example.com",
    "phone number",
    "Needs confirmation",
    "Role Name",
    "Company - Application Notes",
]

BAD_COVER_PHRASES = [
    "attached my CV and cover letter",
    "attached my resume and cover letter",
]

SENIOR_TITLE_TERMS = [
    "Senior",
    "Manager",
    "Lead",
    "Executive",
    "Director",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def first_resume_headline(resume_text: str) -> str:
    lines = [line.strip() for line in resume_text.splitlines() if line.strip()]
    for index, line in enumerate(lines):
        if line.startswith("# ") and index + 1 < len(lines):
            return lines[index + 1]
    return ""


def check_pdf_pages(path: Path, *, min_pages: int, max_pages: int) -> tuple[bool, str]:
    try:
        page_count = len(PdfReader(str(path)).pages)
    except Exception as exc:  # pragma: no cover - defensive CLI output
        return False, f"{path.name}: could not read PDF page count: {exc}"
    if page_count < min_pages or page_count > max_pages:
        return False, f"{path.name}: {page_count} pages, expected {min_pages}-{max_pages}"
    return True, f"{path.name}: {page_count} pages"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("application_dir", help="Application folder, for example applications/company-role")
    parser.add_argument("--prefix", required=True, help='Generated file prefix, for example "Full Name"')
    args = parser.parse_args()

    app_dir = Path(args.application_dir)
    errors: list[str] = []
    warnings: list[str] = []
    notes: list[str] = []

    if not app_dir.exists():
        errors.append(f"Application folder not found: {app_dir}")
    else:
        for file_name in REQUIRED_SOURCE_FILES:
            if not (app_dir / file_name).exists():
                errors.append(f"Missing source file: {file_name}")

    resume_path = app_dir / "tailored-resume.md"
    cover_path = app_dir / "cover-email.md"

    combined_text = ""
    resume_text = ""
    cover_text = ""
    if resume_path.exists():
        resume_text = read_text(resume_path)
        combined_text += resume_text + "\n"
    if cover_path.exists():
        cover_text = read_text(cover_path)
        combined_text += cover_text + "\n"

    for term in PLACEHOLDER_TERMS:
        if term in combined_text:
            errors.append(f"Placeholder or unresolved text remains: {term}")

    for phrase in BAD_COVER_PHRASES:
        if phrase.lower() in cover_text.lower():
            errors.append(f"Bad cover-letter attachment wording: {phrase}")

    headline = first_resume_headline(resume_text)
    if not headline:
        errors.append("Could not identify resume headline under the candidate name.")
    else:
        notes.append(f"Resume headline: {headline}")
        for term in SENIOR_TITLE_TERMS:
            if term.lower() in headline.lower():
                warnings.append(f"Headline uses senior/title word '{term}'. Confirm this is honest for the candidate.")

    expected_files = [
        (f"{args.prefix} CV.pdf", 1, 2),
        (f"{args.prefix} Cover Letter.pdf", 1, 1),
        (f"{args.prefix} CV.docx", 1, 1),
        (f"{args.prefix} Cover Letter.docx", 1, 1),
    ]
    for file_name, min_pages, max_pages in expected_files:
        path = app_dir / file_name
        if not path.exists():
            errors.append(f"Missing generated file: {file_name}")
            continue
        if path.suffix.lower() == ".pdf":
            ok, message = check_pdf_pages(path, min_pages=min_pages, max_pages=max_pages)
            if ok:
                notes.append(message)
            else:
                errors.append(message)

    if errors:
        print("FAILED")
        for item in errors:
            print(f"- {item}")
    else:
        print("PASSED")

    if warnings:
        print("\nWarnings")
        for item in warnings:
            print(f"- {item}")

    if notes:
        print("\nChecks")
        for item in notes:
            print(f"- {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
