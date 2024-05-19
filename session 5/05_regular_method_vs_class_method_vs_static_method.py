class GameCharacter:
    total_characters = 0  # Class variable to track the number of characters created

    def __init__(self, name, level):
        self.name = name  # Instance variable for the character's name
        self.level = level  # Instance variable for the character's level
        GameCharacter.total_characters += 1  # Increment the class variable

    # Regular method: Used to display character details
    def display_character(self):
        print(f"{self.name} is at level {self.level}.")

    # Class method: Used to create an instance of gameCharacter class
    @classmethod
    def from_string(cls, gameCharStr):
        name, level = gameCharStr.split('-')
        return cls(name,level)

    @classmethod
    def reset_count(cls):
        cls.total_characters = 0 


    # Static method: Used to determine if a level upgrade is allowed
    @staticmethod
    def can_level_up(experience_points):
        return experience_points >= 1000

# Create instances of GameCharacter
character1 = GameCharacter("Link", 5)
character2 = GameCharacter("Zelda", 7)

# Call regular method: it uses instance attributes
character1.display_character()  # Outputs: Link is at level 5.
character2.display_character()  # Outputs: Zelda is at level 7.

# Call class method: it affects class state, not dependent on any instance
newGameChar1 = 'crimson-11'
character3 = GameCharacter.from_string(newGameChar1)
character3.display_character()

# Call static method: performs a utility task, checking if a level can be upgraded
print(GameCharacter.can_level_up(1200))  # Outputs: True
print(GameCharacter.can_level_up(800))   # Outputs: False

print(GameCharacter.total_characters)
GameCharacter.reset_count()
print(GameCharacter.total_characters)

# Regular Method (display_character):
#       Uses self to access and display instance-specific data such as the character's
#       name and level.
# Class Method (from_string):
#       Uses cls to access and manipulate data related to the class as a whole, like the total
#       number of game characters created. Useful for actions that affect the entire class rather
#       than individual instances.
# Static Method (can_level_up):
#       Does not need access to either instance-specific data or class-specific data. It simply
#       provides utility functionality to determine if a character can level up based on
#       experience points, making it completely independent of the character's state.


# Study Drills :
# 1. Try to run class method using instances and Using class figure out the difference
# 2. Create GamePlayer from a String with and without class method
#