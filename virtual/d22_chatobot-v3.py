from dataclasses import dataclass
import json
import re

@dataclass
class Response:
    response:str 
    words: list[str]
    required_words: list[str]

def load_responses() -> list[Response]:
    responses: list[Response] = []
    with open('responses.json') as file:
        for response in json.load(file):
            responses.append(
                Response(
                    response['response'], 
                    response['words'],   
                    response['required_words']
                )
            )
    return responses

def split_text(text: str) -> list[str]:
    return re.split(r'\s+|[,;?!.-]\s*', text.lower())

# print(split_text('Loook out bob has a knif!!!')) test split_text

def match_rating(text:str, response: Response) -> float:
    text = text.lower()
    score:int = 0 
    has_required_words: bool = True
    
    for word in split_text(text):
        if word in response.words:
            score += 1

    percent_matched: float = score / (len(response.words))

    if response.required_words:
        for word in response .required_words:
            if word not in text:
                has_required_words = False
                break

    return percent_matched if has_required_words else 0


def get_response(text: str, responses: list[Response]) -> str:
    matches: dict[str, float] = {}

    for response in responses:
        matches[response.response] = match_rating(text, response)
#     print(matches)
# get_response('Hello, I am Bob', load_responses()) - to test out the the upper working
    best_match: str = max(matches, key=matches.get) # type: ignore
    return 'I don\'t understand... [0%]' if matches[best_match] == 0 else f'{best_match} [{matches[best_match]:.0%}]'

def main() -> None:
    responses: list[Response] = load_responses()

    while True:
        user_input: str = input('You: ')
        print(f'Bot: {get_response(user_input, responses)}')


if __name__ == '__main__':
    main()