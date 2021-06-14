# You are to write a function that takes an odd integer which is
# the difference between two consecutive perfect squares and find the squares
#
# Input Format
# num : Odd Integer 0<n<1000000
#
# Output Format
# Answer: String containing
# the bigger and smaller squares in one line like "Max-Min"
#
# Examples
# findSquares(9)  //returns '25-16'
# findSquares(5)  // returns '9-4'

def find_squares(num):
    if num % 2 != 0:
        return f'{(num - int(num/2))**2}-{int(num/2)**2}'
    else:
        return None

print(find_squares(9))