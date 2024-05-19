# Multilevel inheritance involves a child and grandchild relationship
# where features are passed down the lineage.

class Grandfather:
    def height(self):
        print("Tall")

class Father(Grandfather):  # Inherits from Grandfather
    def skills(self):
        print("Programming")

class Son(Father):  # Inherits from Father
    def skills(self):
        super().skills()
        print("Gaming")

# Usage
son = Son()
son.height()  # Outputs: Tall
son.skills()  # Outputs: Programming, Gaming
