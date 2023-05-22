from tinydb import TinyDB, Query
import asyncio
map = TinyDB(r"data\playerLocations.json")

def spawn_on_map(owner_id):
  map.insert({"user_id": owner_id,'location': 'Blumund: Royal Capital','status':'stationery','next location': None,'time_left': None})
  print(f"User with id {owner_id} has been spawned in the Royal Capital of Blumund!")
  
async def move(user,place,time: int):
  time_spend_moving = 0
  userPreviousLocation = Query()
  userFetched = map.get(userPreviousLocation.user_id==user)
  userFetched['time_left'] = int(time)

  if place == "Blumund Royal Capital Arena":  

    print(f"starting movement of {user} from {userFetched['location']} to {place}. ETA: {time}")
    while time_spend_moving != time:
      await asyncio.sleep(1)
      userFetched["status"] = "moving"
      userFetched["next location"] = place
      time_spend_moving = time_spend_moving + 1
      userFetched['time_left'] = int(userFetched['time_left']) - 1
      map.update(userFetched, userPreviousLocation.user_id == user)
  
    print(f"Movement successful. Moved {user} to {place} from {userFetched['location']}")
    print("Executing Final batch of operations. Set status to stationery and 'next location' to None. Current location updated.")
    userFetched['location'] = place
    userFetched['next location'] = None
    userFetched['status'] = 'stationery'
    map.update(userFetched, userPreviousLocation.user_id == user)
  else:
    return "unknown place"
    

