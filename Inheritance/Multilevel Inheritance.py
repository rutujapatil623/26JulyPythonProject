# Multiple Inheritance takes place between 3 or more than 3 classes

class WhatsAppV1:

    def chat(self):
        print("WhatsApp has chatting feature")

class WhatsAppV2(WhatsAppV1):                # Inherit the members of WhatsAppV1 class

    def audioCall(self):
        print("WhatsApp has audio call feature")

class WhatsAppV3(WhatsAppV2):               # Inherit the members of WhatsAppV1 and WhatsAppV2 class

    def videoCall(self):
        print("WhatsApp has video call feature")


App = WhatsAppV3()

App.chat()

App.audioCall()

App.videoCall()
