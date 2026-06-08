#Wyatt McDonald

#The game title and commands to play the game
def show_instructions():
    print("Welcome to Zombie Principal Escape")
    print("=========================================")
    print("You are trapped inside a high school and must")
    print("collect all six items to win the game and escape,")
    print("or be trapped by the Zombie Principal!")
    print("Make sure to avoid the Zombie Principal before you have all six items.")
    print("=========================================")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("Type 'Exit' to quit the game.")
    print("=========================================")


#Show the player's current room, inventory, and any item in the room.
def show_status(current_room, inventory, rooms):
    print(f"You are in the {current_room}")
    print("Inventory:", inventory)
    if "Item" in rooms[current_room]:
        print("You see a", rooms[current_room]["Item"])


#Starts the player with 0 items and counts how many items are in the room
def count_items(rooms):
    item_count = 0
    for room in rooms:
        if "Item" in rooms[room]:
            item_count += 1
    return item_count


#This main function is what runs the game.
def main():
    #This is the dictionary for the rooms.
    rooms = {
        "Entrance": {"West": "Main Hall"},

        "Main Hall": {
            "East": "Entrance",
            "North": "Cafeteria",
            "Item": "School Map"
        },

        "Cafeteria": {
            "South": "Main Hall",
            "North": "Classroom",
            "East": "Gym",
            "West": "Principal Office",
            "Item": "Energy Snack"
        },

        "Classroom": {
            "South": "Cafeteria",
            "East": "Library",
            "Item": "Textbook Shield"
        },

        "Library": {
            "West": "Classroom",
            "Item": "Ancient Spellbook"
        },

        "Gym": {
            "West": "Cafeteria",
            "North": "Nurse Office",
            "Item": "Coach's Whistle"
        },

        "Nurse Office": {
            "South": "Gym",
            "Item": "First Aid Kit"
        },

        "Principal Office": {
            "East": "Cafeteria"
        }
    }
    #Declare variables needed for the game
    inventory = []
    valid_moves = ["North", "South", "East", "West"]
    num_items = count_items(rooms)
    current_room = "Entrance"
    danger_room = "Principal Office"

    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        #This has the player input a move/command
        player_move = input("Enter a move go <direction>, get <item>, or 'Exit' to quit:").strip()
        #Validates what input they gave
        if player_move.lower() == "exit":
            print("You decide to quit and stop exploring the school. Goodbye!")
            break
        if not player_move:
            print("Please enter a valid command.")
            continue
        parts = player_move.split()
        if len(parts) < 2:
            print("This move isn't a direction you can go. Please enter go North, go South, go East, or go West.")
            continue
        command = parts[0].lower()
        target = " ".join(parts[1:])
        #Moves the player between rooms
        if command == "go":
            direction = target.title()
            if direction not in valid_moves:
                print("You can't move in this direction. Please try again.")
                continue
            if direction not in rooms[current_room]:
                print("There is a wall in that direction. Please try again.")
                continue
            #Player moves to next room
            current_room = rooms[current_room][direction]
            #Sees if the room is the danger room and if they lost or won
            if current_room == danger_room:
                inventory_count = len(inventory)
                if inventory_count != num_items:
                    print("The zombie principal catches you unprepared. You Lose!")
                else:
                    print("You use all your items and trap the zombie principal and can escape. You Win!")
                print("Thank you for playing! I hope you enjoyed it.")
                break
        #If there is an item the player takes it, and it goes to the inventory
        elif command == "get":
            if "Item" in rooms[current_room]:
                item = rooms[current_room]["Item"]
                #Player must type the item name exactly
                if target.lower() == item.lower():
                    if item not in inventory:
                        inventory.append(item)
                        print(f"You've picked up: {item}")
                        #Remove this item from the room
                        del rooms[current_room]["Item"]

                        inventory_count = len(inventory)
                        if inventory_count == num_items:
                            print("You now have all six survival items. "
                                  "This means you're ready to face the zombie principal.")
                    else:
                        print("Item is already in the inventory.")
            else:
                print("Nothing to pick up in this room.")


if __name__ == "__main__":
    main()