# import the requires modules
import helpers


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
def setfx():
    return


# Shows user preds
def mypred():
    return


# Lock Preds
def lock():
    return


# Help users
def help():
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
def pred():
    return


# Gets Fabs latest tweets and formats them
def fab():
    return


# Shows current Fixtures
def fixtures():
    embed = helpers.makeEmbed('Fixtures: ', 1)
    return embed


# Resets Fixtures
def resetfx():
    with open("jsons/matches.json", "r") as matches:
        data = imports.json.load(matches)

        keys = data['FirstSet'].keys()
        sets = data.keys()
    for set in sets:
        for key in keys:
            data[set][key] = ''

    with open("jsons/matches.json", "w") as matches:
        imports.json.dump(data, matches)
    embed = helpers.makeEmbed('Fixtures Reset To:', 1)
    return embed


# Test lole
def test():
    embed = helpers.makeEmbed(' ', 3)
    return embed
