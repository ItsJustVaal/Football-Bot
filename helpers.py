import imports as imp
# Helper Functions


def makeEmbed(desc, declare):
    if declare == 1:
        with open("jsons/matches.json", "r") as matches:
            data = imp.json.load(matches)
        embed = imp.discord.Embed(
            description=desc
        )
        embed.add_field(
            name='Group 1',
            inline=True,
            value=f"""
                {data['FirstSet']['Left1']} - {data['FirstSet']['Right1']} 
                {data['FirstSet']['Left2']} - {data['FirstSet']['Right2']}
                {data['FirstSet']['Left3']} - {data['FirstSet']['Right3']}
                {data['FirstSet']['Left4']} - {data['FirstSet']['Right4']}
        """)
        embed.add_field(
            name='Group 2',
            inline=True,
            value=f"""
                {data['SecondSet']['Left1']} - {data['SecondSet']['Right1']} 
                {data['SecondSet']['Left2']} - {data['SecondSet']['Right2']}
                {data['SecondSet']['Left3']} - {data['SecondSet']['Right3']}
                {data['SecondSet']['Left3']} - {data['SecondSet']['Right4']}
        """)
        embed.add_field(
            name='Group 3',
            inline=True,
            value=f"""
                {data['ThirdSet']['Left1']} - {data['ThirdSet']['Right1']} 
                {data['ThirdSet']['Left2']} - {data['ThirdSet']['Right2']}
                {data['ThirdSet']['Left3']} - {data['ThirdSet']['Right3']}
                {data['ThirdSet']['Left3']} - {data['ThirdSet']['Right4']}
        """)
    elif declare == 2:
        embed = imp.discord.Embed(
            description=desc
        )
    elif declare == 3:
        file = imp.discord.File(
            '/Temp/Code/MyBot/jammed.jpg', filename='jammed.jpg')
        embed = imp.discord.Embed(
            description=desc
        )
        embed.set_image(url='attachment://jammed.jpg')
        return file, embed

    elif declare == 4:
        username = desc
        with open("jsons/member.json", "r") as members:
            data = imp.json.load(members)
        if data[username]['isPlaying'] != 1:
            embed = imp.discord.Embed(
                description='You need to .join first nerd')
            return embed
        with open("jsons/matches.json", "r") as matches:
            match = imp.json.load(matches)
        embed = imp.discord.Embed(
            description='My Pred'
        )
        embed.add_field(
            name='Group 1',
            inline=True,
            value=f"""
                {match['FirstSet']['Left1']}: {data[username]['one1Left']} - {match['FirstSet']['Right1']}: {data[username]['one1Right']} 
                {match['FirstSet']['Left2']}: {data[username]['one2Left']} - {match['FirstSet']['Right2']}: {data[username]['one2Right']}
                {match['FirstSet']['Left3']}: {data[username]['one3Left']} - {match['FirstSet']['Right3']}: {data[username]['one3Right']}
                {match['FirstSet']['Left4']}: {data[username]['one4Left']} - {match['FirstSet']['Right4']}: {data[username]['one4Right']}
        """)
        embed.add_field(
            name='Group 2',
            inline=True,
            value=f"""
                {match['SecondSet']['Left1']}: {data[username]['two1Left']} - {match['SecondSet']['Right1']}: {data[username]['two1Right']} 
                {match['SecondSet']['Left2']}: {data[username]['two2Left']} - {match['SecondSet']['Right2']}: {data[username]['two2Right']}
                {match['SecondSet']['Left3']}: {data[username]['two3Left']} - {match['SecondSet']['Right3']}: {data[username]['two3Right']}
                {match['SecondSet']['Left4']}: {data[username]['two4Left']} - {match['SecondSet']['Right4']}: {data[username]['two4Right']}
        """)
        embed.add_field(
            name='Group 3',
            inline=True,
            value=f"""
                {match['ThirdSet']['Left1']}: {data[username]['three1Left']} - {match['ThirdSet']['Right1']}: {data[username]['three1Right']} 
                {match['ThirdSet']['Left2']}: {data[username]['three2Left']} - {match['ThirdSet']['Right2']}: {data[username]['three2Right']}
                {match['ThirdSet']['Left3']}: {data[username]['three3Left']} - {match['ThirdSet']['Right3']}: {data[username]['three3Right']}
                {match['ThirdSet']['Left4']}: {data[username]['three4Left']} - {match['ThirdSet']['Right4']}: {data[username]['three4Right']}
        """)

    return embed


def calculate(lp, rp, lr, rr):
    pass
