# Application Flow

A lightweight workflow for turning a user's existing CV/resume and a job post into a tailored application package.

The workflow is designed to be:

- ATS-friendly
- readable for human recruiters
- honest and role-specific
- useful for technical and non-technical backgrounds
- safe to use locally without committing private applications

## What This Repo Does

1. Convert a user's existing CV/resume into a clean `master-resume.md`.
2. Use a job post to create a tailored resume and cover letter/message.
3. Package the tailored content into PDF and DOCX files.

The generator script does not write the application content by itself. An AI assistant or human writes the tailored Markdown files, then the script formats them into sendable documents.

## Files

- `AI_WORKFLOW.md` - instructions for an AI assistant to intake a user's CV and tailor applications.
- `master-resume-template.md` - blank template for a user's master resume.
- `scripts/build_application_docs.py` - converts tailored Markdown into PDF and DOCX files.
- `scripts/review_application_package.py` - checks a generated package for common mistakes before sending.
- `requirements.txt` - Python dependencies for document generation.

## First-Time Setup

The user should provide their existing CV/resume first. It can be a PDF, DOCX, Google Docs export, plain text, LinkedIn text, or rough career notes.

The AI assistant should:

1. Extract and clean the real content.
2. Ask a few targeted questions if important details are missing.
3. Create `master-resume.md` from `master-resume-template.md`.
4. Keep the master resume broad so it can support many job applications.

For users with little experience, build from education, coursework, internships, attachments, volunteer work, part-time work, practical projects, certificates, and transferable skills.

## Per-Job Workflow

Create a local application folder:

```text
applications/company-role/
```

Inside it, create:

```text
tailored-resume.md
cover-email.md
application-notes.md
```

Then generate the documents:

```powershell
python scripts\build_application_docs.py --resume-md applications\company-role\tailored-resume.md --cover-md applications\company-role\cover-email.md --out-dir applications\company-role --prefix "Full Name"
```

If Python packages are missing:

```powershell
python -m pip install -r requirements.txt
```

On Windows, if `python` is not available, try:

```powershell
py -m pip install -r requirements.txt
py scripts\build_application_docs.py --resume-md applications\company-role\tailored-resume.md --cover-md applications\company-role\cover-email.md --out-dir applications\company-role --prefix "Full Name"
```

## Output

The script creates:

```text
Full Name CV.pdf
Full Name CV.docx
Full Name Cover Letter.pdf
Full Name Cover Letter.docx
```

Send the PDF by default. Use DOCX only if the employer asks for Word format.

## Review Before Sending

Run the package review after generating files:

```powershell
python scripts\review_application_package.py applications\company-role --prefix "Full Name"
```

The review checks for missing files, unresolved placeholders, weak attachment wording, resume headline risks, and PDF page counts.

Do not commit generated CVs, cover letters, phone numbers, emails, or job-specific application folders unless you intentionally want them public.

