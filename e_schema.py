# c_pydantic.py

class Descriptor:
    def __get__(self, instance, owner):
        return getattr(self, self.name)
    def __set__(self, obj, val):
        try:
            casted_value = self.type(val)
        except:
            raise Exception(f"{obj}.{self.name} = '{val}' of type {type(val)} cannot be casted to {self.type}")
        else:
            setattr(self, self.name, casted_value)
    def __init__(self, name, type):
        self.type = type
        self.name = name
        setattr(self, name, self.type())

class BaseMeta(type):
    def __new__(meta_class, class_name, base_classes, attributes):
        cls = super().__new__(meta_class, class_name, base_classes, attributes)
        cls.attribute_types = {}
        annotations = attributes.get('__annotations__',{})
        for attribute_name, value_type in annotations.items():
            descriptor = Descriptor(name=attribute_name, type=value_type)
            setattr(cls, attribute_name, descriptor)
        return cls

class BaseModel(metaclass=BaseMeta):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class User(BaseModel):
    id: int
    name: str

user = User(id="123", name="warren")
print(user.id)
# 123
print(type(user.id))
# <class 'int'>
print(user.name)
try:
    user.id = "john"
except Exception as e:
    print(e)


    
    