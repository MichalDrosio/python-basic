def function(idx, array=[]):
    for i in range(idx):
        array.append(i**3)
    print(array)

function(4)
function(5, ['a', 'b', 'c'])
function(6)
function(2, ['a'])
function(3)

def function_2(*args, **kwargs):
    print(args, kwargs)

function_2(3, 4)
function_2(x=3, y=4)
function_2(1,2, x=3, y=4)