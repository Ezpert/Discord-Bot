import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message.lower() == 'roll':
        return str(random.randint(1, 6))
    if p_message.lower() == "cat":
        return 'cat.jpg'

    if p_message.lower() == 'hello':
        return 'Hey There!'

    if p_message.lower() == 'help':
        return 'This is help message that you can modify.'

    if p_message.lower() == 'robert':
        return 'Hello, my name is RobBot Thibodeaux I dont get girls and love "The Beatles"'



