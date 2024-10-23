class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        repr = f"{self.x}i\u0302 {self.y:+}j\u0302 {self.z:+}k\u0302"
        return repr


if __name__ == "__main__":
    v1 = Vector(1,3,6)
    v2 = Vector(-2,0,4)
    v3 = Vector(0,0,4)
    print(v1)
    print(v2)
    print(v3)
    print("k"+"\u0302")
