# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in app.py.
7. Refine UML so it matches what you actually built.

## ✨ Features

- Multi-pet care tracking: one owner manages any number of pets, each with its own task list.
- Task validation: tasks need a description, a positive duration, a frequency, and an optional time.
- Sorting by time: tasks are ordered chronologically; tasks without a time go last.
- Filtering: list tasks by pet name (case-insensitive), by completion status, or both.
- Conflict warnings: pending tasks that share the same start time, even across different pets, produce a readable warning. Warnings are listed in chronological order.
- Daily and weekly recurrence: completing a recurring task automatically adds the next occurrence with a due date 1 or 7 days later.
- Time-budgeted daily plan: pending tasks are taken in time order and kept only if they fit the owner's available minutes.

## Implementation Summary

The backend logic lives in pawpal_system.py. Task stores an activity's description, scheduled time, duration, frequency, and completion status. Each Pet owns a list of tasks, and an Owner manages multiple pets and can filter their tasks by pet name or completion status. Scheduler sorts tasks chronologically, skips completed tasks, fits tasks within the available time, and reports same-time scheduling conflicts as warnings. main.py demonstrates these behaviors in the terminal.

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
............                                                             [100%]
12 passed in 0.03s
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.sort_by_time() | Orders tasks by their HH:MM scheduled time; tasks without a time appear last. |
| Filtering | Owner.get_all_tasks() | Optional completion-status and pet-name filters. |
| Conflict handling | Scheduler.detect_conflicts() | Returns warnings when pending tasks for any pets share an start time. |
| Recurring tasks | Scheduler.complete_task(), Task.next_occurrence() | Completing a daily or weekly task marks it done and adds a fresh pending copy to the same pet with due_date advanced by 1 day (daily) or 7 days (weekly), counted from the task's`due_date or today if unset; other frequencies do not recur. |
| Plan generation | Scheduler.generate_plan() | Walks tasks in time order and keeps pending ones that fit the owner's remaining minutes. |





## 🎬 Demo Walkthrough

### Running the app

```bash
streamlit run app.py     # web UI
python main.py           # terminal demo
```

### Main UI features

In the Streamlit app (app.py) a user can:

- Set time available today** in minutes.
- Add pets by name and species (dog, cat, other).
- Add care tasks** to a chosen pet: description, duration, scheduled time, and frequency (daily, weekly, as needed).
- Review each pet's task table.
- Click Generate schedule to see today's plan, with conflict warnings shown above it.

### Example workflow

1. Set time available to 60 minutes.
2. Add a pet, for example "Mochi" (dog), then another, "Biscuit" (cat).
3. Choose Mochi and add "Morning medication" (5 min, 06:45, daily). Choose Biscuit and add "Feeding" (10 min, 06:45, daily).
4. Add a few more tasks, such as "Morning walk" (25 min, 08:00) and "Brush coat" (10 min, 12:00, weekly).
5. Click Generate schedule. A yellow warning reports the 06:45 conflict between the two pets, followed by the plan in time order.

### Scheduler behaviors shown

- Sorting: the plan lists tasks by time regardless of the order they were added.
- Conflict warnings: two tasks at 06:45 for different pets trigger a warning.
- Time budget: tasks that would exceed the available minutes are left out of the plan.
- Filtering and recurrence: demonstrated in main.py and covered by the tests. The web UI does not yet have a button to mark a task complete, so recurrence is not triggered from the UI.

### Sample CLI output

Output from python main.py:

```text
Today's Schedule for Jordan (60 minutes available):
- 06:45 Morning medication (5 min, daily)
- 06:45 Feeding (10 min, daily)
- 08:00 Morning walk (25 min, daily)
- 12:00 Brush coat (10 min, weekly)

Schedule conflict warnings:
WARNING: Conflict at 06:45: Morning medication for Mochi, Feeding for Biscuit

All tasks sorted by time:
- 06:45 Morning medication (completed: False)
- 06:45 Feeding (completed: False)
- 07:00 Breakfast (completed: True)
- 08:00 Morning walk (completed: False)
- 12:00 Brush coat (completed: False)
- 16:00 Playtime (completed: False)

Pending tasks for Mochi:
- 08:00 Morning walk
- 06:45 Morning medication
- 12:00 Brush coat

Completed tasks:
- 07:00 Breakfast
```
