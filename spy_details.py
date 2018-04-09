from datetime import datetime
class Spy:
    def __init__(self, Name, Salutation, Age, Rating):
        self.Name =  Salutation + " " +  Name

        self.Age = Age
        self.Rating = Rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

spy = Spy('Himanshuk','Mr.',21,1.4)


class ChatMessage:

  def __init__(self, message, sent_by_me):
     self.message = message
     self.time = datetime.now()
     self.sent_by_me = sent_by_me