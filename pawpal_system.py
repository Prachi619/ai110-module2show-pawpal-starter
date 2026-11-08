from dataclasses import dataclass, field


@dataclass
class Owner:
    name: str
    available_minutes: int
    preferences: list[str] = field(default_factory=list)

    def set_availability(self, minutes: int) -> None:
        raise NotImplementedError

    def update_preferences(self, preferences: list[str]) -> None:
        raise NotImplementedError


@dataclass
class Pet:
    name: str
    species: str
    care_needs: list[str] = field(default_factory=list)

    def update_details(self, name: str, species: str) -> None:
        raise NotImplementedError

    def get_care_requirements(self) -> list[str]:
        raise NotImplementedError


@dataclass
class CareTask:
    title: str
    duration_minutes: int
    priority: str

    def update_details(
        self,
        title: str,
        duration_minutes: int,
        priority: str,
    ) -> None:
        raise NotImplementedError

    def validate(self) -> bool:
        raise NotImplementedError


class Scheduler:
    def generate_plan(
        self,
        owner: Owner,
        pet: Pet,
        tasks: list[CareTask],
    ) -> list[CareTask]:
        raise NotImplementedError

    def explain_choices(self, tasks: list[CareTask]) -> list[str]:
        raise NotImplementedError
