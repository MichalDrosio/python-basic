# The drawing below gives an idea of how to cut a given "true" rectangle into squares
# ("true" rectangle meaning that the two dimensions are different).
# Can you translate this drawing into an algorithm?
#
# You will be given two dimensions
#
# a positive integer length
# a positive integer width
# You will return a collection or a string (depending on the language; Shell bash, PowerShell,
# Pascal and Fortran return a string) with the size of each of the squares.

def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    if lng < wdth:
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res


print(sq_in_rect(5, 3))