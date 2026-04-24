class Transaction:
    def __init__(self):
        self.history = []

    def add(self, msg):
        self.history.append(msg)

    def statement(self):
        if not self.history:
            return "No transactions yet"
        return "\n".join(self.history)