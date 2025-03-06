import copy
from abc import ABC, abstractmethod

# Prototype Interface
class ICloneable(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete Prototype Class
class Car(ICloneable):
    def __init__(self, model, features):
        self.model = model
        self.features = features  # Mutable object (list)

    def clone(self):
        clone_car = Car(self.model, self.features.copy()) # [Character(), Character()]
        return copy.deepcopy(self)  # ✅ Deep copy (fixes the problem)

    def __str__(self):
        return f"Car(model={self.model}, features={self.features})"

# Client Code
original_car = Car("Sedan", ["Air Conditioning", "ABS", "Sunroof"])
cloned_car = original_car.clone()

# Modifying the cloned object's features
cloned_car.features.append("GPS")

# Output
print("Original Car:", original_car)  # 🎯 Unchanged!
print("Cloned Car:", cloned_car)
