from typing import Dict
import xml.etree.ElementTree as ET
import sys
import os
import json


def parse_file(xml_file,folder):
    parsed_data = dict()
    tree = ET.parse(xml_file)
    root = tree.getroot()
    parsed_data["nome"] = root.find("meta").find("nome").text
    parsed_data["num"] = root.find("meta").find("número").text
    corpo = root.find("corpo")
    parsed_data["descricao"] = [
        ET.tostring(para).decode() for para in corpo if para.tag == "para"
    ]
    parsed_data["figuras"] = {
        fig.attrib["id"]: {
            "img":  os.path.abspath( os.path.join( folder,fig.find("imagem").attrib["path"])),
            "desc": fig.find("legenda").text,
        }
        for fig in corpo.findall("figura")
    }

    def parse_casa(casa):
        try:
            return {
                "num": casa.find("número").text,
                "foro": casa.find("foro").text,
                "desc": ET.tostring(casa.find("desc")),
            }
        except:
            return None

    parsed_data["casas"] = [parse_casa(casa) for casa in root.findall(".//casa") if parse_casa(casa)]
    return parsed_data


def parse_folder(folder):
    links = dict()
    material_base: str = folder
    folder = material_base + "/texto"
    return {file.split('.')[0]: parse_file(folder + "/" + file,folder) for file in os.listdir(folder)}


if __name__ == "__main__":
    parse_folder(sys.argv[1])
