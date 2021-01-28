import functools
from typing import Callable

NONE = "None"


def type_check(*args1: type, is_class_method: bool = False) -> Callable:
    """
    Used for runtime type checking
    """

    def decorator(func: Callable) -> Callable:
        """
        functools.wraps maintains the integrity of the og func name
        """

        @functools.wraps(func)
        def wrapper(*args2: tuple, **keywords: dict) -> Callable:
            args = args2[1:] if is_class_method else args2
            for (arg2, arg1) in zip(args, args1):
                if not isinstance(arg2, arg1):
                    raise TypeError(f"expected type: {arg1}, actual type: {type(arg2)}")
            return func(*args2, **keywords)

        return wrapper

    return decorator
