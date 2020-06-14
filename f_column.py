from typing import List, Optional
def validate(data, cls):
    annotations = cls.__annotations__
    for key, val in data.items():
        val_type = annotations.get(key)
        if not val_type:
            raise Exception(f"{key} is not an attribute of {cls}")
        try:
            data[key] = val_type(val)
        except:    
            raise Exception(f"{cls}.{key}: '{val}' is not of type {val_type}")

class ODMeta(type):
    def __new__(cls, class_name, base_classes, attributes):
        if class_name != "ODBase":
            for attr_name, attr in attributes.items():
                if isinstance(attr, Column):
                    attr.set_name(attr_name)
        return super().__new__(cls, class_name, base_classes, attributes)

class Column:
    def __get__(self, obj, type):
        # obj = owner, owner class
        return getattr(self, self.attr_name) 
    def __set__(self, obj, val):
        if not isinstance(val, self.type):
            raise Exception(f"The value of attribute '{self.attr_name}' in {obj} :'{val}' is not of type {self.type}")
        setattr(self, self.attr_name, val)
    def __init__(self, type):
        self.type = type
    def set_name(self, attr_name):
        self.attr_name = attr_name
        setattr(self, attr_name, self.type())

class ODBase(metaclass=ODMeta):
    _registry = {}
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


class Policy(ODBase):
    name = Column(type=str)
    age = Column(type=int)
    is_active = Column(type=bool)

policy = Policy(name="medical", age=123, is_active=False)
print(policy.__dict__)
print(policy.name)
print(policy.age)
print(policy.is_active)
policy.name = "john"
policy.age=1
print(policy.name)
print(policy.age)
policy.is_active =123
# import sys
# sys.path.append("pydantic/")
# from datetime import datetime
# from typing import List, Optional
# from pydantic import BaseModel

# class User(BaseModel):
#     id: int
#     name = 'John Doe'
#     signup_ts: Optional[datetime] = None
#     friends: List[int] = []

# external_data = {
#     'id': '123',
#     'signup_ts': '2019-06-01 12:22',
#     'friends': [1, 2, '3']
# }
# user = User(**external_data)