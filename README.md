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
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Terminal output from running `python main.py`:

```text
Today's Schedule for Jordan (60 minutes available):
- 06:45 Feeding (10 min, daily)
- 08:00 Morning walk (25 min, daily)
- 12:00 Brush coat (10 min, weekly)
- 16:00 Playtime (15 min, daily)
```

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
# Paste your pytest output here
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.sort_by_time() | Orders tasks by theirHH:MM scheduled time; tasks without a time appear last. |
| Filtering | Owner.get_all_tasks() | Optional completion-status and pet-name filters. |
| Conflict handling | Scheduler.detect_conflicts()| Returns warnings when pending tasks for any pets share an HH:MM start time. |
| Recurring tasks | Scheduler.complete_task, Task.next_occurrence() | Completing a daily or weekly task marks it done and adds a fresh pending copy to the same pet; other frequencies (e.g. once) do not recur. |
| Plan generation | Scheduler.generate_plan() | Walks tasks in time order and keeps pending ones that fit the owner's remaining minutes. |



## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
