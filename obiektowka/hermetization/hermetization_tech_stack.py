class TechStack:
    def __init__(self, tech_names):
        self._tech_names = tech_names

    @property
    def tech_names(self):
        return self._tech_names

    @tech_names.setter
    def tech_names(self, value):
        self._tech_names = value

    @tech_names.deleter
    def tech_names(self):
        del self._tech_names


tech = TechStack('python')
print(tech.tech_names)
tech.tech_names = 'sql'
print(tech.tech_names)
del tech.tech_names
print(tech.__dict__)
