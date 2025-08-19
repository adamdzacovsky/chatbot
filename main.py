class Chatbot: 
    def __init__(self, name = "Chatbotv1"):
        self.name = name
    
    def pozdrav(self):
        print("Zavolala sa funkcia pozdrav " + self.name)
        return f"Ahoj, moje meno je {self.name}"
        



bot = Chatbot("Bot1")




