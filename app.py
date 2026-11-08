from datetime import time

import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_minutes=60)

st.title("🐾 PawPal+")

st.markdown(
    """
Plan care tasks for all of your pets, based on the time you have available.
"""
)

st.divider()

owner = st.session_state.owner
st.subheader(f"Plan for {owner.name}")
available_minutes = st.number_input(
    "Time available today (minutes)",
    min_value=0,
    max_value=1440,
    value=owner.available_minutes,
)
owner.set_availability(int(available_minutes))

st.subheader("Pets")
with st.form("add_pet_form", clear_on_submit=True):
    pet_name = st.text_input("Pet name")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    add_pet_submitted = st.form_submit_button("Add pet")

if add_pet_submitted:
    if not pet_name.strip():
        st.error("Enter a name for the pet.")
    else:
        owner.add_pet(Pet(name=pet_name.strip(), species=species))

if owner.pets:
    st.write("Your pets:")
    st.write(", ".join(f"{pet.name} ({pet.species})" for pet in owner.pets))
else:
    st.info("Add a pet to start planning care tasks.")

st.subheader("Care tasks")
if owner.pets:
    pet_index = st.selectbox(
        "Choose a pet",
        options=range(len(owner.pets)),
        format_func=lambda index: owner.pets[index].name,
    )
    selected_pet = owner.pets[pet_index]

    with st.form("add_task_form", clear_on_submit=True):
        task_description = st.text_input("Task description")
        duration = st.number_input(
            "Duration (minutes)", min_value=1, max_value=240, value=20
        )
        scheduled_time = st.time_input("Scheduled time", value=time(9, 0))
        frequency = st.selectbox(
            "Frequency", ["daily", "weekly", "as needed"]
        )
        add_task_submitted = st.form_submit_button("Add task")

    if add_task_submitted:
        if not task_description.strip():
            st.error("Enter a description for the task.")
        else:
            selected_pet.add_task(
                Task(
                    description=task_description.strip(),
                    duration_minutes=int(duration),
                    frequency=frequency,
                    time=scheduled_time.strftime("%H:%M"),
                )
            )

    for pet in owner.pets:
        if pet.tasks:
            st.markdown(f"**{pet.name}'s tasks**")
            st.table(
                [
                    {
                        "Task": task.description,
                        "Time": task.time or "Not set",
                        "Duration (min)": task.duration_minutes,
                        "Frequency": task.frequency,
                        "Completed": task.completed,
                    }
                    for task in pet.tasks
                ]
            )
        else:
            st.caption(f"No tasks added for {pet.name} yet.")
else:
    st.caption("Add a pet before adding its care tasks.")

st.divider()

st.subheader("Today's Schedule")
if st.button("Generate schedule"):
    scheduler = Scheduler()
    for warning in scheduler.detect_conflicts(owner):
        st.warning(warning)

    plan = scheduler.generate_plan(owner)
    if plan:
        for task in plan:
            pet_name = next(
                pet.name for pet in owner.pets if task in pet.tasks
            )
            st.write(
                f"- {task.time or 'Time not set'} {task.description} for {pet_name} "
                f"({task.duration_minutes} min, {task.frequency})"
            )
    else:
        st.info("No pending tasks fit within the available time.")
