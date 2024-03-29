from typing import Any, Dict
import xml.etree.ElementTree as ET
from funcs import error

def convert(hmtl_json: Dict[str, Any]):
    main = ET.Element("div")

