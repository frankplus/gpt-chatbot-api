from collections import deque

class Conversation:
    """Simple Conversation class with two users, their nicks and the messages so
    far. This is dumb but enough for the purpose of this mini bot. It can output
    the conversation with double newlines for GPT-2 to take as input, add
    replies, and that's about it. """

    def __init__(self, gpt, name_human = "You", name_computer = "Me"):
        self.gpt = gpt
        self.name_human = name_human
        self.name_computer = name_computer
        self.conversation = deque()

        self.add_human("Nice to meet you. What's your name?")
        self.add_computer("My name is Pete.")
        self.add_human("That's an interesting name. How old are you?")
        self.add_computer("I'm 40 years old.")
        self.add_human("Can you tell me something about yourself?")
        self.add_computer("Ofcourse! I like playing video games and eating cake.")

    def add(self, name, text):
        self.conversation.append("{}: \"{}\"".format(name, text))
        if len(self.conversation) > 6:
            self.conversation.popleft()

    def add_computer(self, text):
        self.add(self.name_computer, text)

    def add_human(self, text):
        self.add(self.name_human, text)

    def text_generic(self, nspace = 1):
        output = ""
        for reply in self.conversation:
            output = output + (reply + ("\n" * nspace))
        return output

    def text_gpt(self):
        return self.text_generic(2)

    def get_answer(self):
        prompt = self.text_gpt() + "{}: \"".format(self.name_computer)
        print("INPUT " + "="*30)
        print(prompt)
        print("INPUT " + "="*30)
        text = self.gpt.generate_conditional(prompt)
        reply = (text.strip().split('\n'))[0]
        if reply[-1] == "\"":
            reply = reply[:-1]
        return reply
