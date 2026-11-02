from datetime import datetime

def contains(terms: list[str], content: str) -> bool:
    matches: list[str] = []

    for term in terms:
        matches.append(term in content.lower())

    
    return any(matches)

def response(text: str)-> str:
    text = text.lower()

    if contains(['hello', 'hi'], text):
        return 'Hello There!'
    elif contains(['goodbye', 'bye'], text):
        return 'Talk to you later!'
    elif contains(['what time is it?', 'current time'], text):
        return f'The current time is {datetime.now()}'
    else:
        return "I can't answer that right now."


while True:
    user_input: str = input('You: ')
    print(f'Bot: {response(user_input)}')
