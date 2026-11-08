# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The design uses four classes: 
- Owner - stores the owner's name, available time, preferences, and pets
- Pet - stores a pet's name, species, care needs, and care tasks
CareTask - describes an activity with a title, duration, and priority
- Scheduler - builds a daily plan for a selected owner and pet and explains its choices.

3 core actions a user should be able to perform:
    - Add pet owner and details
    - Add or edit care tasks
    - Generate and view the day's care plan

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

A little bit of change was made. I saw that the Owner to Pet and Pet to CareTask relationships were drawn but not represented in the classes. I added a pets list to Owner and a tasks list to Pet. I also changed Scheduler.generate_plan to take the selected owner and pet rather than a separate task list, so it can get tasks from that pet instead of receiving duplicate or mismatched task data. A plan is generated for one selected pet at a time.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers three constraints: the owner's available minutes, each task's scheduled time, and whether a task is already completed. It walks pending tasks in time order and keeps each one that still fits the remaining minutes. I treated the time budget as the most important constraint because a plan that exceeds the owner's day is unusable, and scheduled time came second because pet care such as medication and feeding is tied to the clock. I did not implement priorities or preferences, so a long early task can use up time that a more important later task needed.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The conflict detector only flags tasks with the exact same start time; it does not check whether tasks with different start times overlap based on their durations. This keeps conflict detection simple and easy to explain, but a later improvement could compare the full time intervals. The AI assistant also suggested removing the sort of conflict times to avoid sorting, but I kept it because predictable, chronological warning output is more useful and readable. The task grouping is already a clear single pass, so the small sorting cost is reasonable.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to brainstorm the main classes, draft the UML, and build out the Python logic and terminal demo. The most useful prompts described the project requirements and asked for a design or implementation that matched them, especially the requirement to schedule tasks across multiple pets.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

The first design used a scheduler that planned for one selected pet. I did not keep that approach because the requirement was to manage tasks across all of an owner's pets. I changed the design so Owner.get_all_tasks() gathers tasks from every pet and the scheduler reads from that method. I also ran main.py to check the terminal demo.

**c. AI strategy**

- Which AI coding assistant features were most effective for building your scheduler?
- Give one example of an AI suggestion you rejected or modified to keep your system design clean.
- How did using separate chat sessions for different phases help you stay organized?

The most effective features were drafting the UML and class skeleton from the requirements, and drafting tests and docstrings for methods that already existed. Running the code after each change caught problems quickly.

One suggestion I modified was in conflict detection. The assistant proposed removing the sort of conflict times to save work. I kept it because chronological warnings are easier for a person to read, and the cost is small. I also rejected the first scheduler design that planned for one selected pet, because the requirement is to plan across all of an owner's pets.

I used three separate chat sessions: one for planning, one for implementing, and one for review. Planning covered the requirements, the classes, and the UML. Implementation covered writing the code and tests. Review covered checking the finished work, such as asking how an algorithm could be simplified. Keeping them apart meant each conversation stayed focused on one job. Design decisions were not buried in code discussions, and the review session looked at the code fresh instead of defending choices made while building it.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I picked five core behaviors to verify in tests test_pawpal.py (12 tests):
-  Sorting: tasks come back in chronological order, and tasks without a time go last.
- Recurrence: completing a daily task adds a pending copy due the next day, weekly adds 7 days, and non-recurring tasks do not repeat.
-  Conflict detection: tasks at the same time are flagged across pets, while different times and completed tasks are not.
-  Filtering: get_all_tasks filters by pet name and completion status.
-  Plan generation: the plan never exceeds the owner's available minutes.

I also covered edge cases: an empty task list, a pet with no tasks, an owner with no pets, and completing a task that does not belong to the pet. These matter because sorting, recurrence and conflicts are the features the daily plan depends on, and edge cases are where scheduling code usually breaks.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident (4 out of 5) because all 12 tests pass and cover the main paths. The gap is that conflicts only compare exact start times. Next I would test overlapping durations (for example 08:00 for 30 minutes and 08:15), invalid time strings, and a recurring task completed more than once.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied that the scheduling logic is small, readable and tested. Sorting, filtering, conflict warnings and recurrence each live in one clearly named method, and the README and UML name those same methods, so the documentation matches the code.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would add a "Mark complete" or emojis to the output so recurrence can be used from the UI, since right now it only runs through main.py and the tests. I would also make conflict detection compare full time intervals using each task's duration, and add task priorities so the plan can choose important tasks first when time is short. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

Being the lead architect means the AI proposes and I decide. The assistant was fast at producing code, but it could not know the requirements that mattered, such as planning across all pets. I had to set the design, check each suggestion against it, and verify with tests and by running the code. When the model and the code drifted apart, for example the UML missing due_date and complete_task, it was my job to notice and update the diagram. The AI makes building quicker, but responsibility for the design stays with me.
