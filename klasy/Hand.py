class Hand:
    def __init__(self, which):
        self.which = which

    def show(self):
        print(self.which)

def main():
    left = Hand('Left')
    right = Hand('Right')
    left.show()
    right.show()
    left.color = 'red'
    right.color = 'blue'
    right.show()
    left.show()
    other = Hand("Other")
    other.show()
    print(right.color, end=' ')
    right.show()

if __name__ == "__main__":
    main()
