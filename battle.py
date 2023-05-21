from tinydb import TinyDB, Query, where
from discord.ext import tasks, commands


#smol to-do list. Make a player-vs battle command first.
"""
Hi!

"""




class Effect(originator,user,effect_id):
    
    def __init__(self,time):
        self.effect_interval = time
        effectDB = TinyDB()
        effectInfo = Query(where("ID") == effect_id)
        self.harm = effectInfo["harming"]
        if effectInfo["selfheal"]:
            self.selfHeal = effectInfo["selfheal"]
            self.burstHeal = effectInfo["burst"] if effectInfo["burst"] True else self.regenerative = True
  
            
            
        self.dmgPerTurn = effectInfo["dmgPerTurn"]
        self.duration = effectInfo["durationTurns"]
        self.gapPerTurn = effectInfo["gapPerTurn"]
        self.effect_emoji = effectInfo["emoji"]
        
        

class Combatant(name,owner,hp,moves):
    def __init__(self):
        self.name = name
        self.owner = owner
        self.hp = hp
        self.moves = moves
        self.effects = []
    
    def attack(opponent,move_name): #opponent arg expected to be Combatant class instance.
        #Class returns true if success. False if not.
        if attack in moves:
            moveDB = TinyDB()
            moveinfo = moveDB.get(where("name") == move_name)
            
            if moveinfo == None:
                print(f"No move matching the given move name: [{move_name}] was found. Returning False")
                return False
            
            prevHPholder = opponent.hp
            opponent.hp = opponent.hp - moveinfo["damage"]
            
            if opponent.hp == prevHPholder:
                print("Opponent's hp remained unchanged despite executing move! Fatal error. Stopping further actions. Returning False")
                return False
            
            print(f"Damage done! Previous hp: {prevHPholder} and current hp: {opponent.hp}")
            
            if len(moveinfo["effect_ids"]) >= 0:
                amountOfEffects = len(moveinfo["effect_ids"])
                for effect_id in moveinfo["effect_ids"]:
                    Effect(self.owner,opponent,effect_id)
                    print(f"Made instance of Effect class. Originator: {self.owner}, inflicted on: {opponent}, effect id {effect_id}")
                    
                
                return True
            
            elif moveinfo["effect_ids"] == 0:
                print("effect ids list empty. Skipping.")
                return True
            
            pass
            
        
        