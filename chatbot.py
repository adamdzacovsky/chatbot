import random

class Chatbot: 
    def __init__(self, name = "Chatbotv1"):
        self.name = name
    
    def greet(self):
        return f"Hi, my name is {self.name}"
    
    def tell_joke(self):
        jokes = ["This is the first joke", "This is the second joke", "This is the third joke"]
        return random.choice(jokes)
    
    def advice(self):
        advices = ["This is the first advice", "This is the second advice", "This is the third advice"]
        return random.choice(advices)
    
    def number(self, number):
        return f"{number} multiplied by 10 is {number * 10}"
    
    def respond(self,user_input):
        user_input = user_input.lower()

        if "hi" in user_input:
            return "Hi, welcome in the chat"
        elif "end" in user_input:
            return "Take care"
        elif "joke" in user_input:
            return self.tell_joke()
        elif "advice" in user_input or "advice" in user_input:
            return self.advice()
        elif "10" in user_input:
            return self.number(int(user_input))
        else:
            return "I can not understand this yet"
    
    def chat(self):
        print(self.greet())
        while True:
            user_input = input("You: ")
            response = self.respond(user_input)
            print(f"{self.name}: {response}")
            if "End" in user_input:
                break