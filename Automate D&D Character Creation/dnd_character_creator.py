import random


############ Define Character Components ############

# Races with ability score bonuses
RACES = {
    "Human": {"str": 1, "dex": 1, "con": 1, "int": 1, "wis": 1, "cha": 1},
    "Elf": {"dex": 2},
    "Dwarf": {"con": 2},
}

# Classes with hit dice and primary abilities
CLASSES = {
    "Fighter": {"hit_die": 10, "primary_abilities": ["str", "con"]},
    "Wizard": {"hit_die": 6, "primary_abilities": ["int", "wis"]},
}

# Backgrounds with skill proficiencies
BACKGROUNDS = {
    "Soldier": {"skills": ["Athletics", "Intimidation"]},
    "Scholar": {"skills": ["Arcana", "History"]},
}

# Ability score modifiers
def ability_modifier(score):
    return (score - 10) // 2

# Rolling for ability scores (4d6, drop the lowest)
def roll_ability_scores():
    return sorted([sum(sorted([random.randint(1, 6) for _ in range(4)])[1:]) for _ in range(6)], reverse=True)

# Point-buy system for ability scores
def point_buy_ability_scores():
    point_buy = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
    points = 27
    scores = {"str": 8, "dex": 8, "con": 8, "int": 8, "wis": 8, "cha": 8}

    print("\nPoint Buy System")
    print("You have 27 points to distribute among your abilities.")
    print("The cost to raise an ability score:")
    for score, cost in point_buy.items():
        print(f"Score {score}: {cost} points")
    
    for ability in scores:
        while True:
            print(f"\nCurrent points: {points}")
            current_score = scores[ability]
            print(f"Current {ability.upper()} score: {current_score}")
            new_score = int(input(f"Enter new score for {ability.upper()} (8-15): "))
            if new_score < 8 or new_score > 15:
                print("Score must be between 8 and 15.")
                continue
            cost = point_buy[new_score] - point_buy[current_score]
            if cost <= points:
                scores[ability] = new_score
                points -= cost
                break
            else:
                print("Not enough points. Try a lower score.")

    return scores

# Choose method for generating ability scores
def choose_ability_score_method():
    while True:
        method = input("Choose ability score generation method (roll/point-buy): ").strip().lower()
        if method == "roll":
            return roll_ability_scores()
        elif method == "point-buy":
            return point_buy_ability_scores()
        else:
            print("Invalid choice. Please choose 'roll' or 'point-buy'.")


############ Character Creation Process ############

# Select race and apply racial bonuses
def choose_race():
    print("Available Races: ", ", ".join(RACES.keys()))
    while True:
        race = input("Choose a race: ")
        if race in RACES:
            return race, RACES[race]
        else:
            print("Invalid race. Please choose from the available options.")


# Select class and get hit die and primary abilities
def choose_class():
    print("Available Classes: ", ", ".join(CLASSES.keys()))
    while True:
        cls = input("Choose a class: ")
        if cls in CLASSES:
            return cls, CLASSES[cls]
        else:
            print("Invalid class. Please choose from the available options.")

# Select background and get skill proficiencies
def choose_background():
    print("Available Backgrounds: ", ", ".join(BACKGROUNDS.keys()))
    while True:
        background = input("Choose a background: ")
        if background in BACKGROUNDS:
            return background, BACKGROUNDS[background]
        else:
            print("Invalid background. Please choose from the available options.")

# Assign ability scores
def assign_ability_scores(ability_scores):
    abilities = ["str", "dex", "con", "int", "wis", "cha"]
    assigned_scores = {}
    print("\nAvailable ability scores to assign:", ability_scores)
    
    for ability in abilities:
        while True:
            try:
                score = int(input(f"Assign score to {ability.upper()}: "))
                if score in ability_scores:
                    assigned_scores[ability] = score
                    ability_scores.remove(score)
                    break
                else:
                    print(f"Invalid score. Please choose from the available scores: {ability_scores}")
            except ValueError:
                print("Please enter a valid number.")
    
    return assigned_scores

############ Display Character Sheet ############

def display_character_sheet(name, race, cls, background, ability_scores, race_bonuses):
    print("\n--- Character Sheet ---")
    print(f"Name: {name}")
    print(f"Race: {race}")
    print(f"Class: {cls}")
    print(f"Background: {background}")
    print("\nAbility Scores:")
    for ability, score in ability_scores.items():
        total_score = score + race_bonuses.get(ability, 0)
        print(f"{ability.upper()}: {total_score} (Mod: {ability_modifier(total_score)})")
    print("-----------------------")

# Main function to create a character
def create_character():
    name = input("Enter your character's name: ")
    race, race_bonuses = choose_race()
    cls, class_details = choose_class()
    background, background_details = choose_background()
    ability_scores = roll_ability_scores()
    print(f"Ability Scores: {ability_scores}")
    if isinstance(ability_scores, list):
        assigned_scores = assign_ability_scores(ability_scores)
    else:
        assigned_scores = ability_scores
    display_character_sheet(name, race, cls, background, assigned_scores, race_bonuses)

# Run the character creation process
if __name__ == "__main__":
    create_character()

