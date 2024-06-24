# Child - Parent Relationship
# Defining class Polygon
class Polygon:
    # initiating the class
    def __init__(self,sideList):
        self.sideList = sideList
    
    # defining function display
    def display(self):
        print('A polygon is a two dimensional shape with straight lines')
    
    # function to calculate and return perimeter
    def perimeter(self):
        return sum(self.sideList) # return sum of sides

# Defining class Triangle as child of class Polygon
class Triangle(Polygon):
    
    # defining function display
    def display(self):
        print('A triangle is a polygon with 3 edges')
        super().display()  #calss parent display function
    
    # function to print perimeter
    def get_perimeter(self):
        return f'of Triangle: {self.perimeter()}'

# Defining class Quadrilateral as child of class Polygon
class Quadrilateral(Polygon):
    
    # defining function display
    def display(self):
        print('A quadrilateral is a polygon with 4 edges')
    
    # function to print perimeter   
    def get_perimeter(self):
        return f'of Quadrilateral: {self.perimeter()}'

#defining the main function
def main():
    t1 = Triangle([9, 8, 9])
    t2 = Quadrilateral([5, 6, 7, 9])
    perimeter = t1.get_perimeter()
    perimeter2 = t2.get_perimeter()
    print("Perimeter", perimeter)
    print("Perimeter", perimeter2)
    t1.display()
    t2.display()

#To check python interpreter and call main function    
if __name__ == "__main__" :
    main()