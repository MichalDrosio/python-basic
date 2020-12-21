class ClientList(list):
    def search_email(self, value):
        result = [client for client in self if value in client.email]
        return result


class Client:
    all_clients = ClientList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, email={self.email})'


client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@yahoo.com')
client3 = Client('Mike', 'sales-contact@yahoo.com')
client4 = Client('Lisa', 'info@gmail.com')
print(Client.all_clients)
print(Client.all_clients.search_email('gmail'))

for client in Client.all_clients.search_email('gmail'):
    print(client)





