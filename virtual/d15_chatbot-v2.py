from datetime import datetime

def contains(terms: list[str], content: str) -> bool:
    matches: list[bool] = []
    for term in terms:
        matches.append(term in content.lower())
    return any(matches)

# print(contains(['bob', 'hello'],'Hello, this is bob'))

class Chatbot():
    def __init__(self, name: str) -> None:
        self.name = name
        self.history: list[str] = []

    def response(self, text: str) -> str:
        text = text.lower()

        if contains(['tomorrow'], text) and contains(['weather'], self.history[-1]):
            return "Tomorrow looks Sunny."

        if contains(['hello', 'hi'], text):
            return "Hello There!"

        elif contains(['goodbye', 'bye'], text):
            return "Goodbye. Talk to you Later!"

        elif contains(['what is the time','current time'], text):
            return f"The current time is {datetime.now().strftime("%H:%M:%S")}"
            
        elif contains(['weather'], text):
            return "It's partly cloudy and 22 C right now."

        elif contains(['help', 'commands'], text):
            return "I understand: hello/hi,  goodbye/bye, what time is it/curren time, weather, tomorrow(after weather), and help/command"

        return "Sorry I can't Answer that right now"

    def remember (self, text: str) -> None:
        self.history.append(text.lower())
        if len(self.history) > 2:
            self.history.pop(0)

    def run(self, ) -> None:
        print("Type 'help' for commands. Type 'bye' to quit.\n")
        while True:
            user_input: str= input("You: ")
            bot_reply: str= self.response(user_input)
            print(f"{self.name}: {bot_reply}")

            if contains(['goodbye', 'bye'], user_input):
                break
            
            self.remember(user_input)

def main() -> None:
    bot: Chatbot = Chatbot('Bob')
    bot.run()

if __name__=='__main__':
    main() 

# Homework: Add two more follow questions