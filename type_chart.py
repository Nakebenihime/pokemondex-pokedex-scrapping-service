class PokemonTypeChart:

    def __init__(self):
        self.types_generations = {
            6: [
                'normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying',
                'psychic',
                'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy'
            ],
            2: [
                'normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying',
                'psychic',
                'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel'
            ],
            1: [
                'normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying',
                'psychic',
                'bug', 'rock', 'ghost', 'dragon'
            ]}

        self.type_effectiveness_generations = {
            6: {
                "normal": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],
                "fire": [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],
                "water": [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1],
                "electric": [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],
                "grass": [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1],
                "ice": [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],
                "fighting": [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5],
                "poison": [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2],
                "ground": [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1],
                "flying": [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1],
                "psychic": [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1],
                "bug": [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5],
                "rock": [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1],
                "ghost": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1],
                "dragon": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0],
                "dark": [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5],
                "steel": [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2],
                "fairy": [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1]
            },
            2: {
                "normal": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5],
                "fire": [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2],
                "water": [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1],
                "electric": [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1],
                "grass": [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5],
                "ice": [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5],
                "fighting": [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2],
                "poison": [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0],
                "ground": [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2],
                "flying": [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5],
                "psychic": [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5],
                "bug": [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5],
                "rock": [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5],
                "ghost": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 0.5, 0.5],
                "dragon": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5],
                "dark": [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 0.5],
                "steel": [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5]

            },
            1: {
                "normal": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1],
                "fire": [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5],
                "water": [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5],
                "electric": [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5],
                "grass": [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5],
                "ice": [1, 1, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2],
                "fighting": [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1],
                "poison": [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 2, 0.5, 0.5, 1],
                "ground": [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1],
                "flying": [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1],
                "psychic": [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1],
                "bug": [1, 0.5, 1, 1, 2, 1, 0.5, 2, 1, 0.5, 2, 1, 1, 0.5, 1],
                "rock": [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1],
                "ghost": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1],
                "dragon": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],

            }
        }

    def check_invalid_number_of_types(self, in_types):
        if not (1 <= len(in_types) <= 2):
            raise ValueError("Specify a minimum of 1 type and maximum of 2 types")

    def check_valid_types(self, in_types):
        types_across_gen = set(t for types in self.types_generations.values() for t in types)
        invalid_types = [t.lower() for t in in_types if t.lower() not in types_across_gen]

        if invalid_types:
            raise ValueError(f"The types: {invalid_types} are not recognized as valid types.")

    def check_unavailable_types_by_gen(self, in_types):
        unavailable_types_by_gen = {}
        for gen, type_effectiveness in self.type_effectiveness_generations.items():
            unavailable_types_by_gen[gen] = [t.lower() for t in in_types if t.lower() not in type_effectiveness]

        return unavailable_types_by_gen

    def get_pokemon_type_chart(self, in_types):
        self.check_invalid_number_of_types(in_types)
        self.check_valid_types(in_types)

        unavailable_types_by_gen = self.check_unavailable_types_by_gen(in_types)

        charts = []
        for gen, pk_types in self.types_generations.items():
            unavailable_types = unavailable_types_by_gen.get(gen, [])

            if unavailable_types:
                continue

            type_effectiveness = self.type_effectiveness_generations[gen]

            pk_attacking_chart_type = [type_effectiveness[t] for t in in_types]

            pk_type_effectiveness_transposed = {
                k: list(v) for k, v in zip(type_effectiveness, zip(*type_effectiveness.values()))
            }
            pk_defending_chart_type = [pk_type_effectiveness_transposed[t] for t in in_types]

            if len(in_types) == 2:
                final_atk_chart = [x * y for x, y in zip(pk_attacking_chart_type[0], pk_attacking_chart_type[1])]
                final_def_chart = [x * y for x, y in zip(pk_defending_chart_type[0], pk_defending_chart_type[1])]
            else:
                final_atk_chart = pk_attacking_chart_type[0]
                final_def_chart = pk_defending_chart_type[0]

            charts.append({
                'generation': gen,
                'attack': dict(zip(pk_types, final_atk_chart)),
                'defense': dict(zip(pk_types, final_def_chart))
            })

        return charts
