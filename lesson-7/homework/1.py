import math

class Vector:
    def __init__(self, *components):
        self.components = components
    
    def __repr__(self):
        return f"Vector{self.components}"
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for addition.")
        
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for subtraction.")
        
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must be of the same dimension for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            raise ValueError("Unsupported operation.")
    
    def __rmul__(self, other):
        return self * other
    
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))
    
    def normalize(self):
        mag = self.magnitude()

        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        
        return Vector(*(round(a / mag, 3) for a in self.components))

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)
print(v1 + v2)
print(v2 - v1)
print(v1 * v2)
print(3 * v1)
print(v1.magnitude())
print(v1.normalize())