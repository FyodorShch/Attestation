import json
from Note import Note
from Attestation.Functional import Functional

class Notes:
    notes = []
    functional = Functional()
    index = 0
    indexes = []
    
    def create_file(self):
        try:
            with open('notes.csv', 'rb') as file:
                self.notes = json.load(file)
                self.index = len(self.notes)
            with open('indexes.csv', 'rb') as file:
                self.indexes = json.load(file)
        except EOFError:
            self.notes = []
            self.functional = Functional()
            self.index = 0
            self.indexes = []
                
    def add_note(self):
        note = Note()
        note.set_title(self.functional.input_note_title())
        note.set_text(self.functional.input_note_text())
        note.update_date()
        if len(self.indexes) == 0:
            note.set_id(self.index)
        else:
            note.set_id(self.indexes.pop())
        self.notes.append(note)
        self.index = len(self.notes)
        self.functional.info_msg('add')
        
    def delete_note(self, note):
        self.indexes.append(note.get_id())
        self.notes.remove(note)
        if len(self.notes) == 0:
            self.indexes.clear()
        self.functional.info_msg('del')
        
    def read_all_notes(self):
        self.functional.all_notes(len(self.notes))
        for note in self.notes:
            self.functional.show_note(note)
    
    def manage_note_by_id(self):
        commands =  {1: self.functional.show_note,
                     2: self.functional.edit_note,
                     3: self.delete_note}
        flag = False
        self.functional.note_menu()
        choice = self.functional.input_number(len(commands.keys()), 'menu')
        value = self.functional.input_number(self.index, 'id')
        for note in self.notes:
            if note.get_id() == value:
                commands[choice](note)
                flag = True
        if not flag:
            self.functional.not_found()
    
    def save_notes_to_file(self):
        with open('notes.json', 'wb') as file:
            json.dump(self.notes, fp= file)
        with open('indexes.csv', 'wb') as file:
            json.dump(self.indexes, fp= file)
        self.functional.saved_info()