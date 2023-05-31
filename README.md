# GigaDMB
![GigaDMB](https://github.com/WhiteHodok/GigaDMB/assets/39564937/3f755e4a-a2dc-4e18-8d51-244c65d1b76a)



# Music Bot

This is a Discord bot that allows you to play music from YouTube in a voice channel. It uses the discord.py library and several other Python packages to provide the functionality.

# Installation

To use this bot, you need to have Python 3.8 or higher installed on your system. Follow these steps to set up the bot:

- Clone this repository to your local machine or download the code as a ZIP file.

# Install the required dependencies by running the following command in the project directory:

- pip install -r requirements.txt

- Replace the token variable in the code with your own Discord bot token. You can obtain a token by creating a new bot on the Discord Developer Portal.

# Run the bot by executing the following command:

python bot.py


# Usage
Once the bot is up and running, you can use the following commands to control the music playback in your Discord server:

- $play <search_query>: Searches for a YouTube video based on the provided search query and adds it to the playback queue.

- $skip: Skips the currently playing song and plays the next song in the queue.

- $pause: Pauses the music playback.

- $resume: Resumes the music playback if it was paused.

- $stop: Stops the music playback and clears the queue.

- $bye: Stops the music playback, clears the queue, and disconnects the bot from the voice channel.

- $shuffle: Shuffles the songs in the queue.

- $nowplaying: Displays the currently playing song.

- $queue: Shows the current queue of songs.

- $remove <index>: Removes the song at the specified index from the queue.

 Feel free to modify the code and add more features according to your needs.
