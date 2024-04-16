#!/usr/bin/python3

def inherits_from(obj, a_class):
    obj_class = type(obj)

    if obj_class == a_class:
        return True

    for base_class in obj_class.__bases__:
        if inherits_from(base_class, a_class):
            return True
    
    return False
