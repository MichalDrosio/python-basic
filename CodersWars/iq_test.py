# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers
# differs from the others. Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program that among the given numbers finds one
# that is different in evenness, and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test,
# which means indexes of the elements start from 1 (not 0)


# def iq_test(numbers):
#     numbers_array = numbers.split()
#     print(numbers_array)
#     odd_num= []
#     even_num = []
#     for i in numbers_array:
#         if int(i) % 2 == 0:
#             even_num.append(i)
#         else:
#             odd_num.append(i)
#     if len(odd_num) == 1:
#         return numbers_array.index(odd_num[0]) +1
#     else:
#         return numbers_array.index(even_num[0]) + 1

def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    print(e)

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))



