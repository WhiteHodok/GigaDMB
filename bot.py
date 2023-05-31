import discord
from discord import *
import pafy
from youtubesearchpython import VideosSearch
import asyncio
import random

token = ""
intents = discord.Intents.all()
client = discord.Client(intents=intents)

voice_clients = {}
ffmpeg_options = {'options': '-vn'}



# message when the bot gets run
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")


queue = []
titles = []


@client.event
async def on_message(msg):
    if msg.content.startswith("$play"):
        global queue
        global titles
        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[msg.guild.id] = voice_client
        except Exception as err:
            print(err)
        search_query = " ".join(msg.content.split()[1:])  # returns a list of words and puts them into a string
        try:
            loop = asyncio.get_event_loop()
            while voice_clients[msg.guild.id].is_playing():
                await asyncio.sleep(1)
            videosSearch = VideosSearch(search_query, limit = 1)
            video_url = videosSearch.result()['result'][0]['link']
            video = pafy.new(video_url)
            song = video.getbest().url
            title = video.title
            queue.append(song)
            titles.append(title)
            if len(queue) == 1 and not voice_clients[msg.guild.id].is_playing():
                player = discord.FFmpegPCMAudio(queue[0], **ffmpeg_options)
                voice_clients[msg.guild.id].play(player, after=lambda x: queue.pop(0))
                titles.pop(0)
                await msg.channel.send(f"Playing {title}")
            else:
                await msg.channel.send(f"Added to queue: {title}")
        except Exception as err:
            print(err)
    if msg.content.startswith("$skip"):
        try:
            if voice_clients[msg.guild.id].is_playing():
                voice_clients[msg.guild.id].stop()
                await msg.channel.send("Song skipped")
        except Exception as err:
            print(err)
    # pause
    if msg.content.startswith("$pause"):
        try:
            voice_clients[msg.guild.id].pause()
            await msg.channel.send("Music paused!")
        except Exception as err:
            print(err)
    #resume
    if msg.content.startswith("$resume"):
        try:
            voice_clients[msg.guild.id].resume()
            await msg.channel.send("Music resumed!")
        except Exception as err:
            print(err)
    #stop
    if msg.content.startswith("$stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await msg.channel.send("Music stopped, let's listen next!")
        except Exception as err:
            print(err)
    if msg.content.startswith("$bye"):
        try:
            voice_clients[msg.guild.id].stop()
            await msg.channel.send("Bye!")
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)
    #shuffle
    if msg.content.startswith("$shuffle"):
        try:
            random.shuffle(queue)
            random.shuffle(titles)
            await msg.channel.send("Queue shuffled!")
        except Exception as err:
            print(err)
    #nowplaying
    if msg.content.startswith("$nowplaying"):
        try:
            if voice_clients[msg.guild.id].is_playing():
                await msg.channel.send(f"Now playing: {titles[0]}")
            else:
                await msg.channel.send("No music is currently playing")
        except Exception as err:
            print(err)
    #queue
    if msg.content.startswith("$queue"):
        try:
            if not queue:
                await msg.channel.send("Queue is empty")
            else:
                queue_str = ""
                for i in range(len(queue)):
                    queue_str += f"{i+1}. {titles[i]}\n"
                await msg.channel.send(f"Current queue:\n{queue_str}")
        except Exception as err:
            print(err)
    #remove
    if msg.content.startswith("$remove"):
        try:
            index = int(msg.content.split()[1]) - 1
            removed_title = titles.pop(index)
            removed_song = queue.pop(index)
            await msg.channel.send(f"Removed {removed_title} from the queue")
        except Exception as err:
            print(err)
    # resume
    if msg.content.startswith("$resume"):
        try:
            voice_clients[msg.guild.id].resume()
            await msg.channel.send("Music resumed!")
        except Exception as err:
            print(err)
    # stop
    if msg.content.startswith("$stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await msg.channel.send("Music stopped, let's listen next!")
        except Exception as err:
            print(err)
    if msg.content.startswith("$bye"):
        try:
            voice_clients[msg.guild.id].stop()
            await msg.channel.send("Bye!")
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)
    # shuffle
    if msg.content.startswith("$shuffle"):
        try:
            random.shuffle(queue)
            random.shuffle(titles)
            await msg.channel.send("Queue shuffled!")
        except Exception as err:
            print(err)
    # nowplaying
    if msg.content.startswith("$nowplaying"):
        try:
            if voice_clients[msg.guild.id].is_playing():
                await msg.channel.send(f"Now playing: {titles[0]}")
            else:
                await msg.channel.send("No music is currently playing")
        except Exception as err:
            print(err)
    # queue
    if msg.content.startswith("$queue"):
        try:
            if not queue:
                await msg.channel.send("Queue is empty")
            else:
                queue_str = ""
                for i in range(len(queue)):
                    queue_str += f"{i + 1}. {titles[i]}\n"
                await msg.channel.send(f"Current queue:\n{queue_str}")
        except Exception as err:
            print(err)
    # remove
    if msg.content.startswith("$remove"):
        try:
            index = int(msg.content.split()[1]) - 1
            removed_title = titles.pop(index)
            removed_song = queue.pop(index)
            await msg.channel.send(f"Removed {removed_title} from the queue")
        except Exception as err:
            print(err)


client.run(token)
