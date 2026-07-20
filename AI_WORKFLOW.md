# AI Workflow Instructions

Use this file when an AI assistant is helping someone create and tailor job applications with this repo.

This workflow supports technical and non-technical backgrounds, including chemistry, laboratory work, education, customer service, administration, sales, hospitality, healthcare support, finance, operations, research, graduate applications, and IT/data roles.

## Goal

Create a focused, honest, ATS-friendly job application package from the user's real background and a specific job post.

The final output should be:

- `Full Name CV.pdf`
- `Full Name CV.docx`
- `Full Name Cover Letter.pdf`
- `Full Name Cover Letter.docx`

## Privacy Rule

This workflow can contain personal contact details, CVs, and job applications. Keep generated application folders local unless the user explicitly asks to publish or share them.

Do not commit filled resumes or generated applications to a public repo.

## First-Time Setup

Before tailoring any job application, ask the user to provide their current CV/resume or career details.

Accepted inputs:

- PDF CV
- DOCX CV
- Google Docs export
- plain text resume
- LinkedIn profile text
- pasted work history
- rough notes about education, experience, projects, skills, and target jobs

Then:

1. Extract the real content.
2. Clean broken formatting from PDF exports, columns, symbols, and corrupted characters.
3. Ask only necessary clarifying questions if key facts are missing.
4. Rewrite the content into a clear `master-resume.md`.
5. Keep the master resume broad because it will be used for many tailored versions.
6. Add confirmed projects, coursework, internships, volunteer work, lab work, research work, freelance work, or practical tasks that are missing from the old CV.
7. Mark unclear details as `Needs confirmation` instead of inventing them.
8. Remove or avoid sensitive personal information unless the job explicitly requires it.

Avoid including:

- national ID numbers
- passport numbers
- home addresses unless required
- birth dates
- referee phone/email details unless the user explicitly wants them included
- private client details unless the user confirms they can be named

## Consultative Intake

Be consultative, but do not overwhelm the user.

If the user has little experience, do not stop because the CV looks thin. Build from:

- education
- coursework
- practical assignments
- final-year projects
- lab work
- internships
- attachments
- volunteer work
- family business support
- part-time work
- online courses
- certificates
- personal projects
- leadership roles
- club/society work
- customer-facing tasks
- tools they have used in school or practice

Ask at most 3-5 important questions at a time. If the user does not answer everything, continue with a reasonable draft and mark unclear details as `Needs confirmation`.

Good first intake questions:

1. What type of jobs are you targeting?
2. What is your highest education level and field of study?
3. Have you done any internship, attachment, volunteer work, part-time work, or practical project?
4. What tools, software, lab equipment, languages, or platforms have you used?
5. Do you have any certificate, short course, competition, club role, or achievement worth including?

Ask follow-up questions only when they improve the application materially.

## Truthfulness Rules

- Do not invent employers, dates, tools, certifications, grades, metrics, or outcomes.
- Do not claim paid work if it was coursework, volunteer work, personal work, or an unpaid internship.
- Do not overstate skill level.
- Improve wording and positioning, but keep facts true.
- If the job requires something the user does not have, use adjacent real experience honestly or leave it out.

## Master Resume Content

Create `master-resume.md` with this structure:

```markdown
# Full Name - Master Resume

Email: email@example.com  
Phone: phone number  
LinkedIn: LinkedIn URL  
Portfolio: portfolio URL if available

## Target Titles

- Target role 1
- Target role 2

## Professional Summary

Broad summary based on real experience.

## Core Skills

### Skill Category

- Skill
- Skill

## Relevant Experience

### Job, Internship, Project, Coursework, or Volunteer Role

Company, institution, or context  
Date range or project type

- Real responsibility, achievement, or task.
- Real responsibility, achievement, or task.

## Education

### Degree, Diploma, Certificate, or Program

Institution

## Certifications and Training

- Certification or training

## Projects, Practical Work, or Coursework

### Project Name

Brief description.

## Languages

- Language

## Role-Specific Positioning Notes

### Role Category

What to emphasize and downplay for this type of role.
```

## Little-Experience Resume Strategy

For users with little formal work experience:

- Put education higher.
- Use a stronger `Projects, Practical Work, or Coursework` section.
- Include internships, attachments, volunteer roles, and part-time work as experience if relevant.
- Use transferable skills honestly.
- Keep the tone confident but not exaggerated.
- Avoid senior-sounding titles that the user has not earned.
- Prefer `Relevant Experience` over `Professional Experience` if most experience is coursework, practical work, or internships.
- Use `Selected Practical Work` instead of `Selected Projects` when the user is not technical.
- Keep the CV to 1 page unless the user has enough real content for 2 pages.

## Output Folder

Create one local-only folder per application:

```text
applications/company-role/
```

Use lowercase folder slugs with no spaces.

The `applications/` folder is intentionally ignored by Git. Do not push generated job applications unless the user explicitly asks.

## Required Files Per Application

Create:

```text
applications/company-role/tailored-resume.md
applications/company-role/cover-email.md
applications/company-role/application-notes.md
```

Then run the generator to create PDF and DOCX files.

## Tailoring Rules

Do not simply copy the master resume. Tailor it.

## Resume Headline Rule

Do not copy the advertised job title into the resume headline unless the user has already held that title or explicitly asks for it.

Use a capability-based headline that matches the role while staying honest. The headline should describe what the candidate can do, not pretend they already have the advertised title.

Good examples:

- `ICT Support | Technical Troubleshooting | Customer & Operations Support`
- `Laboratory Support | Sample Handling | Quality Documentation`
- `Administration | Customer Service | Records Management`
- `Data Analysis | Reporting | Spreadsheet Workflows`

Avoid inflated or title-copy headlines such as:

- `Support & Operations Executive`
- `Senior Data Analyst`
- `Laboratory Manager`

For each job:

- Rewrite the summary to match the role.
- Put the most relevant experience first.
- Use the job post's keywords naturally.
- Highlight only experience, coursework, projects, or skills that support the job.
- Downplay unrelated details.
- Keep the CV easy for humans to scan and readable for ATS.
- Prefer clear headings, normal bullets, and plain text structure.
- For early-career users, aim for 1 page when possible and 2 pages only when justified.
- If the user lacks direct experience, match the role through transferable skills, coursework, internships, practical work, and reliable learning ability.

## Background-Specific Positioning

### Chemistry / Laboratory / Science

Emphasize laboratory techniques, sample preparation, chemical handling and safety, quality control, documentation, data recording, equipment use, report writing, attention to detail, research projects, and relevant coursework.

### Customer Service / Call Centre / Sales

Emphasize communication, customer handling, follow-up, recordkeeping, CRM or spreadsheet use, complaint resolution, sales support, reliability, and target-driven work.

### Administration / Office Support

Emphasize data entry, email and document handling, scheduling, filing, Microsoft Office, Google Sheets/Excel, organization, accuracy, and confidentiality.

### Graduate / Internship / Entry-Level

Emphasize education, coursework, internships, practical assignments, volunteer work, transferable skills, willingness to learn, reliability, and communication.

### Technical / Data / IT

Emphasize tools, projects, automation, data analysis, dashboards, troubleshooting, programming, and technical support only when relevant.

## `tailored-resume.md` Format

Use:

```markdown
# Full Name

Role-aligned headline

Email: email@example.com  
Phone: phone number  
LinkedIn: LinkedIn URL  
Portfolio: portfolio URL

## Professional Summary

Short role-matched summary.

## Key Skills

- Skill 1
- Skill 2
- Skill 3

## Relevant Experience

### Job, Internship, Project, or Coursework Title

Company, institution, or context  
Date or project type

- Strong real responsibility or achievement.
- Strong real responsibility or achievement.

## Education

### Degree, Diploma, Certificate, or Program

Institution

## Certifications and Training

- Certification

## Selected Practical Work

### Project, Coursework, or Practical Task

Short description focused on this job.
```

## `cover-email.md` Format

Use:

```markdown
# Cover Email

To: recipient email if known  
Subject: Application for Role Name

Dear Hiring Team,

Paragraph 1: State the role and interest.

Paragraph 2: Match the user's strongest experience to the role.

Paragraph 3: Mention role-specific strengths, tools, reliability, communication, or learning ability.

I have attached my CV for your review.

Kind regards,  
Full Name  
Phone  
Portfolio or LinkedIn URL if available
```

For Reddit, Discord, WhatsApp, or LinkedIn DMs, create a shorter message instead of a formal cover letter, but still save it as `cover-email.md`.

## `application-notes.md` Format

Include:

```markdown
# Company - Application Notes

## Role

Role name

## Best Resume Emphasis

- Item
- Item

## Experience to Highlight

- Experience, project, coursework, or skill

## Downplay for This Application

- Item
- Item

## Application Strategy

Apply directly / send email / send DM / ask for related work / avoid.
```

## Generate PDF and DOCX

Install dependencies first if needed:

```powershell
python -m pip install -r requirements.txt
```

Run from the repo root:

```powershell
python scripts\build_application_docs.py --resume-md applications\company-role\tailored-resume.md --cover-md applications\company-role\cover-email.md --out-dir applications\company-role --prefix "Full Name"
```

If `python` is unavailable, use the user's working Python command, such as `py` on Windows.

## Quality Checks

After generating files:

- Run `python scripts\review_application_package.py applications\company-role --prefix "Full Name"` from the repo root, replacing `Full Name` with the user's real name.
- Confirm the PDF opens and has a reasonable page count.
- Confirm the CV PDF is usually 1-2 pages.
- Confirm the cover letter PDF is usually 1 page.
- Confirm the generated header uses the correct user's name and contact details.
- Confirm the role/company/job title in the cover letter is correct.
- Confirm no placeholder text remains.
- Confirm no unrelated or distracting experience is over-emphasized.
- Confirm generated application folders are not staged for Git unless the user explicitly wants that.

## Final Application Review

Before telling the user the package is ready, the AI must review the generated `tailored-resume.md`, `cover-email.md`, and the generated PDF text/output like a recruiter would.

Do not rely only on the script passing. The script catches mechanical issues; the AI review must catch judgment issues, weak wording, duplication, and anything that looks awkward to a human reader.

Check:

- The headline is capability-based and does not copy an advertised title the user has not held.
- The first half page immediately matches the role's strongest needs.
- The most relevant experience, coursework, or practical work appears before weaker or unrelated content.
- The cover letter does not say "I have attached my CV and cover letter" inside the cover letter itself. Use "I have attached my CV for your review."
- The same portfolio, phone number, email, or link is not repeated awkwardly in both the paragraph body and signature/footer.
- Email metadata such as `To:`, `CC:`, or `Subject:` does not appear as part of the formal letter body in the PDF.
- The cover letter names the correct company, role, and reference number if known.
- No wording sounds inflated, desperate, generic, or copied from the job post.
- No sentence is too broad for the application. If the job is specific, the wording should be specific.
- The application sounds like the candidate is applying for relevant work, not begging for any role.
- Senior terms such as "manager", "lead", "executive", or "specialist" are used only when they honestly fit the user's background.
- The final answer tells the user which file to send first and whether to paste the cover text or attach the cover letter PDF.

If the AI finds a wording or positioning issue, it should fix the source Markdown, regenerate the PDF/DOCX, rerun the review script, and only then report that the package is ready.

## Final Response to User

After generating files, tell the user:

- Where the files are.
- Which file to send first.
- Whether the cover letter should be attached or pasted as email text.
- Any facts the user still needs to confirm.
- Any limitations, such as if visual DOCX render QA could not be completed.

Do not overwhelm the user with the full resume text unless they ask.
