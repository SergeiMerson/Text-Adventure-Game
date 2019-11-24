from modules import places, player, objects, language, general


def create_world():
    # Create dict to store the World objects:
    world = {'player': {}, 'places': {}, 'objects': {}, 'items': {}}

    """ ----------------------------------------------- Create Map ------------------------------------------------ """
    # Create a list of tuples with places and its descriptions:
    place_set = [
        ('Lookout Point', 'The highest point of Monkey Island'),
        ('The Scumm Bar', 'Dirty old bar full of pirates waiting for a next opportunity to get out of this place'),
        ('Kitchen', 'A place more suitable for graveyard that for cooking'),
        ('Circus', 'The sign at the entrance tells "Welcome to the Fettuccini Brother\'s Circus, ' +
         'the only place where you can be really fired"'),
        ('Voodoo Lady\'s Den', 'The strangest place you have ever seen in your life full of different voodoo stuff '),
        ('Victory', 'Congratulation! You win! Just a test location))')
    ]

    # Iterate over this list and add each place to the world dict:
    for location, description in place_set:
        world['places'][location] = places.create_place(name=location, description=description)

    """ ----------------------------------------------- Connect Map ----------------------------------------------- """
    # Get default directions:
    dir_options = places.get_dir_options()

    # Create a list of tuples with places that need to be connected ({start from , {direction to}, {destination}):
    direction_set = [
        ('Lookout Point',       'South',    'The Scumm Bar'),
        ('The Scumm Bar',       'West',     'Kitchen'),
        ('The Scumm Bar',       'East',     'Circus'),
        ('Circus',              'North',    'Voodoo Lady\'s Den'),
        ('Voodoo Lady\'s Den',  'West',     'Lookout Point')
    ]

    # Iterate over this list and connect locations in appropriate direction:
    for start, direction, end in direction_set:
        places.connect_places(
            start=world['places'][start], direction=direction, end=world['places'][end], dir_options=dir_options
        )

    """ ---------------------------------------------- Create Player ---------------------------------------------- """
    # Add a player to the world dict:
    world['player'] = player.create(
        name='Guybrush Threepwood',
        description="I'm Guybrush Threepwood and I want to be a mighty pirate",
        location=world['places']['Lookout Point']
    )

    """ ---------------------------------------------- Create Items ----------------------------------------------- """

    return world


world = create_world()
print({i for i in world['player']['location']['connections']})
