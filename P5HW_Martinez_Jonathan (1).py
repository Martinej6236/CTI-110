
# Jonathan Martinez
# 11/18/2024
# P5HW
# making a game with functions

# Import Libary

import random
import time

# List to store all characters created
all_characters = []

def select_character_type():
    """Let player select their character type"""
    print("\nChoose your character type:")
    print("1. 🐉 Dragon")
    print("2. 🦸‍♂️ Knight")
    print("3. 🧙‍♂️ Wizard")
    print("4. 🦹 Dark Lord")
    
    while True:
        choice = input("Select type (1-4): ")
        types = {
            '1': '🐉 Dragon',
            '2': '🦸‍♂️ Knight',
            '3': '🧙‍♂️ Wizard',
            '4': '🦹 Dark Lord',
        }
        if choice in types:
            return types[choice]
        print("Invalid choice! Please try again.")

def create_character():
    """Create a character"""
    print("\nLet's create your character!")
    
    # Select character type first
    char_type = select_character_type()
    
    # Get character name
    name = input(f"Enter your {char_type}'s name: ")
    name = f"{name} the {char_type}"  # Combine name with type
    
    # Set stats without point limits
    print("\nSet your character's stats :")
    while True:
        try:
            health = int(input("Enter health points : "))
            if health < 10:
                print("Health must be at least 10!")
                continue
            
            attack_points = int(input("Enter attack points: "))
            if attack_points < 0:
                print("Attack must be 0 or greater!")
                continue
            
            defense = int(input("Enter defense points: "))
            if defense < 0:
                print("Defense must be 0 or greater!")
                continue
            
            break
        except ValueError:
            print("Please enter valid numbers!")
    
    # Create the character as a dictionary and add to the list
    new_character = {
        'name': name,
        'health': health,
        'attack_points': attack_points,
        'defense': defense
    }
    
    all_characters.append(new_character)
    print(f"\n{new_character['name']} has been created!")
    return new_character

def display_all_characters():
    """Display all characters"""
    print("\nAll Characters:")
    if not all_characters:
        print("No characters created yet.")
    for i, char in enumerate(all_characters, 1):
        print(f"{i}. {char['name']}")
        print(f"   Health: {char['health']} Attack: {char['attack_points']} Defense: {char['defense']}")

def select_character():
    """Let player select a character from the list"""
    display_all_characters()
    while True:
        try:
            choice = int(input("Select a character by number: "))
            if 1 <= choice <= len(all_characters):
                return all_characters[choice - 1]
            else:
                print("Invalid choice. Please select a valid character number.")
        except ValueError:
            print("Please enter a number!")

def battle(attacker, victim):
    """Simulate a battle round between two characters"""
    print(f"\n{attacker['name']} is attacking {victim['name']}!! ⚔️")
    
    # Calculate damage
    damage = max(0, random.randint(0, attacker['attack_points']) - victim['defense'])
    
    victim['health'] = max(0, victim['health'] - damage)
    print(f"{attacker['name']} did {damage} damage to {victim['name']} 💥")
    print(f"{victim['name']} has {victim['health']} health remaining.\n")
    
    return victim

def main():
    print("🎮 BATTLE GAME STARTING.... 🎮")
    print("\nWelcome to the Character Battle Arena!")
    
    while True:
        print("\nMain Menu:")
        print("1. Create a character")
        print("2. View all characters")
        print("3. Battle between two characters")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            create_character()
        elif choice == '2':
            display_all_characters()
        elif choice == '3':
            if len(all_characters) < 2:
                print("\nNot enough characters to battle. Create at least two characters.")
                continue
            
            print("\n🎯 Player 1, choose your character:")
            char1 = select_character()
            
            print("\n🎯 Player 2, choose your character:")
            char2 = select_character()
            
            print("\n⚔️ BATTLE STARTED! ⚔️")
            print(f"\n⚔️ {char1['name']} vs {char2['name']} ⚔️")
            
            while char1['health'] > 0 and char2['health'] > 0:
                # Player 1 attacks first
                char2 = battle(char1, char2)
                if char2['health'] <= 0:
                    print(f"\n💀 {char2['name']} is defeated!")
                    print(f"🏆 {char1['name']} WINS! 🏆")
                    break
                
                # Wait 1 second before next round
                time.sleep(1)
                
                # Player 2 attacks next
                char1 = battle(char2, char1)
                if char1['health'] <= 0:
                    print(f"\n💀 {char1['name']} is defeated!")
                    print(f"🏆 {char2['name']} WINS! 🏆")
                    break
                
                # Wait 1 second before next round
                time.sleep(1)

        elif choice == '4':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
