import functools
from typing import Any, Callable, Dict, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызова функции и ее результата.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Dict[str, Any]) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                raise

            if filename:
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)

            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> float:
    """
    Выполняет деление двух чисел.
    """
    return x / y


@log()
def another_function(a: int, b: int) -> int:
    """
    Складывает два числа.
    """
    return a + b


my_function(1, 2)
another_function(3, 4)

try:
    my_function(1, 0)
except ZeroDivisionError:
    pass
