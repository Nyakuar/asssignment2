class Student:
    school="Akirachix"
    def __init__(self,firstname,lastname,age,country):
        self.firstname=firstname
        self.age=age 
        self.country=country
        self.lastname=lastname

   # def greet(self):
        #return f"Hello {self.name} welcome to {self.school},How is {self.country}"

    def full_name(self):
        return f"Hello your full name is {self.firstname } {self.lastname} "

    def years_of_birth(self)  :
       year_of_birth=2022-self.age
       return f"Hello your year of birth is {year_of_birth}"


    def your_initials(self):
        return f"Hello your initial is {self.firstname[0]}{self.lastname[0]}"
    