from typing import List
from rich import print

def error(message: str | List[str], error_start: str="Err:"):
    print(f"  [red]{error_start}[/red] ", end="")
    if isinstance(message, str):
        print(f"{message}")
    elif isinstance(message, list):
        for index, line in enumerate(message):
            if index == 0:
                print(f"{line}")
                continue
            print(f"       {line}")
    quit()
