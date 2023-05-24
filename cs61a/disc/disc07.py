class Student:
    extension_days = 3

    def __init__(self, name, staff):
        self.name = name
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_extension_days(self, student, days):
        student.extension_days = days
# ---------------- problem 2 ------------------------------------------------------------------
class Server:
    """Each Server has an instance attribute clients, which
        is a dictionary that associates client names with
        client objects.
        """

    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        "*** YOUR CODE HERE ***"
        # This will access the servers clients dict and look for the key that is assosciated with the recipient
        # name attached to the email.
        client = self.clients[email.recipient_name]
        # this will put the email in the client's mailbox, which is implemented below
        client.recieve(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        "*** YOUR CODE HERE ***"
        # we don't use self.client_name, or self.client here because our server object does not actually store
        # those attributes. for this function they will have to be provided as arguments.
        # without this function clients will not be reachable because they will not be stored within
        # the clients dict on the server, so looking them up would be impossible
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    """
    def __init__(self, server, name):
        self.inbox = []
        "*** YOUR CODE HERE ***"
        self.server = server
        self.name = name
        # this will add the client to the server. if we did not do this they would not be stored in the clients
        # dict on the server and would then be impossible to reach
        self.server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        "*** YOUR CODE HERE ***"
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        "*** YOUR CODE HERE ***"
        self.inbox.append(email)

class Email:
    """Every email object has 3 instance attributes: the
       message, the sender name, and the recipient name.
       >>> email = Email('hello', 'Alice', 'Bob')
       >>> email.msg
       'hello'
       >>> email.sender_name
       'Alice'
       >>> email.recipient_name
       'Bob'
       """

    def __init__(self, msg, sender_name, recipient_name):
        "*** YOUR CODE HERE ***"
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


# -------- Inheritance ---------------------------------------------------------------
class Pet:

    def __init__(self, name, owner):
        self.name = name
        self.is_alive = True
        self.owner = owner

    def eat(self, thing):
        print(f' {self.name} ate a {thing}!')

    def talk(self):
        print(self.name)

class Dog(Pet):

    # ---------Class Methods ---------------------------------------------------------

    @classmethod
    def robo_factory(cls, owner):
        return cls("RoboDog", owner)

    def talk(self):
        super().talk()
        print('This Dog says woof!')

class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives

    @classmethod
    def cat_creator(cls, owner):
        name = f"{owner}'s Cat"
        return cls(name, owner)

    def talk(self):
        print(f'{self.name} says meow')

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            is_alive = False
            print('This cat has no more live to lose')

class NoisyCat(Cat):

    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner, lives)

    def talk(self):
        print(f'{self.name} says meow')
        print(f'{self.name} says meow')


