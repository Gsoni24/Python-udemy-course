import re

def extract_emails(text:str, unique_only: bool = True, case_sensitive: bool = True) -> list[str]:
    email_patter: str = (r'/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/')

    email: list[str] = re.findall(email_patter, text)

    if not case_sensitive:
        emails = [email.lower() for email in emails]

    if unique_only:
        emails = list(dict.fromkeys(emails))
    
    return emails

def list_emails(path: str) -> None:
    emails: list[str] = []

    with open(path, 'r') as f:
        text: str = f.read()
        emails = extract_emails(text)
    
    if emails:
        for email in emails:
            print(email)
    else:
        print("No emails were found")

def main() -> None:
    list_emails(path = "\Users\gaura\OneDrive\Desktop\vs-code-py\udemy\virtual\common_password.txt")

if __name__ == '__main__':
    main()

