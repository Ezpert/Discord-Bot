import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message.startswith('roll'):
        p_message = p_message.split()
        if len(p_message) > 1 and p_message[1].isdigit():
            die_size = int(p_message[1])
            return str(random.randint(1, die_size))
        else:
            return str(random.randint(1, 6))

    if p_message.lower() == 'never back down never what?':
        return 'NEVER GIVE UP!'

    if p_message.lower() == 'hello':
        return 'Hey There!'

    if p_message.lower() == 'help':
        return 'This is help message that you can modify.'

    if p_message.lower() == 'robert':
        return 'Hello, my name is RobBot Thibodeaux I dont get girls and love "The Beatles"'