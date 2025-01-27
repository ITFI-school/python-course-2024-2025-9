def class_tree(cls, indent=0):
    print('.' * indent, cls.__name__)
    for sub_cls in cls.__subclasses__():
        class_tree(sub_cls, indent + 3)

class_tree(BaseException)
