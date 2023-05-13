from replit import db
from tinydb import TinyDB, Query
import discord
import movement


intents = discord.Intents().all()
bot = discord.Client(command_prefix="@",intents=intents)

def reference(target):
  res = []
  #id, name, hp, max moves, attacks
  try:
    target = int(target)
    with open('entityDex.txt', 'r') as f:
        for line in f:
            values = line.strip().strip('[]').split(',')
            if int(values[0]) == target:
              for i, el in enumerate(values):
                if i == 0: #ID
                  res.append(int(el))
                elif i == 1: #name
                  res.append(str(el)) 
                elif i == 2: #rank
                  res.append(str(el))
                elif i == 3: #HP
                  res.append(int(el))
                elif i==4: #max movez
                  res.append(int(el))
                else: #attacks
                  res.append(str(el))
        return res


  except ValueError:
      target = str(target)
      with open('entityDex.txt', 'r') as f:
        for line in f:
            values = line.strip().strip('[]').split(',')
            if str(values[1]) == target:
              for i, el in enumerate(values):
                if i == 0: #ID
                  res.append(int(el))
                elif i == 1: #name
                  res.append(str(el)) 
                elif i == 2: #rank
                  res.append(str(el))
                elif i == 3: #HP
                  res.append(int(el))
                elif i==4: #max movez
                  res.append(int(el))
                else: #attacks
                  res.append(str(el))
        return res
  
  
    


def create(owner_id, entityName):
  enCache = TinyDB("entities.json")
  result = reference(entityName)

  if result != None:
    final_entity_id, name, rank, hp, max_moves, *attacks = result

  if enCache.all():
        # entities.json is not empty, do something
      entity_ids = [entity['entityID'] for entity in enCache.all() if 'entityID' in entity]
      highest_id = max(entity_ids)
      print(f"The highest entity id is: {highest_id}")
        
      enCache.insert({'entityID':highest_id+1,'name':entityName,'owner_id':owner_id, 'hp':hp, 'referId':result[0], 'level':1, 'moves': []})
      movement.spawn_on_map(owner_id)

    
  else:
      enCache.insert({'entityID':1,'name':entityName,'owner_id':owner_id, 'hp':hp, 'referId':result[0], 'level':1, 'moves': []})
      movement.spawn_on_map(owner_id)
  



'''def create(owner_id, namePassed):
    existing_keys = db.keys()
          
    if len(existing_keys) != 0:
          
    # If there are keys in the database, get the name of the highest key
        highest_key_name = max(existing_keys)
              
        new_key_name = str(int(highest_key_name) + 1)
      
        result = reference(namePassed)

      
        if result is not None:
          final_entity_id, name, rank, hp, max_moves, *attacks = result
          db[new_key_name] = [name, owner_id, hp]
          movement.spawn_on_map(owner_id)
        else:
          print("Entity not found.")
          return
        

    else:
      stats = reference(namePassed)

      if stats is not None:
          second_entity_id, name2, rank2,hp2, max_moves2, *attacks2 = stats
          db[1] = [name2, owner_id, hp2]
          movement.spawn_on_map(owner_id)
      else:
        print("stats r none")'''



def listMine(owner_id):
  myEntityName = []
  myEntityID = []
  myEntityHP = []
  enCache = TinyDB("entities.json")
  
  entityFind = Query()
  targetTeam = enCache.search(entityFind.owner_id==owner_id)
  if targetTeam:
    teamLen = len(targetTeam)
    times = 0
    while times != teamLen:
      myEntityName.append(targetTeam[times]['name']) #name
      print(f"appended name '{targetTeam[times]['name']}' to user id {owner_id}")
      myEntityID.append(targetTeam[times]['referId']) #refer id
      print(f"appended value '{targetTeam[times]['referId']}' to user id {owner_id}")
      myEntityHP.append(targetTeam[times]['hp']) #Hp
      print(f"appended value '{targetTeam[times]['hp']}' to user id {owner_id}")
      times = times + 1

    if myEntityName and myEntityID and myEntityHP != None:
      return myEntityName, myEntityID, myEntityHP
      print(f"Entity ID: {myEntityID}")
      print(f"Entity HP: {myEntityHP}")
      print(f"Entity Names: {myEntityName}")

  if not targetTeam:
    print("targetTeam list empty. Returning None.")
    return None
    
      
''' print("searching DB")  
    keyData = db[key]
    print(keyData)
    if int(keyData[1]) == int(owner_id):
      print(f"found 1: {keyData[0]}")

      myEntityName.append(keyData[0])
      print(f"appended")
      myEntityHP.append(keyData[2]) #hp is always stored in db.
      entityID = fetch_entity_id(keyData[0])
      myEntityID.append(entityID)

    else:
      print(f"found not owned key; {keyData[0]} owned by {keyData[1]}, with entity ID {keyData[0]} with HP {keyData[-1]}")

      
  if myEntityName and myEntityID and myEntityHP != None:
    return myEntityName, myEntityID, myEntityHP
    print(f"Entity ID: {myEntityID}")
    print(f"Entity HP: {myEntityHP}")
    print(f"Entity Names: {myEntityName}")
  else:
    print(f"Entity ID: {myEntityID}")
    print(f"Entity HP: {myEntityHP}")
    print(f"Entity Names: {myEntityName}")
    print("failure")
    return None'''


def moveset(target):
  entity_id, name, rank, hp, max_moves, *attacks = reference(target)
  print(attacks)

  embed = discord.Embed(title=f"Moveset for {name}, ID {entity_id}", description="There are three kinds of moves: techniques, magic spells and skills(passive and active) **If you own this character and wish to see what moves you've already taught it, see page 2.** If there's no option to switch pages, it means the character doesn't know any moves, __or__ you don't own it.", colour = discord.Colour.green())

  times = 0
  for move in attacks: 
    embed.add_field(name=f"{attacks[times]}", value = " ",inline=False)
    times = times + 1

  return embed
    
    
def getKnownMoves(owner_id, entity_refID):
  query = Query()
  enCache = TinyDB("entities.json")
  entityList = enCache.search(query.referId == entity_refID)
  print(len(entityList))
  for entity in entityList:
    if entity['owner_id'] == owner_id:
      print(f"An entity with ref id {entity_refID} is owned by user id {owner_id}. Making an embed with moves: {entity['moves']}")
      return entity['moves']

  print(f"Couldn't find a/an entity with ref id {entity_refID} that is associated with user id {owner_id}")
  return None

