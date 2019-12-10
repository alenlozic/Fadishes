# Course: CS 30
# Period: 1
# Date created: 10/12/2019
# Date last modified: 10/12/2019
# Name: Alen Lozic
# Description: Nested Dictionary

# valid directions and actions for the characters
valid_actions = {"directions": ["north", "south", "east", "west"],
                 "actions": ["explore", "attack", "defend", "heal"]}

attack = ['knife', 'sword', 'axe']
protection = ['magnum shield', 'bicycle helmet', 'trojan armor']
restore =[]
print(f"There are {len(attack)} items in attack and {len(protection)} items " +
      f"in protection")
# valid weapons directions for attack
print("\nAttack:\n")
for weapons in attack:
    print(weapons)
print("\nProtection:\n")
for items in protection:
    print(items)
print("\n")
# print out the choices in valid actions: actions or directions
for choice in valid_actions:
    print(choice)
    # print out all the directions
    direction = valid_actions["directions"]
    if choice == "directions":
        for direct in direction:
            print(f"- {direct} ")
    # print out all the actions
    action = valid_actions["actions"]
    if choice == "actions":
        for direct in action:
            print(f"- {direct}")
