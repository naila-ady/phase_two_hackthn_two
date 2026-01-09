# Implementation Plan Creation Skill

## Purpose
This skill enables Claude to create comprehensive implementation plans based on feature specifications using the /sp.plan command. It follows the Spec-Driven Development (SDD) methodology with structured phases for research, design, and architecture.

## Process

### 1. Setup Phase
- Execute `.specify/scripts/bash/setup-plan.sh --json` to get feature paths
- Parse JSON output for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH
- Load feature specification and constitution for context

### 2. Research Phase (Phase 0)
- Extract unknowns from Technical Context as "NEEDS CLARIFICATION"
- Generate research tasks for each unknown, dependency, and integration point
- Consolidate findings in `research.md` with:
  - Decision: [what was chosen]
  - Rationale: [why chosen]
  - Alternatives considered: [what else evaluated]

### 3. Design Phase (Phase 1)
- Extract entities from feature spec to create `data-model.md`
- Generate API contracts from functional requirements
- Create `quickstart.md` with setup instructions
- Place API contracts in `/contracts/` directory

### 4. Architecture Documentation
- Fill Technical Context with specific technologies and constraints
- Perform Constitution Check with pre- and post-design validation
- Define project structure with clear directory organization
- Document complexity tracking if needed

### 5. Agent Context Update
- Run `.specify/scripts/bash/update-agent-context.sh claude`
- Update agent-specific context with new technologies from the plan

## Required Artifacts
The plan creation process produces these files:
- `plan.md` - Main implementation plan with technical context and architecture
- `research.md` - Research findings and technology decisions
- `data-model.md` - Entity definitions and data structures
- `quickstart.md` - Setup and running instructions
- `contracts/` directory - API contracts and specifications
- Updated agent context file

## Constitution Compliance Checks
Each plan must validate:
- Technology Stack Compliance (FastAPI, SQLModel, Next.js, etc.)
- Feature Scope Limitation (no AI/NLP features)
- Spec-Driven Development approach
- Code Generation Only (no manual coding)
- Security and Privacy requirements

## Template Structure
The implementation plan follows this structure:
```
# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

## Summary
[Primary requirement + technical approach]

## Technical Context
[Technology stack, dependencies, constraints]

## Constitution Check
[Pre-design and post-design validation]

## Project Structure
[Directory structure and organization]

## Complexity Tracking
[For any constitution violations that need justification]
```

## Validation Checklist
Before completing, ensure:
- [ ] All constitution checks passed
- [ ] Research.md resolves all NEEDS CLARIFICATION items
- [ ] Data model matches specification requirements
- [ ] API contracts align with functional requirements
- [ ] Project structure supports the planned architecture
- [ ] Agent context updated with new technologies
- [ ] All required artifacts created

## Output Files
- Plan: `specs/[branch-name]/plan.md`
- Research: `specs/[branch-name]/research.md`
- Data Model: `specs/[branch-name]/data-model.md`
- Quickstart: `specs/[branch-name]/quickstart.md`
- Contracts: `specs/[branch-name]/contracts/`
- PHR: `history/prompts/[branch-name]/[id]-create-implementation-plan.plan.prompt.md`