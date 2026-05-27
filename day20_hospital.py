from abc import ABC, abstractmethod
class Person(ABC):

    @abstractmethod
    def display(self):
        pass



class Doctor(Person):
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization


    def display(self):
        print("----- Doctor Details -----")
        print(f"Doctor Name: {self.name}")
        print(f"Specialization: {self.specialization}")


class Patient(Person):
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease


    def display(self):
        print("----- Patient Record -----")
        print(f"Patient Name: {self.name}")
        print(f"Disease: {self.disease}")


class Appointment:
    def __init__(self, patient_name, doctor_name, date):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date

    def booking(self):
        print("----- Appointment Booking -----")
        print(f"Patient: {self.patient_name}")
        print(f"Doctor: {self.doctor_name}")
        print(f"Date: {self.date}")


class Billing:
    def __init__(self, patient_name, amount):
        self.patient_name = patient_name
        self.amount = amount

    def bill(self):
        print("----- Billing System -----")
        print(f"Patient: {self.patient_name}")
        print(f"Bill Amount: ₹{self.amount}")



d1 = Doctor("Dr. Sharma", "Cardiologist")
p1 = Patient("Rahul", "Fever")

a1 = Appointment("Rahul", "Dr. Sharma", "10 May 2026")

b1 = Billing("Rahul", 5000)


d1.display()
print()
p1.display()
print()
a1.booking()
print()
b1.bill()