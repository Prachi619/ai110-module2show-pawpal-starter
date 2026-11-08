from pawpal_system import Owner, Pet, Scheduler, Task


owner = Owner(name="Jordan", available_minutes=60)

dog = Pet(name="Mochi", species="dog")
dog.add_task(Task("Morning walk", 25, "daily", time="08:00"))
dog.add_task(Task("Morning medication", 5, "daily", time="06:45"))
breakfast = Task("Breakfast", 10, "daily", time="07:00")
breakfast.mark_complete()
dog.add_task(breakfast)
dog.add_task(Task("Brush coat", 10, "weekly", time="12:00"))

cat = Pet(name="Biscuit", species="cat")
cat.add_task(Task("Feeding", 10, "daily", time="06:45"))
cat.add_task(Task("Playtime", 15, "daily", time="16:00"))

owner.add_pet(dog)
owner.add_pet(cat)

schedule = Scheduler().generate_plan(owner)

print(f"Today's Schedule for {owner.name} ({owner.available_minutes} minutes available):")
for task in schedule:
    print(
        f"- {task.time} {task.description} "
        f"({task.duration_minutes} min, {task.frequency})"
    )

scheduler = Scheduler()
print("\nSchedule conflict warnings:")
conflicts = scheduler.detect_conflicts(owner)
if conflicts:
    for warning in conflicts:
        print(f"WARNING: {warning}")
else:
    print("No schedule conflicts.")

print("\nAll tasks sorted by time:")
for task in scheduler.sort_by_time(owner.get_all_tasks()):
    print(f"- {task.time} {task.description} (completed: {task.completed})")

print("\nPending tasks for Mochi:")
for task in owner.get_all_tasks(completed=False, pet_name="Mochi"):
    print(f"- {task.time} {task.description}")

print("\nCompleted tasks:")
for task in owner.get_all_tasks(completed=True):
    print(f"- {task.time} {task.description}")
