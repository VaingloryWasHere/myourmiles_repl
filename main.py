import entity
from discord.ext import commands
import discord
import os
from keep_alive import keep_alive
from replit import db
import asyncio
import currency
from math import *
from time import *
from datetime import timedelta
from discord.ui import View, Button, Select
import movement

print(os.getenv("REPLIT_DB_URL"))



these = discord.Intents().all()
# Set up the bot command prefix
bot = commands.Bot(command_prefix="#", intents=these)
#instance discord-ui



bot.owner_id = 718710286596702220

   
@bot.command()
async def button(ctx):
  button = Button(label="This is a button", style=discord.ButtonStyle.green)
  button2 = Button(label="Get nuclear launch codes", style=discord.ButtonStyle.danger, url="https://r.mtdv.me/articles/thermonuke")
  view = View()
  view.add_item(button)
  view.add_item(button2)
  await ctx.send("Yo.", view=view)
  

#GAME.START SECTION
@bot.command()
async def start(ctx):
  all_entity = db.keys()
  for key in all_entity:
      entity_data = db[key]
      if entity_data[1] == ctx.author.id: 
        await ctx.send("Dummy, you've already used this command before!")
        for key in all_entity:
          print(f"{key}={db[key]}")
        return
    
    
  embed=discord.Embed(title="Welcome!", description="This bot is like PokeTwo, except that instead of pokemon you use characters from Tensura and the people in this server. With that said, go ahead and choose your first character!", color=discord.Color.blue())

  choice1 = '''
      `Rarity: Common`
      `HP: 250` 
      `Max moves: 5`
      `Description: Spirits that specialise in healing.`
    '''

  choice2 = '''
  `Rarity: Common`
  `HP:500` 
  `Max moves: 7`
  `Description:` Wait... why does this feel so familiar?`
  
  
  '''

  choice3 = '''
  `Rarity: Common`
  `HP:750`
  `Max moves: 5`
  `Description: Demons specialise in all kinds of magic. Their skills and techniques are mainly centered around offense.'''

  choice4 = '''
  `Rarity: Common`
  `HP: 500`
  `Max moves: 5`
  `Description: Elves are famous for their long lifespans. They too specialise in a wide variety of magic however they are more balanced at combat than demons. `
  '''
  ranks = '''
      Character Rankings: `Common,Rare,Legendary,Mythical`
      Max moves: `The number of moves a character can learn at max. Higher rank characters will be able to learn and use more moves in combat.`
      HP: `Self explainatory.`
      **There is no levelling system.. for now**

''' 
  embed.add_field(name="Helpful information", value=ranks, inline=False)
  embed.add_field(name="1. Unnamed Undine Spirit", value=choice1, inline=False)
  embed.add_field(name="2. Unnamed Slime", value=choice2,inline=False)
  embed.add_field(name="3. Unnamed Lesser Demon", value=choice3,inline=False)
  embed.add_field(name="4. Unnamed Elf", value=choice4,inline=False)

  
  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
  #select  menu callback:

  select = Select(options=[
    discord.SelectOption(label="Unnamed Undine Spirit",emoji="<:undine:1097100135214891088>", default=True),
    discord.SelectOption(label="Unnamed Slime",emoji="<:slime:1097112499641405480>"),
    discord.SelectOption(label="Unnamed Lesser Demon",emoji="<:lesserdemon:1097112199916421160>"),
    discord.SelectOption(label="Unnamed Elf",emoji="<:unnamed_elf:1097112978811265095>")
  ])
  view = View()
  view.add_item(select)

  

  await ctx.send(embed=embed,view=view)

  async def my_callback(interaction):
    disCrazy = interaction.response
    print(interaction.id)
    await disCrazy.send_message("Hmm. I see you have chosen an {select.values[0]} as your first character. Type `#tutorial` to get further instructions. ")
    print(f"Chosen: {select.values[0]}")
    entity.create(ctx.author.id,select.values[0])

  select.callback = my_callback


 

#Tutorial,woooo

@bot.command()
async def tutorial(ctx):
  page1_description = '''

  __Page 1: Introduction to the bot__ **[Current Page]**
  
  __Page 2: Frequently Asked Questions.__

  __Page 3: Everything you can do with your character.__

  __Page 4: Encounters.__

  __Page 5: Moving to different locations.__
  
  '''
  page1 = discord.Embed(title="Your journey begins now.", description=page1_description, colour = discord.Colour.green())

  page1.add_field(name="Basic functionality.", value="The things you can do in this bot, boiled down to the simplest manner, are the following: Fight and defeat characters of different ranks, each with their own unique powers, to add to your team. Challenge other people, log in daily, and accept quests to earn more credits, which can be used in the shop. Once you reach a certain threshold, evolve your characters by naming them.", inline=False)

  page1.add_field(name="Prefix", value="The prefix for the bot is `#`", inline=False)

  view = View()
  pageMenu = Select(options=[
    discord.SelectOption(label="Page 2"),
    discord.SelectOption(label="Page 3"),
    discord.SelectOption(label="Page 4"),
    discord.SelectOption(label="Page 5"),
    discord.SelectOption(label="Page 6")
    
  ])
  view.add_item(pageMenu)

  await ctx.send(embed=page1,view=view)

  
  async def my_callback(interaction):
    if pageMenu.values[0] == "Page 2":
      page2 = discord.Embed(title="Frequently Asked Questions..", description="Find answers to any questions you may have.", colour=discord.Colour.green())
      page2.add_field(name="Question 1. What should I do with my team?", value="Answer-> You will have to use your team members to battle against other users, earning credits in the process. Battling other, stronger characters and defeating them will allow you to add said characters to your team.",inline=False)
      page2.add_field(name="Question 2. My starter character is trashy. How do I change it?", value="Answer-> You can't. Heh.",inline=False)
      page2.add_field(name="Question 3. Alright, how do I get more characters?", value="Answer-> Your character should have spawned in the royal capital of Blumund. You can head over to the arena to defeat and add new characters to your team, or move to a different location entirely, where you shall have random encounters with other entities. [See page 4 for more info on encounters]",inline=False)
      page2.add_field(name="Question 3. What are the basic stats/attributes of a character?", value="Name,ID,Rank and max moves are the stats of a character. Your character will be unnamed at first. You will get opportunities to name them at certain special events. Ranks are divided into - Common, Rare, Legendary and Mythical, with Mythical class representating true dragons and stronger beings. Max moves defines how many moves your character may use in a battle. By default, your character will know 0 moves.",inline=False)
      await interaction.response.defer()
      await interaction.edit_original_response(embed=page2)
      print("one change")


    elif pageMenu.values[0] == "Page 3":
      page3 = discord.Embed(title="Everything you can do with your characters", description="A neatly organised list of actions that you can do to your characters.")
      page3.add_field(name="Moves", value="Moves are divided into three categories: Techniques, like 'melt slash', spells like 'fireball', and skills like [Multi Layer Barrier.] Do note that skills can be both passive and active", inline=False)
      page3.add_field(name="Learning moves", value="By typing #moveset, followed by the id id of the character, you can view a list of the moves that a character can learn. However, there are certain level requirements to learn certain moves. Do #learn <move name> to learn said move.")
      await interaction.response.defer()
      await interaction.edit_original_response(embed=page3)

  pageMenu.callback = my_callback


#List command
@bot.command()
async def team(ctx):
  
  try:
    teamNames, teamIDs, teamHPs = entity.listMine(ctx.author.id)
  except:
      stupid = discord.Embed(title="Woah, hold on!", description="You don't have any characters in your team because you haven't registered with the bot! To do so, type `#start`.", colour=discord.Colour.blue())
      await ctx.send(embed=stupid)
      return
  else:
    info = discord.Embed(title="Your team.", description=f"You have {len(teamNames)} characters in your team.", colour = discord.Colour.green())
    times = 0
    for member in teamNames:
      descriptionEmbed = f'''
     
      `ID: {teamIDs[times]}`
      `HP: {teamHPs[times]}` 
      '''
      info.add_field(name=f"{times+1}. **{teamNames[times]}**", value = descriptionEmbed)
      times = times + 1

    await ctx.send(embed=info)

    
#MOVESET

@bot.command()
async def moveset(ctx, entityDexID):
  #each player can own only one instance of each character, thus each player will have only one entityDexId for each character

  result = entity.moveset(entityDexID)
  
  await ctx.send(embed=result)

#currency

@bot.command(aliases=["bal"])
async def balance(ctx):
  try:
    bal = currency.get_balance(ctx.author.id)
    embed = discord.Embed(title="Your balance.", description = f"You currently have {bal} credits", colour = discord.Colour.green())

    remaining_time = bot.get_command('daily').get_cooldown_retry_after(ctx)
    if remaining_time:
        remaining_time_str = str(timedelta(seconds=remaining_time))
        embed.add_field(name="Daily command", value=f"Cooldown: {remaining_time_str}.")
    else:
        embed.add_field(name="Daily command", value=f"Cooldown ended. You can use the commad now!")


      

    await ctx.send(embed=embed)
    
  except TypeError:

    await ctx.send("Looks like ya don't have an account yet Worry not! I just created one for ya.")
    currency.create_account(ctx.author.id)


@bot.command()
@commands.cooldown(1,86400.0,commands.BucketType.user)
async def daily(ctx):
  try:
    currency.update_balance(ctx.author.id, 100, "add")
    embed = discord.Embed(title="Daily bonus collected", description=f"You've collected 100 credits by using the daily command!",colour = discord.Colour.green())
    current_bal = currency.get_balance(ctx.author.id)
    embed.add_field(name="New Balance", value=f"{current_bal} credits")
    await ctx.send(embed=embed)
    
  except:
    
    currency.create_account(ctx.author.id)
    embed = discord.Embed(title="Daily bonus collected", description=f"You've collected ~~100~~ 80 credits by using the daily command!",colour = discord.Colour.red())
    currency.update_balance(ctx.author.id,80,"add")
    current_bal = currency.get_balance(ctx.author.id)
    embed.add_field(name="New Balance", value=f"{current_bal} credits")
    embed.set_footer(text="Note, as a punishment for using the daily command BEFORE creating an account, you've received 80 credits instead of the usual 100")
    await ctx.send(embed=embed)
    
#DEV-ONLY

#Check:



@bot.command()
@commands.is_owner()
async def dataBase(ctx,action,key = None):
  if action == 'list':
    await ctx.send(db.keys())
  elif action == "del":
    del db[key]
    await ctx.send(f"Key {key} deleted.")
  elif action == "url":
    url = os.getenv("REPLIT_DB_URL")
    await ctx.send(f"URL: {url}")
  elif action == "get":
    res = db[key]
    await ctx.send(f"Key {key} contains value: {res}")


  else:
    await ctx.send("Uknown command.")




#ERROR HANDLING

@bot.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.send("Iam missing the required permissions!")

  elif isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have the required permissions to do that")


  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Missing required argument")

  elif isinstance(error, commands.BadArgument):
    await ctx.send("Please enter the correct argument")

  elif isinstance(error, commands.MemberNotFound):
    await ctx.send("Member Not Found")

  elif isinstance(error, commands.CheckFailure):
    await ctx.send("You cannot use this!")


  elif isinstance(error, commands.CommandOnCooldown): 
      timee = float(format(error.retry_after))

      

      
      dayraw = timee / 86400

      day = math.floor(dayraw)


      hoursraw = timee / 3600

      hours = truncate(hoursraw,1)

      secsraw = timee % 3600

      secs = truncate(secsraw, 2)



      msg = f'**Still on cooldown**, please try again in {day} days, {hours} hours and {secs} seconds' #says the time
      await ctx.send(msg) #send the error message

  else:
    raise error


#movement

@bot.command()
async def travel(ctx,*,destination):
  
  if destination != "Blumund Royal Capital Arena":
    await ctx.send("Sorry. You can only go to the Blumund Royal Capital Arena, for now. Try typing `#travel Blumund Royal Capital Arena`")
  else:
    timeleft = discord.Embed(title=f"Travelling to Blumund Royal Capital Arena, {ctx.author.name}", description="Time required: 10 seconds", colour=discord.Colour.red())
    await ctx.send(embed=timeleft)
    await movement.move(ctx.author.id,destination, 10)
    movementDoneEmbed = discord.Embed(title=f"Travel complete, {ctx.author}", description="Your current location is the Blumund Royal Capital Arena. TO get started with fightning in the arena, type `#arena help`", colour=discord.Colour.green())
    await ctx.send(embed=movementDoneEmbed)
    






keep_alive()
bot.run("MTA5NTY0NTA3NzM5MDUwODEwMg.G2qIJZ.Z72tzGiYYj-L4B2O3X72RzT-rUVaGUkvZh9BhI")