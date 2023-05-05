from replit import db

def create_account(owner_id):
  owner_id = str(owner_id)
  db[owner_id] = 0
  print(f"Account created for {owner_id} with balance 0")

def get_balance(owner_id):
  owner_id = str(owner_id)
  bal = db[owner_id]
  return bal

def update_balance(owner_id, amount, type):
  owner_id = str(owner_id)
  if type == "add":
    print(f"Executing currency add operation to user id {owner_id}")
    previous_bal = int(db[owner_id])
    print(f"Previous balance: {previous_bal}. Adding {amount}")
    db[owner_id] = previous_bal + amount
    print(f"Sucess. New balance:{db[owner_id]}")

  elif type == "subtract":
    owner_id = str(owner_id)
    print(f"Executing currency subtract operation to user id {owner_id}")
    previous_bal = int(db[owner_id])
    print(f"Previous balance: {previous_bal}. Subtracting {amount}")
    db[owner_id] = previous_bal - amount
    print(f"Sucess. New balance:{db[owner_id]}")
  else:
    print("unknown error in update_balance")
    return