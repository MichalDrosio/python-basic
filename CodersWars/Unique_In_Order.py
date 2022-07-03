#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

#For example:

#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    result = []
    if len(iterable) == 1:
        result.append(iterable)
        return result
    elif len(iterable) == 2 and iterable[0] == iterable[1]:
        result.append(iterable[0])
        return result
    else:
        for i in range(len(iterable)):
            if iterable[i] == iterable[i-1]:
                continue
            else:
                result.append(iterable[i])
        return result



def unique(words):
    result = []
    for i in words:
        if len(result) == 0 or i != result[-1]:
            result.append(i)
    return result

