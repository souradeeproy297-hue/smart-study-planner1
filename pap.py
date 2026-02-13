class StudyPlannerAgent:
    def __init__(self):
        self.subjects = {}

    def perceive(self):
        n = int(input("Enter number of subjects: "))
        for i in range(n):
            name = input(f"Subject {i+1} name: ")
            difficulty = input("Difficulty (easy/medium/hard): ").lower()
            self.subjects[name] = difficulty

    def decide(self, total_time):
        # Minimum hours per difficulty
        min_time = {"easy": 1, "medium": 2, "hard": 3}

        required_time = sum([min_time[diff] for diff in self.subjects.values()])

        # If given time is less than minimum required, return False
        if total_time < required_time:
            return False, required_time

        return True, required_time

    def act(self, can_study, required_time, total_time):
        if not can_study:
            print("\n❌ Study more!")
            print(f"Minimum required time: {required_time} hours")
            print(f"You entered: {total_time} hours")
        else:
            print("\n📘 Study Plan (Minimum Required):")
            min_time = {"easy": 1, "medium": 2, "hard": 3}
            for subject, diff in self.subjects.items():
                print(f"{subject}: {min_time[diff]} hours")

    def run(self):
        print("Smart Study Planner AI Agent")
        self.perceive()
        total_time = float(input("Total available study time (hours): "))
        can_study, required_time = self.decide(total_time)
        self.act(can_study, required_time, total_time)


agent = StudyPlannerAgent()
agent.run()