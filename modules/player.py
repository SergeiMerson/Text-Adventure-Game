from modules import general, language


def create(name: str = 'Player', description: str = '', location: dict = None):
    """Create a {player} object.
    Args:
        name: The Player's name. Default is "Player";
        description: (optional) Short description of the Player;
        location: (optional) If provided, place Player to specified location
    Return:
        {player} dictionary with following fields:
        - name;
        - description;
        - location:
        - items: list of items in Player's inventory;
        - abilities: a set of default actions that Player can take no mater of what items does he/she have;
        - actions: set of actions that available to Player: combination of his/her abilities and items actions;
    """
    # Check that location was provided, if not, make it empty dict:
    location = {} if location is None else location

    # Create {player} object:
    player = {'category': 'player',
              'name': name,
              'description': description,
              'location': location,
              'items': [],
              'abilities': set(),
              'actions': set()}

    # Print info message:
    print(f'{name} was successfully created')

    return player


def set_abilities(player: dict, abilities: set, commands: set = None):
    """Update set of abilities available to Player.
    Args:
        player: {player} object;
        abilities: set of actions that would be available to Player by default;
        commands: a set of acceptable command keywords.
    Return:
        Updated {player} object
    """
    # If no set of acceptable command keywords was passed, use the default one:
    if commands is None:
        commands = language.create_vocabulary()

    # Check that {player} object was passed:
    if not general.is_player(player):
        print(f'{player["name"]} is not an appropriate object.')

    # Check that all actions in abilities are acceptable commands:
    elif not abilities.issubset(commands):
        print(f"Following actions are unknown: {', '.join(abilities.difference(commands))}")
    else:
        player['abilities'] = abilities

        # Print info message:
        print(f"{player}\'s abilities were set successfully")

    return player


def update_actions(player: dict):
    """Update set of actions available to Player.
    Args:
        player: {player} object;
    Return:
        Updated {player} object
    """
    # Check that {player} object was passed:
    if general.is_player(player):
        # Get a set of actions provided by items in inventory:
        inv_actions = set()
        for item in player['items']:
            inv_actions.update(item['actions'])

        # Set Player's actions as union of inv_actions and abilities:
        player['actions'] = player['abilities'].union(inv_actions)

    else:
        print(f'{player["name"]} is not an appropriate object.')

    return player


def pickup_item(player: dict, item: dict, place: dict):
    """Move {item} from it current location and place it in Player's Inventory.
    Args:
        player: {player} object;
        item: {item} to be moved;
        place: {place} where {item} is located now
    Return:
        Updated {player}, {item} and {place} objects
    """
    # Check that {player} and {item} objects was passed and that:
    if not (general.is_player(player) and general.is_item(item) and general.is_place(place)):
        print(f'{player["name"]}, {item["name"]} or {place["name"]} is not an appropriate object.')

    # Check if the {item} is located in {place}:
    elif item.get('location') == place:
        # Remove {item} from its current location:
        place['items'].remove(item)

        # Move the {item} to Inventory:
        item['location'] = player
        player['items'].append(item)

        # Update player's actions:
        player = update_actions(player)

    else:
        print(f"There is no {item['name']} in {place['name']}")

    return player, item, place


def drop_item(player: dict, item: dict, place: dict):
    """Move {item} from Player's Inventory to a specified location.
    Args:
        player: {player} object;
        item: {item} to be moved;
        place: {place} where {item} should be placed
    Return:
        Updated {player}, {item} and {place} objects
    """
    # Check that {player} and {item} objects was passed and that:
    if not (general.is_player(player) and general.is_item(item) and general.is_place(place)):
        print(f'{player["name"]}, {item["name"]} or {place["name"]} is not an appropriate object.')

    else:
        # Remove {item} from Inventory:
        player['items'].remove(item)

        # Move the {item} to Inventory:
        item['location'] = place
        place['items'].append(item)

        # Update player's actions:
        player = update_actions(player)

        print(f"You have dropped {item['name']} in {place['name']}")

    return player, item, place


def transit(player: dict, direction: str):
    """Move {player} to another {place}.
    Args:
        player: {player} object;
        direction: where player should go.
    Return:
        Updated {player} objects
    """
    # Check that the passed direction does exist in current player's location:
    if direction in player['location']['connections']:
        # Move Player to a new place:
        player['location'] = player['location']['connections'][direction]
        print(f"You arrived to {player['location']['name']}.")
        general.describe(player['location'])

    pass


def apply_action(player: dict, obj: dict, action: str):
    """Execute reactions for specified action trigger word.
    Args:
        player: {player} object;
        obj: object that launch reactions;
        action: trigger action word.
    Return:
        Updated {player} objects
    """
    # Check that proper {object} was passed and specified action is available and can launch reaction:
    if general.is_object(obj) and (action in player['actions']) and (action in obj['reactions']):
        try:
            for reaction in obj['reactions'][action]:
                func = reaction[0]
                args = reaction[1]
                if len(args) == 0:
                    func()
                else:
                    func(*args)
        except KeyError:
            print(f"You've tried to {action}, but nothing has happen...")
