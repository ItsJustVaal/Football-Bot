# import the requires modules
import helpers
import imports as imp

# Command Functions
# Instead of using the traditional bot.commands from discord
# I am just writing functions that return an embed to the bot


# Show all daily scores using API, this is a big maybe
def scores():
    return


# Report Scores, was thinking about automating this with an API or something
def report():
    return


# Show Standings
def standings():
    return


# Set fixtures
def setfx(*items):
    # Fixture gropup check and keys
    fixture_groups = ['1', '2', '3']
    keys = ['Left1',
            'Right1',
            'Left2',
            'Right2',
            'Left3',
            'Right3',
            'Left4',
            'Right4']

    # opens Json
    with open("jsons/matches.json") as matches:
        data = imp.json.load(matches)

        # check if empty
        if data is None:
            data = {}
    # make iterator for fixtures
    fixtures = iter(items[0][2:])

    # make sure there is enough fixtures entered
    if len(items[0][2:]) < len(keys):
        embed = helpers.makeEmbed(
            'Nope try again with the correct number of fixtures', 2)
        return embed

    # Fixture check
    if items[0][1] not in fixture_groups:
        embed = helpers.makeEmbed(
            'Pick 1, 2, or 3 you nerd', 2)
        return embed

    # set fixtures
    if items[0][1] == '1':
        data['FirstSet'] = {key: next(fixtures) for key in keys}

        with open("jsons/matches.json", "w+") as matches:
            matches.write(imp.json.dumps(data))
    elif items[0][1] == '2':
        data['SecondSet'] = {key: next(fixtures) for key in keys}

        with open("jsons/matches.json", "w+") as matches:
            matches.write(imp.json.dumps(data))
    elif items[0][1] == '3':
        data['ThirdSet'] = {key: next(fixtures) for key in keys}

        with open("jsons/matches.json", "w+") as matches:
            matches.write(imp.json.dumps(data))

    # make and return embed
    embed = helpers.makeEmbed(f'Fixtures Group {items[0][1]} Set', 2)
    return embed


# Shows user preds
def mypred(items):
    embed = helpers.makeEmbed(str(items), 4)
    return embed


# Lock Preds
def lock(items):
    with open("jsons/member.json", 'r', encoding='utf-8') as members:
        data = imp.json.load(members)
    data['locked'] = 1
    with open("jsons/member.json", 'w', encoding='utf-8') as members:
        members.write(imp.json.dumps(data))
    embed = helpers.makeEmbed('Locked', 2)
    return embed


# unlock preds
def unlock(items):
    with open("jsons/member.json", 'r', encoding='utf-8') as members:
        data = imp.json.load(members)
    data['locked'] = 0
    with open("jsons/member.json", 'w', encoding='utf-8') as members:
        imp.json.dump(data, members)
    embed = helpers.makeEmbed('Unlocked', 2)
    return embed


# Help users
def help(items):
    embed = helpers.makeEmbed('-- HELP CENTER --', 2)
    embed.add_field(
        name='.join', value='Join in on the CL/EL predictions betting to win (or lose) titles!', inline=False)
    embed.add_field(name='.fixtures',
                    value='See the current games to bet on!', inline=False)
    embed.add_field(name='.pred',
                    value='Give your predictions to the games depending on the group. For example to give your predictions on the games in group 1 you do: .pred 20 31 40 00', inline=False)
    embed.add_field(name='.standings',
                    value='Shows overall standings for those who predict matches', inline=False)
    embed.add_field(
        name='.fab', value="Show Fab's latest tweets", inline=False)
    return embed


# predictions
def predict(*items):

    # opens members file
    with open("jsons/member.json", encoding='utf-8') as members:
        data = imp.json.load(members)
    if data['locked'] == 1:
        embed = helpers.makeEmbed("Locked you derp lole loser", 2)
        return embed
    # sets all variables and keys
    username = str(items[1])
    keys = data[username].keys()
    group_one, group_two, group_three = [], [], []
    for key in keys:
        if key.startswith('one'):
            group_one.append(key)
        elif key.startswith('two'):
            group_two.append(key)
        elif key.startswith('three'):
            group_three.append(key)
    fixture_groups = ['1', '2', '3']
    initial = [x.split('-') for x in items[0][2:]]
    preds = [int(item) for items in initial for item in items]
    preds_iter = iter(preds)

    # checks
    if data[username]['isPlaying'] != 1:
        embed = helpers.makeEmbed(
            'You need to .join first nerd', 2)
        return embed

    if items[0][1] not in fixture_groups:
        embed = helpers.makeEmbed(
            'Not a fixture group. Syntax: .predict 1 1-1 2-2 3-3 4-4', 2)
        return embed

    if len(preds) != 8:
        embed = helpers.makeEmbed(
            'Not enough predictions. Syntax: .predict 1 1-1 2-2 3-3 4-4', 2)
        return embed

    for x in items[0][2:]:
        if '-' not in x:
            embed = helpers.makeEmbed(
                'Must have a - between scores. Syntax: .predict 1 1-1 2-2 3-3 4-4', 2)
            return embed

    # group 1 pred
    if items[0][1] == '1':
        for x in group_one:
            data[username][f'{x}'] = next(preds_iter)
        with open("jsons/member.json", "w", encoding='utf-8') as members:
            members.write(imp.json.dumps(data))

    # group 2 pred
    if items[0][1] == '2':
        for x in group_two:
            data[username][f'{x}'] = next(preds_iter)
        with open("jsons/member.json", "w", encoding='utf-8') as members:
            members.write(imp.json.dumps(data))

    # group 3 pred
    if items[0][1] == '3':
        for x in group_three:
            data[username][f'{x}'] = next(preds_iter)
        with open("jsons/member.json", "w", encoding='utf-8') as members:
            members.write(imp.json.dumps(data))

    embed = helpers.makeEmbed(
        f'Your prediction for group {items[0][1]} is set, use .mypred to check', 2)
    return embed


# Gets Fabs latest tweets and formats them
def fab(items):
    return


# Shows current Fixtures
def fixtures(items):
    embed = helpers.makeEmbed('Fixtures: ', 1)
    return embed


# Resets Fixtures
def resetfx(items):
    with open("jsons/matches.json", "r") as matches:
        data = imp.json.load(matches)

        keys = data['FirstSet'].keys()
        sets = data.keys()
    for set in sets:
        for key in keys:
            data[set][key] = ''

    with open("jsons/matches.json", "w") as matches:
        imp.json.dump(data, matches)
    embed = helpers.makeEmbed('Fixtures Reset To:', 1)
    return embed


# Test lole
def test(items):
    embed = helpers.makeEmbed(' ', 3)
    return embed
