import os
import discord
from keep_alive import keep_alive
from langcodes import *
from channel import *
from language_processing import google
from locales import locales

client = discord.Client()

# ========================================================
# Executes whenever bot goes live in server
# ========================================================
async def process_command(message):
  text = message.content.split('$proctor-bot ', 1)[1]
  if text.startswith('set-language'):
    code = text.split('set-language ', 1)[1]

    if code == 'none':
      old_code = get_channel_lang(message.channel.id)
      try:
        remove_channel_lang(message.channel.id)
        await say(message.channel, "I am no longer proctoring [language].", [locales.langauges[old_code]])
      except:
        print('Error occured while removing channel language')

    elif code == None or Language.get(code).is_valid() == False:
      await say(message.channel, "I'm sorry, that doesn't seem to be a valid language.")
    else:
      code = standardize_tag(code)
      set_channel_lang(message.channel.id, code)
      await say(message.channel, "I am now proctoring [language]", [locales.languages[code]])
  else:
    await say(message.channel, "I'm sorry, I didn't recognize that command.")

# ========================================================
# Analyzes message for language misuses, and responds accordingly
# ========================================================
async def enforce_language(message):
    lang_guess = google.get_lang_guess(message.content);
    code = lang_guess['language']
    
    # ignore short messages with low confidence
    if len(message.content) <= 10 or len(message.content.split()) < 3:
      return
      # TODO: improve response for short/low confidence messages

    # check if message language matches channel language
    if code != 'und' and code != get_channel_lang(message.channel.id):
      await say(message.channel, "Please only use [language] in this channel. Thank you!", [locales.languages[get_channel_lang(message.channel.id)]]) 

# --------------------------------------------------------
# handlers
# --------------------------------------------------------

# ========================================================
# Executes whenever bot goes live in server
# ========================================================
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# ========================================================
# Executes whenever a message is sent in discord server
# ========================================================
@client.event
async def on_message(message):
  # ignore bot's own messages
  if message.author == client.user:
    return

  # handle bot command
  elif message.content.startswith('$proctor-bot'):
    await process_command(message)

  # detect langage
  elif channel_has_lang(message.channel.id):
    enforce_language(message)

# --------------------------------------------------------
# init
# --------------------------------------------------------
locales.load_locales()
keep_alive()
client.run(os.getenv('DISCORD_BOT_TOKEN'))
