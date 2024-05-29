class FilmProject:
    def __init__(self, title, budget):
        self.title = title
        self.budget = budget
        self.cast_members = []
        self.shooting_schedule = {}
    def add_cast_member(self, name, role):
        self.cast_members.append({"name": name, "role": role})
    def set_shooting_schedule(self, day_schedule):
        self.shooting_schedule = day_schedule
    def update_budget(self, amount):
        self.budget -= amount
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Budget: {self.budget}")
        print("Cast Members:")
        for member in self.cast_members:
            print(f"{member['name']} ({member['role']})")
        print("Shooting Schedule:")
        for day, schedule in self.shooting_schedule.items():
            print(f"{day}: {schedule}")
class CastMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
