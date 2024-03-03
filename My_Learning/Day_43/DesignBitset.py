class Bitset:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * size

    def fix(self, idx):
        if 0 <= idx < self.size:
            self.bits[idx] = 1

    def unfix(self, idx):
        if 0 <= idx < self.size:
            self.bits[idx] = 0

    def flip(self):
        for i in range(self.size):
            self.bits[i] ^= 1

    def all(self):
        return all(self.bits)

    def one(self):
        return any(self.bits)

    def count(self):
        return sum(self.bits)

    def toString(self):
        return ''.join(map(str, self.bits))


# Example
bs = Bitset(5)
bs.fix(3)
bs.fix(1)
bs.flip()
print("all:", bs.all())         
bs.unfix(0)
bs.flip()
print("one:", bs.one())         
bs.unfix(0)
print("count:", bs.count())    
print("toString:", bs.toString()) 
