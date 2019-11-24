from modules import general, language

""" ------------- Actions ------------- """


def add_action(target: dict, keyword: str, commands: tuple):
    """ Add action keyword to the {item} or Player
    Args:
        target: Target {item} or Player;
        keyword: Action word.
        commands: Tuple with acceptable commands
    Return:
        updated {item} objects
    """
    # Check that passed target is an {item} or {player}:
    if not (general.is_item(target) or general.is_player(target)):
        print(f'{target["name"]} is not an appropriate object. Only Items or Player can have actions')

    # Check that keyword is in command list:
    elif keyword not in commands:
        print(f'{keyword} is not an appropriate command')

    else:
        target['actions'].add(keyword)

        # Print info message:
        print(f'successfully added {keyword} action to {target["name"]}')

    return target


def remove_action(target: dict, keyword: str):
    """ Add action keyword to the {item} or Player
    Args:
        target: Target {item} or Player;
        keyword: Action word that needs to be removed.
    Return:
        updated {item} objects
    """
    # Check that passed target is an {item} or {player}:
    if not (general.is_item(target) or general.is_player(target)):
        print(f'{target["name"]} is not an appropriate object. Only Items or Player can have actions')

    # Check that keyword is in item actions:
    elif keyword not in target['actions']:
        print(f'{target["name"]} has no {keyword} action')

    else:
        target['actions'].remove(keyword)

        # Print info message:
        print(f'successfully removed {keyword} action from {target["name"]}')


""" ------------- Reactions ------------- """


def add_reaction(obj: dict, action: str, reaction, args: tuple = (), ind=None, commands: set = None):
    """ Add reaction for specified keyword to the {object}
    Args:
        obj: Target {object};
        action: Trigger action keyword;
        reaction: A function that should be executed;
        args: (optional) Arguments for the function;
        ind: (optional) Reaction index;
        commands: Set of acceptable actions
    Return:
        updated {item} objects
    """
    # If no set of acceptable command keywords was passed, use the default one:
    if commands is None:
        commands = language.create_vocabulary()

    # Check that passed target is an {item} object:
    if not general.is_object(obj):
        print(f"Error: {obj['name']} is not an object")

    # Check that keyword is in command list:
    elif action not in commands:
        print(f'{action} is not an appropriate command')

    else:
        # Check if there is list object exists for passed action and if not, create an empty one:
        obj['reactions'][action] = obj['reactions'].get(action, [])
        if ind is None:
            obj['reactions'][action].append((reaction, args))
            print(f"Reaction was successfully added into {obj['name']} for action: {action}")
        else:
            try:
                obj['reactions'][action].insert(ind, (reaction, args))
                print(f"Reaction was successfully added into {obj['name']} for action: {action}")

            except KeyError:
                print('Error: Incorrect index number')

    return obj


def remove_reaction(obj: dict, action: str, remove_all=False, reaction_ind=-1):
    """ Remove reaction for specified keyword from the {object}
    Args:
        obj: Target {object};
        action: Trigger action keyword;
        remove_all: (optional) If True, removes all reactions for specified action. False by default
        reaction_ind: If remove_all is set to False, remove only action from specified position (last by default).
    Return:
        updated {item} objects
    """
    if remove_all:
        try:
            del obj['reactions'][action]
            print(f"All reactions were successfully deleted for action: {action}")
        except KeyError:
            print(f'There is no reactions for such action: {action}')
    else:
        try:
            obj['reactions'][action].pop(reaction_ind)
            print(f"Reaction was successfully deleted for action: {action}")
        except KeyError:
            print(f'There is no such reaction index{reaction_ind}')

    return obj


def replace_reaction(obj: dict, action: str, reaction_ind, reaction_new, args: tuple = ()):
    """ Replace reaction for specified keyword for the {object}
    Args:
        obj: Target {object};
        action: Trigger action keyword;
        reaction_ind: Index of reaction that should be replaced;
        reaction_new: A new function that should be executed;
        args: (optional) Arguments for the function;.
    Return:
        updated {item} objects
    """
    try:
        obj['reactions'][action][reaction_ind] = (reaction_new, args)
        print(f"Reaction was successfully replaced in {obj['name']} for action: {action}")
    except KeyError:
        print(f'There is no such action: {action} or reaction index: {reaction_ind}')

    return obj


def print_reactions(obj: dict, action: str):
    """ Show all set reactions for specified action for {object}.
    Args:
        obj: Target {object};
        action: Trigger action keyword;
    """
    try:
        # Print list of existing functions:
        for i, reaction in enumerate(obj['reactions'][action]):
            print(f'Reaction #{i}: {reaction}')
    except KeyError:
        print(f'There is no reactions for such action: {action}')


def set_global_reactions(obj_group: dict, action: str, reaction, args: tuple = (), ind=0):
    """ Replace reaction for specified keyword for the {object}
    Args:
        obj_group: A group of target {object};
        action: Trigger action keyword;
        reaction: A function that should be executed;
        args: (optional) Arguments for the function;
        ind: Index of reaction that should be replaced.
    Return:
        updated group of {items}
    """
    try:
        for obj in obj_group.values():
            # Check that {item} object was passed:
            if general.is_object(obj):
                add_reaction(obj, action, reaction, args, ind)
    except KeyError:
        print('Failed to assign reaction to given object group')

    return obj_group
