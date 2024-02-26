from datetime import datetime

class Note:
    id = 0
    title = ""
    date = ""
    text = ""
    
    def set_id(self, value):
        self.id = value
    
    def set_title(self, title):
        self.title = title
    
    def set_text(self, text):
        self.text = text
    
    def update_date(self):
        self.date = datetime.now()
    
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_text(self):
        return self.text
    
    def get_date(self):
        return self.date