class Person:
    def __init__(self, initialAge):
        # Check if the initialAge is negative
        if initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        # Perform age-related checks and print the appropriate message
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person by 1
        self.age += 1

# Input number of test cases
t = int(input())

for i in range(t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(3):
        p.yearPasses()
    p.amIOld()
    print("")
