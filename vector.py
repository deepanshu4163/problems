
class Vector:
    vec = []

    def create(self, vec):
        self.vec = vec

    def modify(self, element, value):
        self.vec[element - 1] = value

    def multiply(self, scalar):
        for i in range(len(self.vec)):
            self.vec[i] = self.vec[i] * scalar

    def display(self):
        print("---------")
        for i in self.vec:
            print(i)
            
        print("---------")    


def main():
    v1 = Vector()
    choice = 1
    while choice != 5:

        print("1.Create")
        print("2.Modify")
        print("3.Multiply")
        print("4.Display")
        print("5.Exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            vec = []
            number_of_items = int(input("enter no. of items:"))

            for i in range(0, number_of_items):
                value = float(input("enter value of the item:"))
                vec.append(value)
 
            v1.create(vec)

        elif choice == 2:
            element = int(input("enter the element you wish to modify:"))
            value = float(input("enter the value:"))

            v1.modify(element, value)
        
        elif choice == 3:
            scalar = int(input("enter the scalar:"))

            v1.multiply(scalar)

        elif choice == 4:
            v1.display()




if __name__ == "__main__":
    main()
