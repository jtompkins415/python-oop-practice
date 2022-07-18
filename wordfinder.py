"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    '''Searches for a random word in a file/dictionary of words'''
    
    def __init__(self, path):
        '''Initilizes word finder and returns number of words in the file/dictionary'''
        dict_file = open(path)
        self.dict = self.parse_dict(dict_file)
        print(f'{len(self.dict)} words read')
    
    def parse_dict(self, dict_file):
        '''Parses the words in the dictionary so they can be counted'''
        return [w.strip() for w in dict_file]
    
    def random_word(self):
        '''Returns a random word from the dictionary'''
        return random.choice(self.dict)


class SpecialWordFinder(WordFinder):
    '''Searches for a random word in a dictionary while excluding spaces/special characters'''

    def __init__(self, path):
        '''Initialize word finder and accesses the functionality of the parent class (Wordfinder)'''
        super().__init__(path)

    def parse(self, dict_file):
        '''Parses the dictionary and excludes all spaces and special characters'''
        return [w.strip() for w in dict_file if w.strip() and not w.startswith('#')]
