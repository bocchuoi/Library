class Person:
    def __init__(self, id, firstName, lastName, email):
        self._id = id
        self._firstName = firstName
        self._lastName = lastName
        self._email = email

    @property
    def firstName(self):
        return self._firstName

    @property
    def lastName(self):
        return self._lastName
