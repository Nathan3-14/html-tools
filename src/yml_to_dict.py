import json
import sys
from typing import Any, Dict, List
import yaml
from rich.console import Console


def convert_item(_input: Dict[str, Any]) -> List[dict]:
    to_return = []
    for property, value in _input.items():
        match property:
            case "title":
                to_return.append({"h1": {
                    
                }})


    return to_return


def convert(input_path: str, output_path: str) -> None:
    input_dict = yaml.load(open(input_path, "r").read(), yaml.BaseLoader)
    input_dict_root_key = list(input_dict.keys())[0]
    output_dict = {}

    # console.print_json(json.dumps(input_dict)) #! Debug !#

    output_dict[input_dict_root_key] = []
    input_dict = input_dict[input_dict_root_key]

    for child in input_dict:
        console.print(child)
    
    console.print_json(json.dumps(output_dict)) #! Debug !#


if __name__ == "__main__":
    console = Console()
    sys_args = sys.argv[1:]
    convert(sys_args[0], sys_args[1])
