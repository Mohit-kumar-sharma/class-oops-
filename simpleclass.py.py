#------------------ Simple class code ------------------------
class Employee:
    No_of_leaves = 10
    pass

Mohit = Employee()
Kunal = Employee()

Mohit.name = "Mohit sharma"
Mohit.age = 19
Mohit.home = "Hathras"

Kunal.name = "Kunal singh"
Kunal.age = 20
Kunal.home = "Aligarh"
#Employee.No_of_leaves = 20 
print(Kunal.name,Kunal.age,Kunal.No_of_leaves)
print(Mohit.name,Mohit.home,Mohit.No_of_leaves)

print(Mohit.__dict__)
print(Kunal.__dict__)

#------------------class code with init function --------------------------
class Employee:
    No_of_leaves = 30
    def __init__(self,name,age,home,gmail) -> None:
        self.name= name
        self.age = age
        self.home = home
        self.gmail = gmail

Mohit = Employee ("Mohit sharma",19 , "Hathras","Mohitsharmag330@gmail.com")
Kunal = Employee ("Kunal singh" ,  20 , "Aligarh","Kunalsingh400@gmail.com")

print(Kunal.gmail)
print(Mohit.name,Mohit.gmail)
