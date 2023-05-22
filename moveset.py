from tinydb import TinyDB, Query

movedb = TinyDB(r"data\moves.json")
entitydb = TinyDB(r"data\entities.json")

def learnmove(entityID, moveName):
  query = Query()
  entityQuery = Query()

  moveObject = movedb.get(query.name == moveName)
  entityObject = entitydb.get(entityQuery.ID == entityID)
  
  if int(entityObject["level"]) == int(moveObject["lvlRequired"]):
    moveList = entityObject["moves"]
    moveList.append(moveName)
    updateQ = Query()
    entitydb.update({"moves": moveList}, updateQ.ID == entityID)
    print("move list updated")

  else:
    returnMsg = "Entity's level is too low!"
    return returnMsg