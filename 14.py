class Mail:

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message


class MailServer:

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users.update({user: []})

    def add_mail(self, user, mail):
        self.users[user].append(mail)

    def get_mail(self, user):
        return self.users[user]


class MailClient:

    def __init__(self, server, user):
        self.server = server
        self.user = user
        self.server.add_user(self.user)

    def receive_mail(self):
        return self.server.get_mail(self.user)

    def send_mail(self, server_to, user_to, mail):
        server_to.add_mail(user_to, mail)


server_A = MailServer()
server_B = MailServer()
user1 = MailClient(server_A, 'user1')
user2 = MailClient(server_B, 'user2')
user1.send_mail(server_B, 'user2', Mail('Hello'))
user1.send_mail(server_B, 'user2', Mail('World'))
messages = user2.receive_mail()
for i in messages:
    print(i.get_message())
