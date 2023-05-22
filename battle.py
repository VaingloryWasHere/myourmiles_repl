from tinydb import TinyDB, Query, where
from discord.ext import tasks, commands


#smol to-do list. Make a player-vs battle command first.
"""
Hi!

"""


#carrier: person on whom the effect is put. [Combatant object.]
#originator: person who put the effect on the carrier. [Combatant object.]
#in healing spells, both are the same. For simplicity's sake, hp points in healing spells are added to carrier, not originator.
class Effect(originator,carrier,effect_id):
    
    def __init__(self,time):
        self.effect_interval = time
        effectDB = TinyDB()
        effectInfo = Query(where("ID") == effect_id)
        self.harming = effectInfo["harming"]
        
        if effectInfo["selfheal"]:
            self.selfHeal = effectInfo["selfheal"]
            self.burstHeal = effectInfo["burst"] if effectInfo["burst"] True else self.regenerative = True
            self.healamt = effectInfo["healamount"]

        self.dmgPerTurn = effectInfo["dmgPerTurn"]
        self.duration = effectInfo["durationTurns"]
        self.gapPerTurn = effectInfo["gapPerTurn"]
        self.consecutive = effectInfo["consecutive"]
        self.turnsLeft = 1 #Effects applied will come into effect immediately after being created, then
        #gapPerTurn takes over.
        self.effect_emoji = effectInfo["emoji"]
        self.times_applied = 0
        self.expired = False
        
    def applyBurstHeal():
        carrier.hp = carrier.hp + self.healamt
        self.expired = True
        return True
    
    def applyRegeneration():
        carrier.hp = carrier.hp + self.healamt
        self.times_applied += 1
        return True
        
    def applyBuff():
        pass
        
    def applyDebuff():
        pass
    
    def applyHarming():
        carrier.hp = carrier.hp - self.dmgPerTurn
        return True


    def applyEffect(): #self explanatory.  May call upon more specific classes if need be.
        if self.harming == True:
            
            applyHarming()
            
        elif self.selfHeal == True:
            
            if self.burst == True:
                applyBurstHeal()
                
            elif self.regenerative == True:
                applyRegeneration()
                
        elif self.buff == True
                
            
            

class Combatant(name,owner,hp,moves): #Owner is ctx.author.id(int) btw.
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
                    e = Effect(self.owner,opponent,effect_id)
                    self.effects.append(e)
                    print(f"Made instance of Effect class. Originator: {self.owner}, inflicted on: {opponent}, effect id {effect_id}")
                    
                
                return True
            
            elif moveinfo["effect_ids"] == 0:
                print("effect ids list empty. Skipping.")
                return True
        else:
            print(f"[Fatal Error] move {move_name} does not exist. Aborting.")
            return False
        
        #idea: each combatant class may be made including a self.opponent_id in the future.
    
    
    def updateEffects(opponent):
        if not self.effects:
            print("Self.effects is empty. Returning false.")
            return False
        
        for effect in self.effects:
            
            if effect.consecutive == True:
                effect.applyEffect()
                print(f"consecutive effect applied.")
                
            elif effect.turnsLeft == 0:
                effect.applyEffect()
                print(f"turnsLeft for effect {effect} is 0. Calling applyEfect function.")
                return True

            else:
                prevTurns = effect.turnsLeft
                effect.turnsLeft = prevTurns - 1
                print(f"Previous turns left for effect {effect}: {prevTurns}. Subtracting 1. new turns left: {effect.turnsleft}")
                return True
        
        
            
            
            
        
        