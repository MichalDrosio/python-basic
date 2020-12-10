class Model:
    pass


class View:
    pass


model = Model()
view = View()
print(isinstance(model, Model), isinstance(view, View))

object1 = Model()
object2 = [Model(), View()]
object3 = {}

print(isinstance(object1, (Model, View)))
print(isinstance(object2, (Model, View)))
print(isinstance(object3, (Model, View)))

print(issubclass(Model, object), issubclass(View, object))