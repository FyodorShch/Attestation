class Functional:
    
    def start(self):
        print("Start of the work")
    
    def main_menu(self):
        print("Choose an option: \n"
              "\t0. Exit from app\n"
              "\t1. Add a note \n"
              "\t2. Read/Change text of/Delete note\n"
              "\t3. Show all notes\n"
              "\t4. Save all notes\n")
     
    def note_menu(self):
         print("Choose an option: \n"
               "\t1. Read a note"
               "\t2. Change text of note"
               "\t3. Delete note")

    def error(self):
        print("Write correct number.")
    
    def not_found(self):
        print("There no number found. Try again.")
        
    def save_complete(self):
        print("All notes saved")
        
    def show_note(self, note):
        result = f"ID: {str(note.get_id())}|\t"
        result += f"Date: [{str(note.get_date())}]\t"
        result += f"Name: [{str(note.get_title())}]\n"
        result += f"{str(note.get_text())}\n"
        print(result)
    
    def all_notes(self, count):
        result = "\tAll notes\n" \
        f"Notes found: {count}\n"
        print(result)
    
    def info_msg(self, key):
        info = {'add': 'added', 'del': 'deleted', 'change': 'changed'}
        print(f"Note succesfuly {info[key]}!")
    
    def input_note_title(self):
        return input("Write a title of note:")

    def input_note_text(self):
        return input("Text of note:")
    
    def edit_note(self, note):
        note.set_text(self.input_note_text())
        note.update_date()
        self.info_msg('edit')
    
    def input_number(self, limit, preset):
        presets = {'id': 'notes', 'menu': "menu's point"}
        value = 0
        while True:
            try:
                value = int(input(f"Input number of {presets[preset]}: "))
            except ValueError:
                self.error()
                continue
            if 0 <= value <= limit:
                break
            else:
                self.not_found()
        return value    
    
    def exit(self):
        print("Exit of work")
    