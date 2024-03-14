import time
from typing import Any


def sleeper(n: int) -> Any:
    """
    Decorator factory to add a delay before executing the decorated function.

    Args:
        n (int): The number of seconds to sleep before executing the decorated function.

    Returns:
        callable: Decorator function.
    """
    def decor(func: Any) -> Any:
        """
        Decorator function to add a delay before executing the decorated function.

        Args:
            func (callable): The function to be decorated.

        Returns:
            callable: Decorated function.
        """
        time.sleep(n)

        def inner_wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Inner wrapper function to execute before and after calling the decorated function.

            Args:
                *args: Positional arguments passed to the decorated function.
                **kwargs: Keyword arguments passed to the decorated function.

            Returns:
                Any: Result of the decorated function call.
            """
            print("Before function")
            result = func(*args, **kwargs)
            print(f"After function. Result: {result}")

            return result

        return inner_wrapper

    return decor
