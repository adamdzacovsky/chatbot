class Chatbot: 
    def __init__(self, name = "Chatbotv1"):
        self.name = name
    
    def pozdrav(self):
        return f"Ahoj, moje meno je {self.name}"
    
    def chat(self):
        print(self.pozdrav())
        



bot = Chatbot("Bot1")

bot.chat()



