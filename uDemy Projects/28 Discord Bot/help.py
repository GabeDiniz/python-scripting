'''
Help.py

Format the discord embed for the !help command
'''

import discord

def format() -> str:
    @client.command()
    async def embeder():
        embed = discord.Embed(
            title = "Text formatting",
            url = "",
            description = "Description here",
            color = discord.Color.blue()
        )

        embed.set_author(
            name = "Cpt. Bot",
            url = "https://github.com/GabeDiniz",
            icon_url = "https://unsplash.com/photos/black-smartphone-near-person-5QgIuuBxKwM" # may not work
        )
        embed.set_thumbnail(url="https://unsplash.com/photos/black-smartphone-near-person-5QgIuuBxKwM")
        embed.add_field(name="!help", value="See list of commands")
        print(f"Embed Type: {type(embed)}")

        return embed