from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    duration_minutes: int
    frequency: str
    completed: bool = False

    def validate(self) -> bool:
        """Return whether the task has valid required details."""
        return (
            bool(self.description.strip())
            and self.duration_minutes > 0
            and bool(self.frequency.strip())
        )

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
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

    def get_all_tasks(self) -> list[Task]:
        """Return the tasks belonging to all of this owner's pets."""
        return [task for pet in self.pets for task in pet.tasks]


class Scheduler:
    def generate_plan(self, owner: Owner) -> list[Task]:
        """Return pending tasks that fit within the owner's available time."""
        planned_tasks: list[Task] = []
        remaining_minutes = owner.available_minutes

        for task in owner.get_all_tasks():
            if task.completed:
                continue
            if not task.validate():
                raise ValueError(f"Invalid task: {task.description!r}")
            if task.duration_minutes <= remaining_minutes:
                planned_tasks.append(task)
                remaining_minutes -= task.duration_minutes

        return planned_tasks
