text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""

result = []
words = text.lower()
words = words.split()
words = [word.replace('.', '').replace(',', '') for word in words]
words = [ word for word in words if len(word) > 10]
print(words)
