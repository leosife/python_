class Ponto():
    def __init__(self,x,y,z='String'):
        self.x = x
        self.y = y
        self. z = z

    # def __str__(self) -> str:
    #     return f'({self.x},{self.y})' o programa sempre usara primeiro o str e depois o repr

    def __repr__(self):
        # cl = self.__class__.__name__
        cl = type(self).__name__
        return f'{cl} (x={self.x!r},y={self.y!r}),z={self.z!r})'
p1 = Ponto(4,6)
p2 = Ponto(232,222)

print(p1)
print(p2)
# print(repr(p1)) maneiras de se ver o repr quando existir uma __str__
# print(f'{p2!r}') 
# se usa !r para ver repr
