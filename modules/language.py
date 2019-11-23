def create_vocabulary(voc: dict = None):
    """Create vocabulary from passed dictionary.
    Args:
        voc: A dictionary of command (as a str): synonyms (as a list)
    Return:
        commands: set with acceptable commands
        inv_voc: inverted dictionary where each synonym added as a key and corresponding command as its value.
    """
    # If no dictionary was passed, create a default one:
    if voc is None:
        voc = {'take': ['get', 'pick up'],
               'go': ['follow', 'run'],
               'use': ['apply']}

    # Save acceptable commands in a tuple:
    commands = set(voc)

    # Create empty dict to store invented key:value pairs:
    inv_voc = {}

    # Invent original dict and store results in the new one:
    for key, val in voc.items():
        inv_voc = {**inv_voc, **{v: key for v in val}}  # unpacks two dicts and joins them
        inv_voc[key] = key  # if it wasn't specified in synonyms, add command as its own synonym

    return commands, inv_voc


def interpret_user_phrase():
    pass
