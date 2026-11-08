from __future__ import annotations

import re
from datetime import date, timedelta
from dataclasses import dataclass, field, replace

RECURRING_FREQUENCIES = {"daily": 1, "weekly": 7}  # frequency -> days until next


@dataclass
class Task:
    """A single pet care activity with duration, frequency and optional HH:MM time."""

    description: str
    duration_minutes: int
    frequency: str
    completed: bool = False
    time: str | None = None
    due_date: date | None = None

    def validate(self) -> bool:
        """Return whether the task has valid required details."""
        return (
            bool(self.description.strip())
            and self.duration_minutes > 0
            and bool(self.frequency.strip())
            and (
                self.time is None
                or bool(re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", self.time))
            )
        )

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def next_occurrence(self) -> Task | None:
        """Return a fresh pending copy of this task if it recurs, else None.

        Only "daily" (+1 day) and "weekly" (+7 days) recur (case-insensitive);
        any other frequency (e.g. "once") yields None. The new due date is
        counted from this task's due_date, or from today if it has none.
        """
        if self.frequency.strip().casefold() not in RECURRING_FREQUENCIES:
            return None
        interval = RECURRING_FREQUENCIES[self.frequency.strip().casefold()]
        base_date = self.due_date or date.today()
        return replace(
            self, completed=False, due_date=base_date + timedelta(days=interval)
        )


@dataclass
class Pet:
    """A pet and the care tasks assigned to it."""

    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Validate and add a task to this pet."""
        if not task.validate():
            raise ValueError("Task must have a description, positive duration, and frequency.")
        self.tasks.append(task)


@dataclass
class Owner:
    """A pet owner with a daily time budget and one or more pets."""

    name: str
    available_minutes: int
    pets: list[Pet] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate the initial available time."""
        self.set_availability(self.available_minutes)

    def set_availability(self, minutes: int) -> None:
        """Set available time, rejecting negative values."""
        if minutes < 0:
            raise ValueError("Available minutes cannot be negative.")
        self.available_minutes = minutes

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's care list."""
        self.pets.append(pet)

    def get_all_tasks(
        self, *, completed: bool | None = None, pet_name: str | None = None
    ) -> list[Task]:
        """Return owner tasks, optionally filtered by completion and pet name."""
        selected_pet_name = (
            pet_name.strip().casefold() if pet_name is not None else None
        )
        return [
            task
            for pet in self.pets
            if selected_pet_name is None or pet.name.casefold() == selected_pet_name
            for task in pet.tasks
            if completed is None or task.completed is completed
        ]


class Scheduler:
    """Sorts, checks and plans pet care tasks across all of an owner's pets."""

    def complete_task(self, pet: Pet, task: Task) -> Task | None:
        """Mark a task complete and, if it recurs, add a new pending copy to the pet.

        Returns the newly created task, or None for non-recurring tasks.
        Raises ValueError if the task does not belong to the pet.
        """
        if task not in pet.tasks:
            raise ValueError(f"{task.description!r} is not a task for {pet.name}.")
        task.mark_complete()
        next_task = task.next_occurrence()
        if next_task is not None:
            pet.add_task(next_task)
        return next_task

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Return tasks in clock-time order, placing tasks without a time last."""
        return sorted(
            tasks,
            key=lambda task: (task.time is None, task.time or ""),
        )

    def detect_conflicts(self, owner: Owner) -> list[str]:
        """Return warnings for pending tasks scheduled at the same time."""
        tasks_by_time: dict[str, list[tuple[str, str]]] = {}
        for pet in owner.pets:
            for task in pet.tasks:
                if task.completed or task.time is None:
                    continue
                tasks_by_time.setdefault(task.time, []).append(
                    (pet.name, task.description)
                )

        return [
            f"Conflict at {scheduled_time}: "
            + ", ".join(
                f"{description} for {pet_name}"
                for pet_name, description in scheduled_tasks
            )
            for scheduled_time, scheduled_tasks in sorted(tasks_by_time.items())
            if len(scheduled_tasks) > 1
        ]

    def generate_plan(self, owner: Owner) -> list[Task]:
        """Return pending tasks that fit within the owner's available time."""
        planned_tasks: list[Task] = []
        remaining_minutes = owner.available_minutes

        for task in self.sort_by_time(owner.get_all_tasks()):
            if task.completed:
                continue
            if not task.validate():
                raise ValueError(f"Invalid task: {task.description!r}")
            if task.duration_minutes <= remaining_minutes:
                planned_tasks.append(task)
                remaining_minutes -= task.duration_minutes

        return planned_tasks
