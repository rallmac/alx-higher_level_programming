#!/usr/bin/python3

import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + '.json'
        with open(file_name, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return json.loads(json_string)
        
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return (dummy_instance)
    
    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + '.json'
        try:
            with open(file_name, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return ([cls.create(**dictionary) for dictionary in dictionaries])
        except FileNotFoundError:
            return ([])
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        file_name = cls.__name__ + '.csv'
        with open(file_name, 'w') as file:
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.get_width()},{obj.get_height()},{obj.get_x()},{obj.get_y()}\n")
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.get_size()},{obj.get_x()},{obj.get_y()}\n")

    @classmethod
    def load_from_file_csv(cls):
        file_name = cls.__name__ + '.csv'
        try:
            instances = []
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if cls.__name__ == 'Rectangle':
                        id, width, height, x, y = map(int, data)
                        instances.append(cls.create(id=id, width=width, height=height, x=x, y=y))
                    elif cls.__name__ == 'Square':
                        id, size, x, y = map(int, data)
                        instances.append(cls.create(id=id, size=size, x=x, y=y))
            return instances
        except FileNotFoundError:
            return ([])