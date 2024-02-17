from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    print(lowered)
    # TODO - replace with you own logic
    if lowered == "":
        return "Well, you'r awafully silent"
    elif "hello" in lowered:
        return "Hello there! Whut u want?"
    elif "time " in lowered:
        return "Have a guess bboừ bbbbbbb"
    elif "idk" in lowered:
        return "IDK either hehe"
    elif "bye" in lowered:
        return "Go cry"
    else: 
        return choice([" Bla bla bla",
                       "Olalalalalala",
                       "I'm hungry too hic hic"])

