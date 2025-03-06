import copy
from abc import ABC, abstractmethod

# Prototype Interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete Prototype Class
class Car(Prototype):
    def __init__(self, model, features):
        self.model = model
        self.features = features  # Mutable object (list)

    def clone(self):
        #return copy.copy(self)  # 🚨 Shallow copy (problematic)
        return Car(self.model, self.features)

    def __str__(self):
        return f"Car(model={self.model}, features={self.features})"

# Client Code
original_car = Car("Sedan", ["Air Conditioning", "ABS", "Sunroof"])
cloned_car = original_car.clone()

# Modifying the cloned object's features
cloned_car.features.append("GPS")

# Output
print("Original Car:", original_car)  # 🚨 Modified! Affects original
print("Cloned Car:", cloned_car)
