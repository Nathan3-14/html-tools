import re
from typing import Any, Dict
import xml.etree.ElementTree as ET
from .funcs import error
import yaml
import json

def convert_dict(html_dict: Dict[str, Any], parent: ET.Element) -> ET.Element:
    single_underscore_regex = r"(?<!_)_(?=[a-zA-Z]).+"

    html_dict_key = list(html_dict.keys())[0]
    html_dict = html_dict.copy()[html_dict_key]

    sub = ET.SubElement(parent, html_dict_key)

    for attrib_name, attrib_data in html_dict.items():
        if attrib_name == "__text":
            sub.text = html_dict["__text"]
        elif attrib_name == "children":
            pass
        elif re.match(single_underscore_regex, attrib_name):
            sub.set(attrib_name[1:], attrib_data)
            print(f"_: {attrib_name}")
    return sub

def convert(html_yml: Dict[str, Any]) -> ET.Element:
    from .main import console


    data = html_yml
    console.print_json(json.dumps(data)) #! DEBUG !#

    main_id = list(data.keys())[0]

    main = ET.Element("div")
    main.set("id", main_id)
    
    data = data[main_id]

    for item in data:
        item_name = list(item.keys())[0]
        item_data = item[item_name]
        item_data_keys = list(item_data.keys())

        sub = convert_dict(item_data, main)



    open("test.html", "wb").write(ET.tostring(main))

    return main

