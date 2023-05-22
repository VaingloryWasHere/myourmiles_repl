from tinydb import TinyDB, Query

bank = TinyDB(r"data\bank.json")

def create_account(owner_id):  
  bank.insert({'id': owner_id, 'credits': 0})
  print(f"Account created for user id {owner_id} with balance 0")

def get_balance(owner_id): 
  user = Query()
  res = bank.get(user.id==owner_id)
  final_amount = res['credits']
  return final_amount

def update_balance(owner_id, amount: int, operation: str):
  if operation == "add":
    print("Starting add operation..")
    target = Query()
    targetAccount = bank.get(target.id==owner_id)
    previousBalance = targetAccount['credits']
    print(f"previous bal of {owner_id} is {previousBalance}. Adding {amount}")
    targetAffect = Query()
    bank.update({'credits': previousBalance + amount}, targetAffect.id==owner_id)
    print(f"Success. New balance: {previousBalance+amount}")
  
    
  elif operation == "subtract":
    target = Query()
    targetAccount = bank.get(target.id==owner_id)
    previousBalance = targetAccount['credits']
    targetAffect = Query()
    bank.update({'credits': previousBalance - amount}, targetAffect.id==owner_id)

  else:
    print("unknown error")
    return
