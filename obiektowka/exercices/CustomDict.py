class CustomDict(dict):

    def is_any_str_value(self):
        flag = False
        for key in self:
            if isinstance(self[key], str):
                flag = True
                break
        return flag


class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only objects of type str can be added to the lsit')
        super().append(string.lower())

slo = StringListOnly()
slo.append('data')
slo.append('science')
print(slo)