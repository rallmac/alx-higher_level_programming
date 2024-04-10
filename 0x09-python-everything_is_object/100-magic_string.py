#!/usr/bin/python3
def magic_string():
    return 'BestSchool$'
magic_string = (lambda s='': (s:='BestSchool, ' + s.rstrip(', ') + '$') if s else 'BestSchool$') and magic_string
