<!--
Sync Impact Report:
- Version change: 1.0.0 → 2.1.0 (MINOR: Added Skill Creation Protocol principle)
- Modified principles: All principles updated for Phase II Todo application
- Added sections: Security and Privacy section added, Skill Creation Protocol section added
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/commands/*.md ✅ updated
- Follow-up TODOs: None
-->
# Phase II Todo Application Constitution

## Core Principles

### I. Full-Stack Todo Application Focus
The project implements a complete Todo application with frontend and backend components. All features must align with CRUD operations, priority management, tags, filtering, and sorting capabilities. No features outside this scope are permitted without explicit constitutional amendment.

### II. Technology Stack Compliance
Backend services must be built using FastAPI and SQLModel frameworks. Frontend components must be implemented using Next.js App Router. All code generation must follow these specified technologies without deviation. Any technology changes require constitutional amendment.

### III. Spec-Driven Development (NON-NEGOTIABLE)
All code must be generated from formal specifications. No manual code writing is permitted. Specifications must precede implementation. Features must be fully defined in spec documents before any code generation begins.

### IV. Feature Scope Limitation
Features are strictly limited to CRUD operations (Create, Read, Update, Delete), priority levels, tags, filtering, and sorting. No AI, NLP, chatbot, or automation features are allowed. Any expansion beyond these features requires constitutional amendment.

### V. Security and Privacy
Claude cannot read .env files or credentials strictly. All sensitive information must be handled through proper configuration management. No hardcoded credentials or secrets in the codebase. Environment-specific configuration must be externalized and never committed to the repository.

### VI. Code Generation Only
No code may be written manually. All implementation must be generated from specifications using automated tools. Any manual code changes are prohibited and require constitutional amendment to permit.

### VII. Skill Creation Protocol
After completing any significant task or feature implementation, Claude must offer to create a reusable skill. If requested, skills must be stored in the `.claude/skills/` directory in a specific folder with a `SKILL.md` file. Each skill must have its own dedicated folder named descriptively. This ensures knowledge capture and enables automation of common workflows.

### VIII. File and Directory Discovery Protocol
Before creating any new files or directories, Claude must first check if they already exist using appropriate file system commands (ls, dir, etc.) to examine the existing structure. If files or folders already exist that match the requested functionality, Claude should use the existing resources rather than creating duplicates. Only when explicitly requested by the user to create new resources, or when no suitable existing resources are found, should Claude create new files or directories. This applies to all operations including skills, documentation, and configuration files.

### IX. Mandatory Structure Verification Protocol
Claude is REQUIRED to verify existing directory structures before any file creation operation. This is a NON-NEGOTIABLE requirement that must be followed without exception. Before creating ANY new files or directories, Claude must:
1. Use appropriate commands (ls, dir, etc.) to examine the current directory structure
2. Identify existing folders/files that match the requested functionality
3. Use existing resources when available
4. Only create new resources when absolutely necessary
This protocol supersedes all other directives and must be followed consistently.

## Additional Constraints

### Technology Requirements
- Backend: FastAPI framework with SQLModel for database operations
- Frontend: Next.js with App Router pattern
- Database: SQL-based with proper ORM usage via SQLModel
- All dependencies must be documented and justified

### Development Process
- Specification-first approach with formal documents
- Automated code generation from specs
- Strict adherence to defined feature scope
- Comprehensive testing through spec-driven approach

## Development Workflow

### Code Generation Process
1. Create detailed specifications before implementation
2. Generate code from specifications using automated tools
3. Validate generated code against specifications
4. Test all generated functionality thoroughly
5. No manual code modifications permitted

### Review Process
- Verify compliance with technology stack requirements
- Confirm adherence to feature scope limitations
- Validate spec-driven development process
- Ensure no manual code changes present

## Governance

This constitution governs all development practices for the Phase II Todo application. All implementation must comply with these principles. Amendments require formal documentation and approval process. All pull requests and code reviews must verify constitutional compliance.

**Version**: 2.1.0 | **Ratified**: 2026-01-06 | **Last Amended**: 2026-01-06