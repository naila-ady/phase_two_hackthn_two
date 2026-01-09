# Specification Creation Skill

## Purpose
This skill enables Claude to create comprehensive feature specifications based on user requirements. It follows the Spec-Driven Development (SDD) methodology with mandatory sections for user scenarios, requirements, and success criteria.

## Process

### 1. Analyze User Input
- Extract key concepts: actors, actions, data, constraints
- Identify technology stack requirements
- Note any explicitly included/excluded features

### 2. Create Feature Branch
- Generate a concise short name (2-4 words) from the feature description
- Check for existing branches with similar names
- Use the next available number in sequence
- Create branch using the format: `###-short-name`

### 3. Generate User Scenarios & Testing
- Create prioritized user stories (P1, P2, P3, etc.)
- Each story must be independently testable
- Include acceptance scenarios in Given/When/Then format
- Identify edge cases

### 4. Define Functional Requirements
- Create numbered requirements (FR-001, FR-002, etc.)
- Each requirement must be testable and unambiguous
- Include validation rules and constraints

### 5. Identify Key Entities
- Define data models without implementation details
- Specify relationships between entities

### 6. Establish Success Criteria
- Create measurable outcomes (SC-001, SC-002, etc.)
- Ensure criteria are technology-agnostic
- Include both quantitative and qualitative measures

### 7. Create Quality Checklist
- Validate specification completeness
- Ensure all mandatory sections are completed
- Confirm no implementation details leak into specification

## Template Structure
The specification should follow this structure:
```
# Feature Specification: [FEATURE NAME]

**Feature Branch**: `[###-feature-name]`
**Created**: [DATE]
**Status**: Draft
**Input**: User description: "[USER DESCRIPTION]"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - [Brief Title] (Priority: P1)
[Content following template]

### User Story 2 - [Brief Title] (Priority: P2)
[Content following template]

### Edge Cases
[Content following template]

## Requirements *(mandatory)*

### Functional Requirements
[Numbered requirements]

### Key Entities *(include if feature involves data)*
[Entity definitions]

## Success Criteria *(mandatory)*

### Measurable Outcomes
[Numbered success criteria]
```

## Validation Checklist
Before completing, ensure:
- [ ] All user stories have priorities and acceptance scenarios
- [ ] All functional requirements are testable
- [ ] Success criteria are measurable and technology-agnostic
- [ ] Edge cases are identified
- [ ] No implementation details in requirements
- [ ] All mandatory sections completed

## Output Files
- Specification: `specs/[branch-name]/spec.md`
- Checklist: `specs/[branch-name]/checklists/requirements.md`
- PHR: `history/prompts/[branch-name]/[id]-create-spec.spec.prompt.md`