

class Employee :
    def __init__(self, name, email, cno, nid):
        self.name = name
        self.email = email
        self.cno = cno
        self.nid = nid
class Engineer(Employee) :
    # tech, exp
    def __init__(self, name, email, cno, nid, tech, exp):
        super().__init__(name, email, cno, nid)
        # Employee.__init__(self, name, email, cno, nid)
        self.tech = tech
        self.exp = exp

class Salesman(Employee) :
    def __init__(self, name, email, cno, nid, profile, reputation):
        super().__init__(name, email, cno, nid)
        self.profile = profile
        self.reputation = reputation

eng1 = Engineer("ABC", "abc@xyz", 111, 111, "spark", 4 )