class Chatbot: 
    def __init__(self, name = "Chatbotv1"):
        self.name = name
    
    def greet(self):
        return f"Ahoj, moje meno je {self.name}"
    
    def respond(self,user_input):
        user_input = user_input.lower()

        if "ahoj" in user_input:
            return "ahoj vitaj v chate"
        elif "koniec" in user_input:
            return "maj sa pekne"
        else:
            return "toto zataial nerozumiem"
    
    def chat(self):
        print(self.greet())
        



bot = Chatbot("Bot1")

bot.chat()



