from pprint import pprint
import inspect
import sys

class Pictures:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color #если цвет None, то цвет картины черно-белый

    def change_name(self, newname):
        if isinstance(newname, str):
            self.name = newname
        return self.name

    def change_color(self, color):
        if self.color == None:
            print('цвет нельзя поменять')
        else:
            self.color = color
            print('цвет картины стал черно-белым')
        return self.color

def introspection_info(obj):
    dict_info = {}
    dict_info['type'] = type(obj)
    dict_info['attributes'] = dir(obj)
    dict_info['methods'] = inspect.getmembers(obj, predicate=inspect.ismethod)
    dict_info['module'] = inspect.getmodule(obj)
    dict_info['class'] = inspect.getmembers(obj, predicate=inspect.isclass)
    dict_info['size'] = sys.getsizeof(obj)
    return dict_info

a = 'string'

number_info = introspection_info(a)
for key, value in number_info.items():
    print(f'{key} : {value}')
print()

class_info = introspection_info(Pictures('tree', 'color'))
for key, value in class_info.items():
    print(f'{key} : {value}')
print()

fun_info = introspection_info(introspection_info)
for key, value in fun_info.items():
    print(f'{key} : {value}')
    