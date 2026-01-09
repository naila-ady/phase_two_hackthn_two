---
id: 4
title: Create Specification Skill
stage: general
date: 2026-01-06
surface: agent
model: claude-opus-4-5-20251101
feature: none
branch: main
user: user
command: general task
labels: [skill, specification, sdd, reusable]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .claude/skills/specification/skills.md
tests:
 - none
---

## Prompt

```
yes write skill that can bu used calude fo writing specification again whenevr required in any other project
```

## Response snapshot

Created a comprehensive skill file at `.claude/skills/specification/skills.md` that enables Claude to create feature specifications following the Spec-Driven Development (SDD) methodology. The skill includes:

- Purpose and process for specification creation
- Step-by-step instructions covering user scenarios, requirements, and success criteria
- Template structure to follow
- Validation checklist
- Output file locations

The skill captures the entire specification creation workflow that was used for the Todo application, making it reusable for any future projects that need specifications created following the same methodology.

## Outcome

- ✅ Impact: Created reusable skill for specification creation in future projects
- 🧪 Tests: none
- 📁 Files: Created .claude/skills/specification/skills.md with comprehensive instructions
- 🔁 Next prompts: Can use this skill for future specification creation tasks
- 🧠 Reflection: Skill follows constitution requirement to offer skill creation after completing significant tasks

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS - Skill properly documented and structured
- Prompt variant (if applicable): general skill creation
- Next experiment (smallest change to try): none needed