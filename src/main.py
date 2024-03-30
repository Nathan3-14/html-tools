import os
from typing import Any, Dict
from .dict_to_html import convert
from .funcs import error
import sys
import yaml
from rich.console import Console
from xml.etree import ElementTree as ET

console = Console()

def main():
    sys_args = sys.argv[1:]
    args: Dict[str, Any] = { #? (optional, data type)
        "input_path": str,
        "output_path": str
    }
    arg_keys = list(args.keys())


    expected_arg_types = [f"<[blue bold]{arg_name}[/blue bold]: [dark_blue bold]{arg_type.__name__}[/dark_blue bold]>" for arg_name, arg_type in args.items()]
    expected_args = f"[medium_spring_green]main.py {' '.join(expected_arg_types)}[/medium_spring_green]"
    recieved_args_in = [f"{arg}" for arg in sys_args]
    recieved_args = f"[medium_spring_green]main.py {' '.join(recieved_args_in)}[/medium_spring_green]"


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
            f"Expected {expected_args} but recieved {recieved_args}"
        ])
    
    open(args["output_path"], "wb").write(
        ET.tostring(convert(yaml.load(
            open(args["input_path"]).read(),
            yaml.BaseLoader)
        ))
    )
