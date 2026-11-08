# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I used Claude Code in agent mode to build most of the app. I told it to write the Owner, Pet, Task and Scheduler classes from my UML. I told it the Scheduler had to get tasks from every pet through one Owner method called get_all_tasks(). Then I asked it to add sorting by time, filtering by pet and by done or not done, tasks that repeat daily or weekly, and a warning when two tasks are at the same time. I also asked it to update main.py, the tests and the README so they all matched the code.

**What did the agent do?**

- It read all the project files first before changing anything.
- It filled in the classes in pawpal_system.py.
- It added Owner.get_all_tasks() so I can filter tasks by pet name or by done status.
-  It added Scheduler.sort_by_time() so tasks show up in clock order and tasks with no time go last.
-  It added a way for a daily or weekly task to make a new copy of itself for the next day or week when it is marked done.
-  It added Scheduler.detect_conflicts(), which gives back a warning message instead of crashing.
-  It wrote the main.py demo with tasks added out of order and two tasks at the same time.
-  It wrote 12 tests

**What did you have to verify or fix manually?**

- The first scheduler only planned for one pet. That was wrong because the app has to handle all of the pets an owner has. I made it change the design so the Scheduler reads from Owner.get_all_tasks().
- The AI wanted to remove the sorting step in the conflict warnings. I kept it because warnings in time order are easier to read.
- The UML diagram was out of date. It was missing due_date and complete_task, so I fixed that myself.
- I read each test to make sure it actually checked something useful and was not just running the code.
- I ran main.py and the tests myself instead of just trusting what the AI said happened.

---

## Prompt Comparison (SF11)

> Compare two different prompts (or two different models) on the same task.

I tried two different prompts on the same job, which was building the scheduler. Both were in Claude Code. I only changed the prompt, not the tool.

| | Option A | Option B |
|-|----------|----------|
| Model  | Claude Code | Claude Code (new chat) |
| Prompt| A short, loose prompt: "Build a scheduler that makes a daily plan for a pet." | A detailed prompt: "Build a Scheduler that works across all the pets an owner has. It should get tasks from one Owner method, sort by HH:MM time, warn about tasks at the same time, and make a new task when a daily or weekly task is finished." |Response summary| It made a scheduler that planned for one chosen pet only. | It made a scheduler that reads all tasks from the owner and has sorting, conflict warnings, repeating tasks and plan building. |
| What was useful| It was fast and easy to read. | It matched what the project needed and was easy to test. |
| Problems notice | It missed the multiple pets rule. Tasks could also get mixed up when passed in separately. | It only catches tasks at the exact same start time. It does not catch tasks that overlap, and it has no priorities. |
| Decision | Rejected. | Kept. |

**Which approach did you use in your final implementation and why?**

I used Option B. When I told the AI exactly what the app had to do, the code fit my design and the project rules. The loose prompt gave me something that looked fine but left out an important rule. What worked best for me was giving clear details up front and then running the code and tests to check the answer.
# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---


