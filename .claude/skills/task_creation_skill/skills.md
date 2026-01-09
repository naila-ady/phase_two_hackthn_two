# Task Creation Skill

## Purpose
This skill enables Claude to create comprehensive implementation task lists based on feature specifications and planning documents. It follows the Spec-Driven Development (SDD) methodology with structured phases and clear dependencies.

## Process

### 1. Setup Phase
- Identify the feature branch and related specification files
- Review the feature specification and implementation plan for context
- Understand the scope and requirements of the feature

### 2. Task Breakdown Phase
- Organize tasks into logical phases (e.g., Backend Foundation, Database Integration, Frontend Foundation, Feature Completion)
- Define individual tasks with clear dependencies between them
- Ensure each task has:
  - Clear dependency requirements
  - Specific action to perform ("What to do")
  - Clear acceptance criteria
  - Expected output

### 3. Structure Requirements
- Group related tasks into phases for logical progression
- Maintain dependency chains to ensure proper implementation order
- Include checkpoint milestones between phases for review
- Add human action requirements at key checkpoints

### 4. Task Definition Format
Each task should follow this format:
```
#### Task X.Y: [Task Name]
- **Depends on**: [Previous task or phase completion]
- **What to do**: [Specific action to perform]
- **Acceptance Criterion**: [How to verify completion]
- **Output**: [What files/artifacts will be created]
- **Status**: [pending, in-progress, completed]
```

### 5. Checkpoint Structure
- Define clear verification steps at the end of each phase
- Include human review and approval requirements
- Specify action needed to proceed (e.g., "Human review → Approve → Commit → Proceed")

## Required Artifacts
The task creation process produces:
- `tasks.md` - Main task breakdown with all implementation steps
- Status tracking for each task
- Dependency mapping between tasks
- Checkpoint definitions between phases

## Template Structure
The tasks file follows this structure:
```
# Implementation Tasks: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Plan**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md` and implementation plan

## [Feature Name and Description]

### Phase X – [Phase Name]
#### Task X.Y: [Task Name]
- **Depends on**: [Dependencies]
- **What to do**: [Action]
- **Acceptance Criterion**: [Verification]
- **Output**: [Artifacts]
- **Status**: [pending]

### ✅ CHECKPOINT X – [Checkpoint Name]
- **Status**: [pending]
- **Verification**: [What to verify]
- **Action**: [Human action required]
```

## Validation Checklist
Before completing, ensure:
- [ ] All tasks have clear dependencies defined
- [ ] Each task has specific acceptance criteria
- [ ] Outputs are clearly specified for each task
- [ ] Phases are logically organized
- [ ] Checkpoints include human review requirements
- [ ] Task statuses are properly initialized
- [ ] No circular dependencies exist between tasks

## Best Practices
- Break complex features into smaller, manageable tasks
- Maintain logical progression from foundation to advanced features
- Ensure each task has a clear, testable outcome
- Include both technical tasks and verification steps
- Consider integration points between frontend and backend
- Plan for data persistence and state management requirements

## Output Files
- Tasks: `specs/[branch-name]/tasks.md`
- PHR: `history/prompts/[branch-name]/[id]-create-tasks.tasks.prompt.md`