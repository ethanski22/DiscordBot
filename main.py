from discord.ext.commands import Bot
import os
import random

bot = Bot(command_prefix="|")

prompts_and_responses = {
  "hello": "Hello there!",
  "sup": "Hi, I'm HyTechClub Robot!",
  "how are you?": "I am fine!",
	"hello there": "General Kenobi"
}

@bot.event
async def on_ready():
  print("Logged in as: {}".format(bot.user))
  print("Command prefix is: {}".format(bot.command_prefix))

@bot.event
async def on_message(message):
  if message.author.bot:
    return

  print("Received message: {} > {}".format(message.author, message.content))

  if message.content == "ping":
    await message.channel.send("pong")

  for prompt in prompts_and_responses.keys():
    if prompt in message.content:
      print("Found prompt: {} in message {}"
        .format(prompt, message.content))
      await message.channel.send(prompts_and_responses[prompt])

token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)