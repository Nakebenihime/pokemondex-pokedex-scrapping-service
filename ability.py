class Ability:

    def __init__(self, name, description, introduced_generation):
        self.name = name
        self.description = description
        self.introduced_generation = introduced_generation

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "introduced_generation": self.introduced_generation,
        }
