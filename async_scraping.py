import asyncio
import time

import aiohttp
from bs4 import BeautifulSoup

from ability import Ability
from mongodb_handler import MongoDBHandler
from move import Move
from pokemon import Pokemon
from type_chart import PokemonTypeChart


async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except aiohttp.ClientError as e:
        print(f'Failed to fetch {url} with the following: {e}')
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


def parse_moves_basic_info(row):
    columns = row.find_all('td')
    move_name = columns[0].find('a').get_text()
    move_type = columns[1].find('a').get_text().lower() if columns[1].find('a') is not None else None
    move_category = None if columns[2]['data-sort-value'].strip() in ['—', ''] else columns[2]['data-sort-value']
    move_power = None if columns[3].get_text().strip() == '—' else int(columns[3].get_text())
    move_accuracy = None if columns[4].get_text().strip() in ['—', '∞'] else int(columns[4].get_text())
    move_pp = None if columns[5].get_text() == '—' else int(columns[5].get_text())
    move_description = columns[6].get_text()
    path_to_resource = columns[0].find('a')['href'].split('/')[-1]

    return {
        'name': move_name,
        'type': move_type,
        'category': move_category,
        'power': move_power,
        'accuracy': move_accuracy,
        'pp': move_pp,
        'description': move_description,
        'path_to_resource': path_to_resource
    }


def parse_abilities_basic_info(row):
    columns = row.find_all('td')
    ability_name = columns[0].find('a').get_text()
    ability_description = columns[2].get_text()
    ability_introduced_generation = int(columns[3].get_text())
    path_to_resource = columns[0].find('a')['href'].split('/')[-1]

    return {
        'name': ability_name,
        'description': ability_description,
        'introduced_generation': ability_introduced_generation,
        'path_to_resource': path_to_resource
    }


def parse_pokemon_stats_info(row):
    columns = row.find_all('td')
    ndex_id = int(columns[0]['data-sort-value'])
    name = columns[1].find('a').get_text()
    name = f'{name} ({columns[1].find("small").get_text()})' if columns[1].find('small') else name

    types = [a.get_text().lower() for a in columns[2].find_all('a')]

    stats = [int(td.get_text()) for td in columns[4:10]]
    hp, attack, defense, spattack, spdefense, speed = stats
    total = sum(stats)
    path_to_resource = columns[1].find('a')['href'].split('/')[-1]

    types_charts = PokemonTypeChart().get_pokemon_type_chart(types)

    return {
        'ndex_id': ndex_id,
        'name': name,
        'types': types,
        'hp': hp,
        'attack': attack,
        'defense': defense,
        'spattack': spattack,
        'spdefense': spdefense,
        'speed': speed,
        'total': total,
        'types_charts': types_charts,
        'path_to_resource': path_to_resource
    }


def parse_pokemon_moves_info(row):
    columns = row.find_all('td')
    move_learned_at = int(columns[0].get_text())
    move_name = columns[1].find('a').get_text()

    return {
        'learned_at': move_learned_at,
        'name': move_name
    }


def parse_pokemon_abilities_info(row):
    ability_name = row.get_text()
    ability_description = row.get('title', '')
    hidden_ability = '(hidden ability)' in row.next_sibling.strip() if row.next_sibling is not None else False

    return {
        'name': ability_name,
        'description': ability_description,
        'hidden': hidden_ability
    }


def find_href_value(soup, name):
    active_tab_panel = soup.find('div', class_='sv-tabs-tab-list')
    if active_tab_panel:
        for a in active_tab_panel.find_all('a', class_='sv-tabs-tab'):
            if name == a.get_text():
                return a['href'].split('#')[-1]
    return None


async def scrape_pk_moves_and_abilities(session, url, name):
    response = await fetch_url(session, url)
    if response is None:
        return []

    soup = BeautifulSoup(response, 'lxml')

    href_tab = find_href_value(soup, name.split('(', 1)[-1].split(')', 1)[0].strip())
    pk_abilities = soup.find('div', class_='sv-tabs-panel', id=href_tab).find('th', string='Abilities').find_next('td')
    pk_moves = soup.find_all('main')[0].find('table', {'class': 'data-table'}).find('tbody').find_all('tr')

    abilities_info = [parse_pokemon_abilities_info(row) for row in pk_abilities.find_all('a')]
    moves_info = [parse_pokemon_moves_info(row) for row in pk_moves]

    return abilities_info, moves_info


async def scrape_pk_table(session, url):
    response = await fetch_url(session, url)
    if response is None:
        return []

    soup = BeautifulSoup(response, 'lxml')
    pk_table = soup.find('table', id='pokedex').find('tbody').find_all('tr')

    return [parse_pokemon_stats_info(row) for row in pk_table]


async def scrape_moves_table(session, url):
    response = await fetch_url(session, url)
    if response is None:
        return []

    soup = BeautifulSoup(response, 'lxml')
    move_table = soup.find('table', id='moves').find('tbody').find_all('tr')

    return [parse_moves_basic_info(row) for row in move_table]


async def scrape_abilities_table(session, url):
    response = await fetch_url(session, url)
    if response is None:
        return []

    soup = BeautifulSoup(response, 'lxml')
    ability_table = soup.find('table', id='abilities').find('tbody').find_all('tr')

    return [parse_abilities_basic_info(row) for row in ability_table]


def create_pokemon_object(pokemon_obj, abilities_info, moves_info):
    return Pokemon(
        ndex_id=pokemon_obj['ndex_id'],
        name=pokemon_obj['name'],
        url=f'https://s3..../',
        types=pokemon_obj['types'],
        stats={
            'hp': pokemon_obj['hp'],
            'attack': pokemon_obj['attack'],
            'defense': pokemon_obj['defense'],
            'spattack': pokemon_obj['spattack'],
            'spdefense': pokemon_obj['spdefense'],
            'speed': pokemon_obj['speed'],
            'total': pokemon_obj['total']
        },
        types_charts=pokemon_obj['types_charts'],
        abilities=abilities_info,
        moves=moves_info
    )


def create_move_object(move_obj):
    return Move(
        name=move_obj['name'],
        move_type=move_obj['type'],
        category=move_obj['category'],
        power=move_obj['power'],
        accuracy=move_obj['accuracy'],
        pp=move_obj['pp'],
        description=move_obj['description']
    )


def create_ability_object(ability_obj):
    return Ability(
        name=ability_obj['name'],
        description=ability_obj['description'],
        introduced_generation=ability_obj['introduced_generation']
    )


async def main():
    start_time = time.time()
    print(f'Starting scraping...')
    async with aiohttp.ClientSession() as session:
        req_pokemons = await scrape_pk_table(session, 'https://pokemondb.net/pokedex/all')
        req_pokemons_tasks = [scrape_pk_moves_and_abilities(session, f'https://pokemondb.net/pokedex/{pk["path_to_resource"]}', pk['name']) for pk in
                              req_pokemons]
        req_pokemons_tasks_results = await asyncio.gather(*req_pokemons_tasks)

        req_moves = await scrape_moves_table(session, 'https://pokemondb.net/move/all')
        req_abilities = await scrape_abilities_table(session, 'https://pokemondb.net/ability')

    pokemons = [create_pokemon_object(pk, abilities, moves).to_dict() for pk, (abilities, moves) in zip(req_pokemons, req_pokemons_tasks_results)]

    abilities = [create_ability_object(ability).to_dict() for ability in req_abilities]

    moves = [create_move_object(move).to_dict() for move in req_moves]

    time_difference = time.time() - start_time
    print(f'Scraping time: {time_difference:.2f} seconds.')

    print(f'Starting saving...')
    mongo_handler = MongoDBHandler('mongodb://localhost:27017', 'pokemondex')

    try:
        mongo_handler.connect()
        mongo_handler.insert_many('pokemons', pokemons)
        mongo_handler.insert_many('moves', moves)
        mongo_handler.insert_many('abilities', abilities)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        mongo_handler.close_connection()

    time_difference = time.time() - start_time
    print(f'Saving time: {time_difference:.2f} seconds.')


if __name__ == '__main__':
    asyncio.run(main())
