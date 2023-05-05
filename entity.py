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
  
  
    


def fetch_entity_id(name):
  
  with open('entityDex.txt', 'r') as f:
        for line in f:
            values = line.strip().strip('[]').split(',')
            if values[1] == "ignore":
              pass              
            elif str(values[1]) == name:
                return int(values[0])
  return None



def search_entity_by_id(id):
    with open('entityDex.txt', 'r') as f:
        for line in f:
            values = line.strip().strip('[]').split(',')
            if str(values[0]) == "ignore":
              pass              
            elif int(values[0]) == id:
                return [int(val) if val.isdigit() else val for val in values]
    return None





def create(owner_id, namePassed):
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
        print("stats r none")



def listMine(owner_id):
  myEntityName = []
  myEntityID = []
  myEntityHP = []

  
  
  for key in db.keys():
    print("searching DB")  
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
    return None


def delete(id):
  del db[id]
  return "Key deleted"


def moveset(target):
  entity_id, name, rank, hp, max_moves, *attacks = reference(target)
  print(attacks)

  embed = discord.Embed(title=f"Moveset for your {name}, ID {entity_id}", description="There are three kinds of moves: techniques, magic spells and skills(passive and active)", colour = discord.Colour.green())

  times = 0
  for move in attacks: 
    embed.add_field(name=f"{attacks[times]}", value = " ",inline=False)
    times = times + 1

  return embed
    
    
    
  


