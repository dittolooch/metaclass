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