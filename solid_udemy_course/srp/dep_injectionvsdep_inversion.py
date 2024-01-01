"""
Dependency Injection
"""

"""
Lets first understand in very simple terms what is dependency Injection

=> You are making a sandwich -> U need bread, cheese, ham
=> Your core job is to make the sandwich -> But you need the depedencies bread, cheese, ham -> To make the sandwich

IF USING DEPENDENCY INJECTION CONCEPT
=> One way is to get these depedencies from a 3rd party
Lets do you do bigbasket -> And the guy delivers you the depdencies

i) You can now solely focus on making the sandwich
ii) You are solely focussed on preparing for the sandwich 
-> Setting the sandwich maker, getting the sauces & veggies ready
iii) When the big basket guy comes with depdencies of bread, ham and cheese 
-> You inject those dependencies -> In your sandwich

IF NOT USING DEPENDENCY INJECTION CONCEPT
=> Then I have to myself take care of getting bread, ham and cheese
=> So instead of doing the core job of creating the sandwich
=> I will also have to take care of getting all the dependencies


Now lets see in terms of coding

What is dependency ?
i) When class A uses some other class B to access one of its feature.
A->B => A is dependent on B

ii) For example lets say my model class Model is using DB class
Model->DB => Model is dependent on DB


Injecting Dependency
i) In general case -> 
When Class A -> Wants to use Class B -> Its needs to instantiate object of Class B in class A
In this way Class A and Class B are tightly coupled

ii) In case of dependency Injection
-> Object of class B is passed in Class A via constructor when instantiating object of class A
-> Object of class B is set by setter methods

"""

"""
Code example without DI
Person and Job Class
"""

# Job class remains the same
class Job:
    def __init__(self, title):
        self.title = title

# Person class without dependency injection
class Person:
    def __init__(self, name):
        self.name = name
        # Create a Job object within the Person class
        self.job = Job("Default Job")

    def display_info(self):
        print(f"{self.name} works as a {self.job.title}")

# Create a Person instance without providing a Job object
john = Person("John")

# Display information using the Person instance
john.display_info()

"""
In this example, there is Job Class and a Person Class. Person Class has a job

i) Each person is instantiated with a default job
ii) Now I want to change the job of the person. 
-> I have to either pass job title in Person class constructor, so that it can be passed to Job Class
or
-> Make a function to change the job of the person

Person Class and Job Class are ***very tightly coupled***. 
-> Lets say tomorrow I make a change in the Job class, adding a new parameter in the constructor
-> The person class will also need to be changed to accomodate the parameter in Job class instantiation

-> Give rise to RIGIDITY, REDUCES FLEXIBILITY OF CODE

"""

"""
Code with DI person and job class
"""
# Job class remains the same
class Job:
    def __init__(self, title):
        self.title = title

# Person class with dependency injection
class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def display_info(self):
        print(f"{self.name} works as a {self.job.title}")

# Create a Job instance
software_engineer = Job("Software Engineer")

# Create a Person instance with dependency injection
john = Person("John", software_engineer)

# Display information using the Person instance
john.display_info()


"""
Here person and Job class are very loosely coupled

i) Job class Object is passed as an argument to the constructor of Person class
ii) When person class is instantiated -> Job object is passed in as argument
iii) Different types of job object is passed easily to Person class
iv) Any changes in the Job class -> will not require any changes in the function class

Person class is not bothered by -> Code changes in the Job Class
"""


