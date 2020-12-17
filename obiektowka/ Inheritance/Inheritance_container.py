class Container:
    category = 'general purpose'


class PlasticContainer(Container):
    pass


class MetalContainer(Container):
    pass


class CustomContainer(Container):
    pass


class SmallPlasticContainer(PlasticContainer):
    pass


class TemperatureControlledContainer(Container):
    temp_range = (-25.0, 25.0)


class RefrigeratedContainer(TemperatureControlledContainer):
    temp_range = (-25.0, 5.0)


array_classes = [PlasticContainer, MetalContainer, CustomContainer, SmallPlasticContainer,
                 TemperatureControlledContainer, RefrigeratedContainer]

for c in array_classes:
    print(issubclass(c, Container))

print(SmallPlasticContainer.mro())
print(getattr(RefrigeratedContainer, 'temp_range'))
print(getattr(TemperatureControlledContainer, 'temp_range'))