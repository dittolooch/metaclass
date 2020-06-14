class User:
    id: int
    name: str
    def __init__(self, id, name):
        id_value_type = self.__annotations__.get('id')
        name_value_type = self.__annotations__.get('name')
        if not isinstance(id, id_value_type):
            raise Exception(f"validation error:{id} is not of type {id_value_type}")
        if not isinstance(name, name_value_type):
            raise Exception(f"validation error:{name} is not of type {name_value_type}")
        self.id= id
        self.name=name

user = User(id="123", name="warren")
# print(user.id)
# # 123
# print(type(user.id))
# # <class 'int'>
# print(user.name)
# try:
#     user.id = "john"
# except Exception as e:
#     print(e)
