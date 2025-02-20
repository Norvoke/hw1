import re
from typing import List


class ChatBot:
    def make_reply(self, text: str) -> str:
        """
        The method where you do your regular expression work!

        Args:
            text (str): the text of the message sent

        Returns:
            str: the chatbot's response
        """
        raise NotImplementedError

    @staticmethod
    def get_name() -> str:
        """
        Gets the name of your chatbot
        This will be used in the web interface

        Returns:
            str: the name of your chatbot
        """
        raise NotImplementedError

    @staticmethod
    def examples() -> List[str]:
        """
        Gets some examples of how your chatbot should be run

        Returns:
            List[str]: _description_
        """
        raise NotImplementedError


def get_user_statement() -> str:
    """
    Get user input and normalizes it by stripping whitespace and
    converting to lowercase

    Returns:
        str: normalized string from standard input
    """
    return input("you: ").lower().strip()


def main():
    bot = ChatBot()

    print(f"You're chatting with {bot.get_name()}")
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

# Discover NLP course materials authored by Julie Medero, Xanda Schofield, and Richard Wicentowski
# This work is licensed under a Creative Commons Attribution-ShareAlike 2.0 Generic License# https://creativecommons.org/licenses/by-sa/2.0/