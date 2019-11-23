from modules import general


def create_place(name: str, description: str):
    """Create a new {place} object.
    Args:
        name: The name of the place to display in the game and to address in functions;
        description: Short description that would be displayed when player gets to the place.
    Return:
        {place} dictionary
    """
    place = {'category': 'place',
             'name': name,
             'description': description,
             'connections': {},
             'items': [],
             'objects': []}

    # Print info message:
    print(f'Successfully created place: {name}')

    return place


def get_dir_options(dir_options: dict = None):
    """Iterate over passed dict and return dist with attached reversed directions.
    Args:
        dir_options: Optional. Dict with one-way directions. If nothing is passed, uses {'South', 'North','East','West'}
    Returns:
        {directions} dictionary
    """
    if dir_options is None:
        dir_options = {'South': 'North', 'East': 'West'}

    directions = dir_options.copy()

    # Iterate over the passed dict and copy reversed directions into the result dict:
    for start, end in dir_options.items():
        directions[end] = start

    # Print info message:
    print(f'Directions were successfully created. Possible options are:')
    for start, end in directions.items():
        print(f'\t{start:>20} <---> {end:<20}')

    return directions


def connect_places(p1: dict, p2: dict, direction: str, dir_options: dict):
    """ Connect two places to each other. Simultaneously add opposite directions to both places.
    Args:
        p1: go from {place}
        p2: go to {place}
        direction: "direction"
        dir_options: dict with corresponding directions
    Returns:
        {p1}, {p2} place dictionaries with updated directions
    """
    # Check that both p1 and p2 are {place} objects:
    if not (general.is_place(p1) and general.is_place(p2)):
        print('Error:',
              f'\n\t{p1["name"]} is', 'not' * general.is_place(p1), 'a place',
              f'\n\t{p2["name"]} is', 'not' * general.is_place(p2), 'a place')

    # Create connection only if the direction is valid:
    elif direction not in dir_options:
        print(f'There is no such direction as {direction}')

    # Check that p1 has no previous connection in that direction:
    elif p1['connections'].get(direction, False):

        # If there is existing connection, print message and do not change it:
        print(f'{p1["name"]} is already connected in this direction to {p1["connections"].get(direction)["name"]}')

    # Check that p2 has no previous connection in opposite direction:
    elif p2['connections'].get(dir_options[direction], False):

        # If there is existing connection, print message and do not change it:
        print("{0} is already connected in opposite direction to {1}"
              .format(p2['name'], p2['connections'].get(dir_options[direction])['name']))

    else:
        # Create connection for both objects:
        p1['connections'][direction] = p2
        p2['connections'][dir_options[direction]] = p1

        # Print info message:
        print(f'Successfully created route: {p1["name"]:>20} <---> {p2["name"]:<20}')

    return p1, p2


def remove_connection(p1: dict, direction: str):
    """Removes connection to specified direction from both {start place} and {target place}.
    Args:
        p1: go from {place}
        direction: "direction"
    """
    # Get direction options:
    dir_options = get_dir_options()

    # Check that p1 has connection in specified direction:
    if p1['connections'].get(direction, False):

        # Save p2 name for info message:
        p2_name = p1['connections'][direction]['name']
        # Remove connections in both directions:
        del p1['connections'][direction]['connections'][dir_options[direction]]
        del p1['connections'][direction]

        # Print info message:
        print(f'Successfully deleted route: {p1["name"]:>20} <---> {p2_name:<20}')

    else:
        print(f'{p1["name"]} has no connection on {direction}')
