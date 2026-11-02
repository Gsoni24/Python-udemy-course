import string

class PasswordValidator:
    def __init__(self) -> None:
        self.common_password: set[str] = self.load_common_password()

    @staticmethod
    def load_common_password() -> set[str]:
        with open('common_password.txt', 'r') as file:
            return {line.strip() for line in file if line}


    def is_common(self, password: str) -> bool:
        return password in self.common_password

    def rate(self, password: str) -> str:
        if self.is_common(password):
            return 'poor'

        score: int = 0
        if any (c.isupper() for c in password):
            score += 1
        
        if any (c in string.punctuation for c in password):
            score += 1

        if len(password) >= 10:
            score += 1

        if score == 3:
            return 'secure'
        elif score == 2:
            return 'medium'
        else:
            return 'poor'



def main() -> None:
    validator: PasswordValidator = PasswordValidator()
    print('🔒 Welcome to the Password Strength Checker!')
    print('Enter a password to get a quality rating.')

    while True:
        password: str = input('Enter the password: ').strip()
        rating: str = validator.rate(password)
        if rating == 'secure':
            print('✅ Your password is secure! ')    
        elif rating == 'medium':
            print('⚠️ Your password is medium strength ')    
        else:
            print('⚠️ Your password sucks! ')
            print('💡 Try adding symbols, uppercase letters, and increasing the length')    

if __name__ == "__main__":
    main()

# homemwork list
# 1.Add funcitonality that tells the user exactly what they are missing to make their password stronger,
# such as symbols, uppercase characters, and/or more characters
# 2. Add funcitionality that detects when a user adds too many sequential characters, such as
# "aaa", "111" or so on.ab
# 3. Check if the password contains digits as well to reach the "secure" rating