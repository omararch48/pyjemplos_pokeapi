import click
import requests
import os


def show_abilities(abilities):
    """
        Esta funcion es usada para generar un string que liste las habilidades
    """
    abilities_str = ''
    for ability in abilities:
        abilities_str += f"\n\t\t      * {ability['ability']['name']}"
    return abilities_str


def show_forms(forms):
    """
        Esta funcion es usada para generar un string que liste las formas
    """
    forms_str = ''
    for form in forms:
        forms_str += f"\n\t\t      * {form['name']}"
    return forms_str


def show_pokemon(pokemon):
    """
        Esta funcion retorna un string con los datos del pokemon con formato
        para la consola
    """
    return f'''
    Pokemon:          {pokemon['name']}\n
    id:               {pokemon['id']}\n
    abilities:        {show_abilities(pokemon['abilities'])}\n
    base_experience:  {pokemon['base_experience']}\n
    forms:            {show_forms(pokemon['forms'])}\n
    '''


api_url = 'https://pokeapi.co/api/v2/pokemon' # url base de la api de pokemon


@click.command()
@click.option(
    '-p',
    '--pokemon',
    default = '',
    help='Buscar por nombre o número del pokemon'
)
@click.option(
    '-j',
    '--json',
    is_flag=True,
    help='Muestra el resultado en formato JSON'
)
def pokedex(pokemon, json):
    """
        La funcion esta decorada para poder ejecutar la aplicacion como una cli
        usando la opcion --pokemon para buscar desde la linea de comandos y 
        la opcion --json para visualizar el resultado en una linea con formato
        json, esta funcion usa el modulo click tanto en los decoradores como
        para presentar los resultados
    """
    # Este condicional se ejecuta si no se recibe ningun arguemento junto con
    # la opcion --pokemon o -p
    if pokemon == '':
        pokemon = click.prompt('Buscar pokemon por nombre o número')
    # Se consulta la api
    pokemon_response = requests.get(f'{api_url}/{pokemon}')
    # Una validacion muy simple 
    if pokemon_response.status_code > 399:
        click.echo(f'Ha ocurrido un error: {pokemon_response.status_code}')
        return
    # Esta condicional se ejecuta si se provee de la opcion --json o -j
    if json:
        click.echo(pokemon_response.text)
        return 
    click.echo(f'Buscando al pokemon {pokemon}...')
    click.echo(show_pokemon(pokemon_response.json()))


if __name__ == '__main__':
    # Limpiar pantalla
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    pokedex()