from events import Events

class Document:
    def __init__(self, name):    
        self.name = name
        self.anevent = Events()
 
    def show(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'
 
class Word(Document):
    def show(self):
        return 'Show word contents!'


