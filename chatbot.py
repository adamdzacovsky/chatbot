import random
import requests
import wikipedia

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
    
    def number(self, number, multiplied_by):
        return f"{number} multiplied by {multiplied_by} is {number * multiplied_by}"
    
    def weather(self):
        city = input("Which city: ")
        url = f"https://wttr.in/{city}?format=%C+%t"
        response = requests.get(url)
        return response.text.strip()
    
    def wikipedia(self, keyword):
        return wikipedia.summary(keyword)
    
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
        elif user_input.isnumeric():
            multiplied_by = input("Enter a number: ")
            print("Vstup je cislo") 
            return self.number(int(user_input), int(multiplied_by))
        elif "weather" in user_input:
            return self.weather()
        elif "wik" in user_input:
            keyword = input("What do you want to search about: ")
            return self.wikipedia(keyword)
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