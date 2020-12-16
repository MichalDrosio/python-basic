class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f'{self.__class__.__name__}(string="{self.string})"'

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(f'{self.string} {other.string}')

    def __lt__(self, other):
        return len(self.string) < len(other.string)

    def __iadd__(self, other):
        return Doc(f'{self.string}&{other.string}')


doc1 = Doc('Python')
doc2 = Doc('3.9')
print(doc1+doc2)
print(doc1 < doc2)
doc1 += doc2
print(doc1)

class Hashtag:
    def __init__(self, string):
        self.string = f'#{string}'

    def __repr__(self):
        return f'Hastag(string="{self.string}")'

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Hashtag(f'{self.string[1:] + other.string}')


h1 = Hashtag('python')
h2 = Hashtag('developer')
h3 = Hashtag('opp')
print(h1+h2+h3)