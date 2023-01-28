from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["My name is Bot", "I am Bot, nice to meet you!"]
    ],
    [
        r"how are you?",
        ["I am doing good, How about You?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that!"]
    ],
    [
        r"quit",
        ["Bye bye take care. It was nice talking to you :) "]
    ],
]

def getReply(query):
    chat = Chat(pairs, reflections)
    return chat.respond(query)