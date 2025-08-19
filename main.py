import random

class Chatbot: 
    def __init__(self, name = "Chatbotv1"):
        self.name = name
    
    def greet(self):
        return f"Ahoj, moje meno je {self.name}"
    
    def tell_joke(self):
        jokes = ["toto je prvy joke", "toto je druhy joke", "toto je treti joke"]
        return random.choice(jokes)
    
    def advice(self):
        advices = ["toto je prva rada", "toto je druha rada", "toto je tretia rada"]
        return random.choice(advices)
    
    def respond(self,user_input):
        user_input = user_input.lower()

        if "ahoj" in user_input:
            return "ahoj vitaj v chate"
        elif "koniec" in user_input:
            return "maj sa pekne"
        elif "vtip" in user_input:
            return self.tell_joke()
        elif "rada" in user_input or "radu" in user_input:
            return self.advice()
        else:
            return "toto zataial nerozumiem"
    
    def chat(self):
        print(self.greet())
        while True:
            user_input = input("Ty: ")
            response = self.respond(user_input)
            print(f"{self.name}: {response}")
            if "koniec" in user_input:
                break


bot = Chatbot("Bot1")

bot.chat()



