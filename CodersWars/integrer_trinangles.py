# You have to give the number of different integer triangles with one angle of 120 degrees which
# perimeters are under or equal a certain value. Each side of an integer triangle is an integer value.
# give_triang(max. perimeter) --------> number of integer triangles,
# with sides a, b, and c integers such that:
#
# a + b + c <= max. perimeter
#
# See some of the following cases
def give_triang(per):
    result = []
    for x in range(3, per):
        if 2 * x > per:
            break
        for y in range(x, per):
            if x + 2 * y > per:
                break
            z = (x * x + x * y + y * y) ** 0.5
            if z == int(z) and x + y + z <= per:
                result.append((x, y, z))
    return result
print(give_triang(50))
