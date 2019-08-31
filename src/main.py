class MyClass:

    _value: str = "a"

    def sample_method(self) -> str:
        print("sample_method\n")
        return self._value

    @staticmethod
    def sample_static_method() -> str:
        print("sample_static_method\n")
        return "original"

    @classmethod
    def sample_class_method(cls) -> str:
        print("sample_class_method\n")
        return "original"
