#Creat Patient Class
class Patient:
    def display_patient_type(self): #Patients Function
        print("Patient Type: Regular Patient") #Standard Parent Class where the subclasses of Senior and Philhealth will base off and 'morph' from.


class SeniorPatient(Patient): #Inherit Parent + Functions
    def display_patient_type(self):
        print("Patient Type: Senior Citizen") #As seen here, the subclass uses the same function: "def display_patient_type(self):", however, it's output in print is different from its parent class, which is essentially its unique morph.


class PhilhealthPatient(Patient):
    def display_patient_type(self):
        print("Patient Type: PhilHealth Member") #Same here


#This will create the different patient objects, from class to variables
patient1 = Patient()
patient2 = SeniorPatient()
patient3 = PhilhealthPatient()

#This will then display patient types, variebles calling a function that will pull an output from their classes.
patient1.display_patient_type()
patient2.display_patient_type()
patient3.display_patient_type()

