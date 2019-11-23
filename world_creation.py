from modules import places, player, objects, language, general


def create_world():
    # Create dict to store the World objects:
    world = {'player': {}, 'places': {}, 'objects': {}, 'items': {}}

    """ ---------------------- Create Map ----------------------- """

    world['places'] = {

        'Lookout Point': places.create_place(
            'Lookout Point',
            'The highest point of Monkey Island'),

        'The Scumm Bar': places.create_place(
            'The Scumm Bar',
            'Dirty old bar full of pirates waiting for a next opportunity to get out of this place'),

        'Kitchen': places.create_place(
            'Kitchen',
            'A place more suitable for graveyard that for cooking'),

        'Circus': places.create_place(
            'Circus',
            'The sign at the entrance tells "Welcome to the Fettuccini Brother\'s Circus, ' +
            'the only place where you can be really fired"'),

        'Voodoo Lady\'s Den': places.create_place(
            'Voodoo Lady\'s Den', 'The strangest place you have ever seen in your life full of different voodoo stuff '),

        'Victory': places.create_place(
            'Victory', 'Congratulation! You win! Just a test location))')
    }

    """ ---------------------- Connect Map ---------------------- """
    # Get default directions:
    dir_options = places.get_dir_options()

    # Connect several nodes:
    places.connect_places(
        world['places']['Lookout Point'],
        world['places']['The Scumm Bar'],
        'South', dir_options)

    places.connect_places(
        world['places']['The Scumm Bar'],
        world['places']['Kitchen'],
        'West', dir_options)

    places.connect_places(
        world['places']['The Scumm Bar'],
        world['places']['Circus'],
        'East', dir_options)

    places.connect_places(
        world['places']['Circus'],
        world['places']['Voodoo Lady\'s Den'],
        'North', dir_options)

    places.connect_places(
        world['places']['Voodoo Lady\'s Den'],
        world['places']['Lookout Point'],
        'West', dir_options)

    """ --------------------- Create Player --------------------- """

    world['player'] = player.create(
        'Guybrush Threepwood',
        "I'm Guybrush Threepwood and I want to be a mighty pirate")

    return world
