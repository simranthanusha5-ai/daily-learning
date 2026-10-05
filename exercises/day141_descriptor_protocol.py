"""Day 141: Typed Field Descriptors."""

class TypedField:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type.__name__}, got {type(value).__name__}")
        instance.__dict__[self.name] = value

class UserProfile:
    age = TypedField(int)
    username = TypedField(str)

if __name__ == "__main__":
    user = UserProfile()
    user.age = 25
    user.username = "alice"
    assert user.age == 25
    try:
        user.age = "twenty-five"
        assert False
    except TypeError:
        pass
    print("Day 141 Descriptors tests passed!")
