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

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
