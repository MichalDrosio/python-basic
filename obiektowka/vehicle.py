class Vehicle:
    """This is a Vehicle class."""

print(type(Vehicle))
print(Vehicle.__name__)
print(Vehicle.__dict__.keys())
print(Vehicle.__module__)
v = Vehicle()
print(isinstance(v, Vehicle))