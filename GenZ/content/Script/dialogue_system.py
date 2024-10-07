import random

class Conversation:
    def __init__(self):
        self.history = []

    def add_utterance(self, speaker, utterance):
        self.history.append((speaker, utterance))

class DialogueSystem:
    def __init__(self):
        self.dialogue_trees = {
            "greeting": {
                "player": ["Hello", "Hi", "How are you?"],
                "npc": [
                    {"response": "Hello there!", "next_topics": ["introduce_self", "smalltalk"]},
                    {"response": "Busy.", "next_topics": ["end_conversation"]}
                ]
            },
            "introduce_self": {
                "player": ["What's your name?", "Who are you?"],
                "npc": [
                    {"response": "I'm {npc_name}, nice to meet you.", "next_topics": ["ask_occupation", "ask_location"]},
                    {"response": "That's not important right now.", "next_topics": ["ask_help"]}
                ]
            },
            "smalltalk": {
                "player": ["Nice weather we're having.", "How's business?"],
                "npc": [
                    {"response": "Indeed, it's a beautiful day.", "next_topics": ["ask_help", "end_conversation"]},
                    {"response": "Business could be better.", "next_topics": ["ask_help", "end_conversation"]}
                ]
            },
            "ask_help": {
                "player": ["Do you need any help?", "Is there something I can do for you?"],
                "npc": [
                    {"response": "Actually, yes. I have a quest for you.", "next_topics": ["accept_quest", "decline_quest"]},
                    {"response": "No, I'm fine. Thanks for asking.", "next_topics": ["end_conversation"]}
                ]
            },
            "end_conversation": {
                "player": ["Goodbye", "See you later"],
                "npc": [
                    {"response": "Farewell!", "next_topics": []},
                    {"response": "Until next time.", "next_topics": []}
                ]
            }
        }

    def generate_dialogue(self, character, topic, conversation, world_knowledge):
        if topic not in self.dialogue_trees:
            return "I don't have anything to say about that."

        options = self.dialogue_trees[topic]["npc"]
        response = random.choice(options)

        if isinstance(response, dict):
            dialogue = self._personalize_dialogue(response['response'], character)
            conversation.add_utterance(character.name, dialogue)
            return dialogue, response['next_topics']
        else:
            dialogue = self._personalize_dialogue(response, character)
            conversation.add_utterance(character.name, dialogue)
            return dialogue, []

    def _personalize_dialogue(self, dialogue, character):
        # Personalize dialogue based on character traits, emotional state, etc.
        if "arrogant" in character.personality['traits']:
            dialogue = dialogue.replace("nice to meet you", "you should be honored to meet me")
        elif "shy" in character.personality['traits']:
            dialogue = dialogue.replace("nice to meet you", "um... nice to meet you, I guess")

        # Replace placeholders with actual character information
        dialogue = dialogue.replace("{npc_name}", character.name)

        return dialogue

def run_conversation(dialogue_system, player, npc):
    conversation = Conversation()
    current_topic = "greeting"

    while current_topic != "end_conversation":
        # NPC's turn
        npc_response, next_topics = dialogue_system.generate_dialogue(npc, current_topic, conversation, {})
        print(f"{npc.name}: {npc_response}")

        if not next_topics:
            break

        # Player's turn
        print("\nChoose your response:")
        for i, topic in enumerate(next_topics, 1):
            print(f"{i}. {dialogue_system.dialogue_trees[topic]['player'][0]}")

        choice = int(input("Enter the number of your choice: ")) - 1
        chosen_topic = next_topics[choice]
        player_response = dialogue_system.dialogue_trees[chosen_topic]['player'][0]
        conversation.add_utterance(player.name, player_response)
        print(f"{player.name}: {player_response}")

        current_topic = chosen_topic

    print("Conversation ended.")

if __name__ == "__main__":
    from character_generator import generate_character, generate_npc

    dialogue_system = DialogueSystem()
    player = generate_character("Player", "Warrior")
    npc = generate_npc("merchant")

    run_conversation(dialogue_system, player, npc)
