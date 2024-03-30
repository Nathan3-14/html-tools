import json
import sys
from typing import Any, Dict, List
import yaml
from rich.console import Console


def convert_item(_input: Dict[str, Any]) -> Dict[str, Any]:
    to_return = {}
    for property, value in _input.items():
        try:
            latest_key = list(to_return.keys())[0]
        except IndexError:
            latest_key = None

        console.print(f"{property} = {value}")

        match property:
            case "title":
                to_return["h1"] = {
                    "__text": value
                }
            case "subtitle":
                to_return["h2"] = {
                    "__text": value
                }
            case "image":
                to_return["img"] = {
                    "_src": value
                }
            case "text":
                to_return["p"] = {
                    "__text": value
                }
            case "section":
                to_return["div"] = {
                    "children": [convert_item(element) for element in value if isinstance(element, dict)]
                }
            case "id":
                to_return[latest_key]["_id"] = value


    return to_return


def convert(input_path: str, output_path: str) -> None:
    input_dict = yaml.load(open(input_path, "r").read(), yaml.BaseLoader)
    input_dict_root_key = list(input_dict.keys())[0]
    output_dict = {}

    output_dict[input_dict_root_key] = []
    input_dict = input_dict[input_dict_root_key]


    for child in input_dict:
        output_dict[input_dict_root_key].append(convert_item(child))
    
    open(output_path, "w").write(yaml.dump(output_dict))

    


if __name__ == "__main__":
    console = Console()
    sys_args = sys.argv[1:]
    convert(sys_args[0], sys_args[1])
