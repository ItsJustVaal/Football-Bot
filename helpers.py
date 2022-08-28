import imports
# Helper Functions


def makeEmbed(desc, declare):
    if declare == 1:
        with open("jsons/matches.json", "r") as matches:
            data = imports.json.load(matches)
        embed = imports.discord.Embed(
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
        embed = imports.discord.Embed(
            description=desc
        )
    elif declare == 3:
        file = imports.discord.File(
            '/Temp/Code/MyBot/jammed.jpg', filename='jammed.jpg')
        embed = imports.discord.Embed(
            description=desc
        )
        embed.set_image(url='attachment://jammed.jpg')
        return file, embed
    return embed
