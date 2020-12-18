import datetime


class Note:
    def __init__(self, content=None):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%y %H:%M:%S')

    def find(self, word):
        if word in self.content:
            return True
        else:
            return False

    def find_2(self, word):
        if word.lower() in self.content.lower():
            return True
        else:
            return False


note1 = Note()
note2 = Note('My first note')
print(note1.__dict__)
print(note2.__dict__)
print(note2.find('my'))
print(note2.find_2('NotE'))


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, content):
        self.notes.append(Note(content))

    def display_notes(self):
        for note in self.notes:
            print(f'{note.creation_time}:{note.content}')

    def search(self, word):
        return [note for note in self.notes if note.find_2(word)]





notebook = Notebook()
notebook.new_note('My first note.')
notebook.new_note('My second note.')
print(notebook.notes)
notebook.display_notes()
print(notebook.search('note'))