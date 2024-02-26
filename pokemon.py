class Pokemon:

    def __init__(self, ndex_id, name, url, types, stats, types_charts, abilities, moves):
        self.ndex_id = ndex_id
        self.name = name
        self.url = url
        self.types = types
        self.stats = stats
        self.types_charts = types_charts
        self.abilities = abilities
        self.moves = moves

    def to_dict(self):
        return {
            "ndex_id": self.ndex_id,
            "name": self.name,
            "url": self.url,
            "types": self.types,
            "stats": self.stats,
            "types_charts": self.types_charts,
            "abilities": self.abilities,
            "moves": self.moves
        }
