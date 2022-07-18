"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        '''Create a new generator'''
        self.start = self.next = start

    def __repr__(self):
        '''A representation of the generator object'''
        return f'A counter that starts at {self.start} and is currently at {self.next}'
    
    def __str__(self):
        '''Return a human readable version of the generator'''
        return self.describe()

    def generate(self):
        '''Return the counter, adding one everytime the function is called'''
        self.next += 1
        return self.next - 1
    
    def reset(self):
        '''Resets the counter'''
        self.next = self.start
    
    def describe(self):
        '''Returns a string representing the counter'''
        return f'The counter starts at {self.start} and is currently at {self.next}'


    
