from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования начала и конца функции, а также результатов и ошибок.
    Если filename задан, то логи записываются в указанный файл, иначе выводится в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            if filename:
                with open(filename, "a") as file:
                    try:
                        result = func(*args, **kwargs)
                        file.write(f"{func_name} ok\n")
                        return result
                    except Exception as e:
                        file.write(f"{func_name} error: {e}. Inputs: {args}, {kwargs}\n")
            else:
                try:
                    result = func(*args, **kwargs)
                    print(f"{func_name} ok")
                    return result
                except Exception as e:
                    print(f"{func_name} error: {e}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator
