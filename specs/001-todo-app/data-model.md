# Data Model for Todo Application

## Todo Entity

### Fields
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key, Auto-generated | Unique identifier for each todo |
| title | String | Required, Min length: 1 | Title of the todo item |
| description | String | Optional | Detailed description of the todo |
| completed | Boolean | Default: False | Completion status of the todo |
| priority | Enum (low, medium, high) | Required, Default: medium | Priority level of the todo |
| category | String | Optional | Category or tag for grouping todos |
| due_date | DateTime | Optional | Deadline for the todo |
| created_at | DateTime | Auto-generated | Timestamp when the todo was created |
| updated_at | DateTime | Auto-generated, Auto-update | Timestamp when the todo was last updated |

### Validation Rules
- `title`: Must not be empty (length > 0)
- `priority`: Must be one of the allowed values ('low', 'medium', 'high')
- `due_date`: If provided, must be a valid date/time format
- `completed`: Boolean value (true/false)

### State Transitions
- `completed` field can transition from `false` to `true` (marked as done)
- `completed` field can transition from `true` to `false` (unmarked as done)
- `updated_at` field updates automatically on any modification

## Relationships
None for the basic Todo entity. Future extensions might include relationships to users or tags.

## Indexes
- Primary index on `id`
- Secondary index on `completed` for filtering
- Secondary index on `priority` for sorting/filtering
- Secondary index on `due_date` for sorting/filtering