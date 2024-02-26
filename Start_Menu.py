from Attestation.Functional import Functional
from Notes import Notes

class Start_menu():
    functional = Functional()
    notes = Notes()
    commands = {1: notes.add_note, 2: notes.manage_note_by_id, 3: notes.read_all_notes,
                  4: notes.save_notes_to_file}
    
    def begining(self):
        self.functional.start()
        while(True):
            self.functional.main_menu()
            choise = self.functional.input_number(len(self.commands.keys()), 'menu')
            if choise == 0:
                self.functional.exit()
                break
            else:
                self.commands[choise]()