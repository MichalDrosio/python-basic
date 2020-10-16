

def triangle_field(base, height):
    field = 0.5 * base * height
    print(field)


def test_triangle_area(capsys):
    # try
    base = 10
    height = 8

    # when
    triangle_field(base, height)
    out, err = capsys.readouterr()

    #then
    assert out == 40