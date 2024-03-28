from typing import Any, Dict
from json_to_html import convert
from rich import print
from funcs import error
import sys

sys_args = sys.argv[1:]
args: Dict[str, Any] = {
    "path": str,
    "cool_arg": int
}
arg_keys = list(args.keys())

expected_arg_types = [f"<[blue bold]{arg_name}[/blue bold]: [dark_blue bold]{arg_type.__name__}[/dark_blue bold]>" for arg_name, arg_type in args.items()]
expected_args = f"[medium_spring_green]main.py {' '.join(expected_arg_types)}[/medium_spring_green]"
try:
    for arg_index in range(len(args)):
        arg_key = arg_keys[arg_index]
        try:
            args[arg_key] = args[arg_key](sys_args[arg_index])
        except ValueError:
            #* Incorrect data types provided in comman line *#
            error([
                f"Incorrect data type supplied in args",
                f"Expected {expected_args}"
            ])
except IndexError:
    error([
        f"Incorrect argument supplied",
        f"Expected {'//expected args//'} but recieved {'//recieved args//'}"
    ])

convert(args["path"])
