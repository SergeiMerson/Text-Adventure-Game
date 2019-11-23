def is_place(obj: dict):
    """Checks that the passed object is a {place} instance.
    Args:
        obj: Object that should be checked.
    Return:
        True/False
    """
    return obj['category'] == 'place'


def is_player(obj: dict):
    """Checks that the passed object is a {player} instance.
    Args:
        obj: Object that should be checked.
    Return:
        True/False
    """
    return obj['category'] == 'player'


def is_item(obj: dict):
    """Checks that the passed object is a {item} instance.
    Args:
        obj: Object that should be checked.
    Return:
        True/False
    """
    return obj['category'] == 'item'


def is_object(obj: dict):
    """Checks that the passed object is a {object} instance.
    Args:
        obj: Object that should be checked.
    Return:
        True/False
    """
    return obj['category'] == 'object'


def describe(target):
    """Print {target} description according to the {target} category.
    Args:
        target: Object that should be described.
    """
    category, description = target['category'], target['description']

    if category == 'player':
        print(f"\nYou are looking in the mirror. {description}",
              "You put away the mirror and continue your jorney", sep='\n')

    elif category == 'item':
        print(f"\nYou are looking at {target['name']}: {description}")

    elif category == 'object':
        print(f"\nYou are looking at {target['name']}: {description}")

        # Check if there is any item in the object:
        if target['items']:
            print('You look closer, and find here', ', '.join([item['name'] for item in target['items']]))

    elif category == 'place':
        print(f"You get to {target['name']}.", description, "You look around:", sep='\n')
        for direction, destination in target['connections'].items():
            print(f"Road to {direction} leads to {destination['name']}.")

        # Check if there is any {object} in the {place}:
        if target['objects']:
            print('You look closer, and find here', ', '.join([item['name'] for item in target['objects']]))

        # Check if there is any item in the {place}:
        if target['items']:
            print('Also, you find here', ', '.join([item['name'] for item in target['items']]))

    else:
        print('There is nothing to look at...')