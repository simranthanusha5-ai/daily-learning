"""Day 159: Command Pattern with Undo/Redo."""

class Command:
    def execute(self): pass
    def undo(self): pass

class AppendTextCommand(Command):
    def __init__(self, doc, text):
        self.doc = doc
        self.text = text

    def execute(self):
        self.doc.append(self.text)

    def undo(self):
        self.doc.pop()

class HistoryManager:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def execute(self, cmd):
        cmd.execute()
        self.history.append(cmd)
        self.redo_stack.clear()

    def undo(self):
        if self.history:
            cmd = self.history.pop()
            cmd.undo()
            self.redo_stack.append(cmd)

if __name__ == "__main__":
    doc = []
    mgr = HistoryManager()
    mgr.execute(AppendTextCommand(doc, "Hello"))
    assert doc == ["Hello"]
    mgr.undo()
    assert doc == []
    print("Day 159 Command Pattern tests passed!")
