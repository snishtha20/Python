# Write OOP classes to handle the following scenarios:
# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line

class Point:

    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod, self.y_cod)
    
    def eucledian_distance(self,a):
        return ((a.x_cod-self.x_cod)**2 + (a.y_cod-self.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return ((self.x_cod)**2 + (self.y_cod)**2)**0.5
    

class Line:
    def __init__(self,a,b,c):
        self.A = a
        self.B = b
        self.C = c

    def __str__(self):
        return '{}x + {}y + {}'.format(self.A, self.B, self.C)
    
    def point_on_line(self,a):
        if self.A * a.x_cod + self.B * a.y_cod + self.C == 0:
            return 'Point lie on line'
        else:
            return 'Not lie on line' 
        
    def distance_from_point(self,a):
        new_num = abs(self.A*a.x_cod + self.B * a.y_cod + self.C)
        new_den = (self.A**2 + self.A**2)*0.5
        return new_num/new_den

p = Point(3,4)
print(p)
q = Point(4,5)
print(p.eucledian_distance(q))
print(p.distance_from_origin())

a = Line(3,4,5)
print(a)

b = Line(1,1,-2)
r = Point(1,1)
print(b.point_on_line(r))

print(b.distance_from_point(r))

s = Point(3,4)
print(a.distance_from_point(s))