from copy import deepcopy

from utils import add_dictionaries


class AddressBook:
    def __init__(self, content=None):
        """
        Initialize internal dictionary and pre-populate
        """
        self.content = dict()
        if isinstance(content, dict):
            if content.get(1):
                self.content = deepcopy(content)
            else:
                self.content[1] = deepcopy(content)

    def add_content(self, content):
        """
        Add address content
        """
        index = len(self.content) + 1
        self.content[index] = deepcopy(content)

    def count(self):
        """
        Return the length of the dictionary
        """
        return len(self.content)

    def __add__(self, other):
        """
        Add two address book instances together
        OR
        Add a dictionary to the existing address book
        """
        if isinstance(other, AddressBook):
            return AddressBook(add_dictionaries(self.content, other.content))
        if isinstance(other, dict):
            self.add_content(other)
            return AddressBook(self.content)
        else:
            err_msg = "unsupported operand type(s) for +: '{}' and '{}'"
            raise TypeError(err_msg.format(type(self), type(other)))

    def __iter__(self):
        """
        Override the iterator to return the internal dictionaries
        """
        for value in self.content.itervalues():
            yield value

    def __enter__(self):
        """
        Define the setup for a "with" statement
        """
        names = list()
        for value in self.content.itervalues():
            names.append(
                '{} {}'.format(value['first_name'], value['last_name']))
        return names

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Define tear down and suppress exceptions for "with" statement
        """
        return isinstance(exc_val, IndexError)
