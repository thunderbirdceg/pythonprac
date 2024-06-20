import string
import secrets


def contains_upper(password: str) -> bool:
    for letter in password:
        if letter.isupper():
            return True
    return False


def contains_symbol(password: str) -> bool:
    for letter in password:
        if letter in string.punctuation:
            return True
    return False


def get_password(length: int, upper: bool, symbols: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if upper:
        combination += string.ascii_uppercase

    if symbols:
        combination += string.punctuation
    combination_length = len(combination)
    password: str = ''
    for _ in range(length):
        password += combination[secrets.randbelow(combination_length)]

    return password

if __name__ in '__main__':
    for i in range(5):
        password =  get_password(length=15,upper=True,symbols=True)

        spec = f'U : {contains_upper(password)} S: {contains_symbol(password)}'

        print(f'{password} {spec}')
