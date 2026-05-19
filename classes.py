class Point: #classes use PascalNamingConvneion
    #defining methods in the body of the class
    def move(self):
        print('move')

    def draw(self):
        print ('draw')

# attributes can be set anywhere in the program
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()