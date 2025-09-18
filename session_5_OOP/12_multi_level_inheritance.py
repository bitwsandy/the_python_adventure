# Multilevel inheritance involves a child and grandchild relationship
# where features are passed down the lineage.

class Grandfather:
    def skills(self):
        print("Tall")
    def grandfther_skills(self):
        print("Tall")

class Father(Grandfather):  # Inherits from Grandfather
    def skills(self):
        # Grandfather.skills(self)
        super().skills()
        print("Programming")

    def father_skills(self):
        print("Programming")

class Son(Father):  # Inherits from Father
    def skills(self):
        # Father.skills(self)
        super().skills()
        print("Gaming")

    def son_skills(self):
        print("Gaming")

# Usage
son = Son()
son.skills()

son.grandfther_skills()
son.father_skills()
son.son_skills()
