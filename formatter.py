from typing import Final

VERSION: Final[str] = '1.0'

def format_text(title: str) -> str:
    words: list[str] = []
    for word in title.split():
        words.append(word.capitalize())

    return ' '.join(words)

if __name__ == '__main__':
    print(format_text("Harry Potter and the goblet of fire"))
    