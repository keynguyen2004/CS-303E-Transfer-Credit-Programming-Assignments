class Lit:
    def __init__(self, exp, simp = None):
        self.exp = exp
        if (simp != None):
            self.simp = simp
        else:
            self.simp = exp

    def toString(self):
        return self.exp

    def simplify(self):
        return self.simp

    def Add(self, obj2):
        new_exp = "(" + self.exp + " + " + obj2.exp + ")"
        new_simp = str(int(self.simp) + int(obj2.simp))
        return Lit(new_exp, new_simp)

    def Sub(self, obj2):
        new_exp = "(" + self.exp + " - " + obj2.exp + ")"
        new_simp = str(int(self.simp) - int(obj2.simp))
        return Lit(new_exp, new_simp)

    def Mul(self, obj2):
        new_exp = "(" + self.exp + " * " + obj2.exp + ")"
        new_simp = str(int(self.simp) * int(obj2.simp))
        return Lit(new_exp, new_simp)

class Var:
    def __init__(self, exp, simp = None):
        self.exp = exp
        if (simp != None):
            self.simp = simp
        else:
            self.simp = exp

    def toString(self):
        return self.exp
        
    def simplify(self):
        return self.simp