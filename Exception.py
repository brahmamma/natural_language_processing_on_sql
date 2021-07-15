# -*- coding: utf-8 -*
import importlib
import sys


importlib.reload(sys)

class ParsingException(Exception):
    reason = ''
    
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return 'ParsingException : ' + self.reason

class GeneratingException(Exception):
    reason = ''

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return 'GeneratingException : ' + self.reason
