class Move:

    def __init__(self, name, move_type, category, power, accuracy, pp, description):
        self.name = name
        self.type = move_type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "category": self.category,
            "power": self.power,
            "accuracy": self.accuracy,
            "pp": self.pp,
            "description": self.description,
        }
