class SomeList:
    def __init__(self):
        self._some_list = []

    def add_element(self, element):
        self._some_list.append(element)

    def remove_element(self):
        self._some_list.pop()

    def __len__(self):
        return len(self._some_list) 


s = SomeList()
s.add_element(1)
s.add_element(4)
s.add_element(7)
s.add_element(9)
print(len(s))
print(s.__len__())