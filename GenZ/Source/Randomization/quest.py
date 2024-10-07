class Quest:
    def __init__(self, name, description, reward):
        self.name = name
        self.description = description
        self.reward = reward
        self.is_completed = False

    def complete_quest(self):
        self.is_completed = True
        print(f"Quest '{self.name}' completed! Reward: {self.reward}")

class QuestLog:
    def __init__(self):
        self.active_quests = []
        self.completed_quests = []

    def add_quest(self, quest):
        self.active_quests.append(quest)
        print(f"New quest added: {quest.name}")

    def complete_quest(self, quest_name):
        for quest in self.active_quests:
            if quest.name == quest_name:
                quest.complete_quest()
                self.active_quests.remove(quest)
                self.completed_quests.append(quest)
                return
        print(f"Quest '{quest_name}' not found in active quests.")

    def display_quests(self):
        print("Active Quests:")
        for quest in self.active_quests:
            print(f"- {quest.name}: {quest.description}")
        print("Completed Quests:")
        for quest in self.completed_quests:
            print(f"- {quest.name}")
