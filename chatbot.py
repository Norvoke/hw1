import re
from typing import List


class ChatBot:
    def __init__(self):
        """
        Initializes the gnomebot with memory for previous responses.
        """
        self.user_name = "friend"

    def make_reply(self, text: str) -> str:
        """
        Processes user input with regex and returns a whimsical response.
        """
        # get user’s name
        name_match = re.search(r"my name is (\w+)", text, re.IGNORECASE)
        if name_match:
            self.user_name = name_match.group(1)
            return f"Ah-ha! A pleasure to meet ye, {self.user_name}! What brings ye to me garden?"

        # greeting
        if re.search(r"\b(hello|hi|greetings|hey)\b", text, re.IGNORECASE):
            return f"Ahoy there, {self.user_name}! Fancy a mushroom riddle?"
        
        # farewell
        if re.search(r"\b(bye|farewell|goodbye|see ya)\b", text, re.IGNORECASE):
            return f"May the moss be ever soft beneath yer toes, {self.user_name}!"
        
        # questions about gnomes
        if re.search(r"\b(what|who) are you\b", text, re.IGNORECASE):
            return "I be Gnorman the Gnome! Keeper of riddles and protector of enchanted turnips!"
        
        # find numbers in a sentence (for counting mushrooms, flowers or snails ofc)
        number_match = re.search(r"(\d+) (mushrooms|flowers|snails)", text, re.IGNORECASE)
        if number_match:
            count, item = number_match.groups()
            return f"Oh ho! {count} {item}, ye say? A fine collection indeed! But can ye find one more hidden under the toadstool?"

        # mention treasure!!
        if re.search(r"\btreasure\b", text, re.IGNORECASE):
            return "Treasure ye seek? Ah, but the real treasure be friendship... and a good compost pile!"

        # backup
        return "Oh ho! That be a curious thing to say! But tell me, have ye ever spoken to a talking mushroom?"
    
    @staticmethod
    def get_name() -> str:
        """
        Returns the chatbot's name.
        """
        return "Gnorman the Gnome"

    @staticmethod
    def examples() -> List[str]:
        """
        Provides example interactions.
        """
        return [
            "hello",
            "my name is Finn",
            "do you know any riddles?",
            "I found 5 mushrooms!",
            "what are you?",
            "goodbye"
        ]


def get_user_statement() -> str:
    """
    Get user input and normalize it.
    """
    return input("you: ").strip()


def main():
    bot = ChatBot()
    print(f"You're chatting with {bot.get_name()}!")
    you_said = get_user_statement()
    while you_said.lower().strip() != "exit":
        if you_said == "examples":
            print("Examples: ", bot.examples())
        else:
            bot_said = bot.make_reply(you_said)
            print("bot: " + bot_said)
        you_said = get_user_statement()
    print("Bye!")


if __name__ == "__main__":
    main()
