import os
from xml.etree import ElementTree as ET


def generate_html_street_page(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    street_name = root.find("meta").find("nome").text

    street_html = f"""
    <!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"UTF-8\">\n<title>{street_name}</title>\n</head>\n
    <body>
        <h1>{street_name}</h1>
        <h2>Informação da rua</h2>
        """

    for elem in root.findall(".//meta/.*"):
        street_html += f"<p><strong>{elem.tag}:</strong> {elem.text}</p>\n"

    street_html += "<h2>Descrição da Rua</h2>\n"
    for para in root.findall(".//corpo/para"):
        street_html += f"<p>{ET.tostring(para).decode()}</p>\n"

    """<h2>Casas</h2>
    <ul>"""
    for casa in root.findall(".//corpo/lista-casas/casa"):
        house_info = ""
        for child in casa:
            if child.tag == "desc":
                para_element = child.find("para")
                if para_element is not None:
                    house_info += f"<li><strong>Descrição:</strong> {ET.tostring(para_element).decode()}</li>\n"
            elif child.tag == "número":
                house_info += f"<li>nº {child.text}</li>\n"
            elif child.tag == "foro":
                house_info += f"<li><strong>Foro:</strong> {child.text}</li>\n"
            elif child.tag == "enfiteuta":
                house_info += f"<li><strong>Enfiteuta:</strong> {child.text}</li>\n"
            else:
                house_info += f"<li><strong>{child.tag}:</strong> {child.text}</li>\n"
        street_html += house_info

    street_html += "</body>\n</html>"

    with open(f"{street_name}.html", "w") as f:
        f.write(street_html)


def main(argv):
    path = argv[1]
    xml_files = sorted(
        [
            filename
            for filename in os.listdir(path + "/texto")
            if filename.endswith(".xml")
        ]
    )

    for xml_file in xml_files:
        generate_html_street_page(path + "/texto/" + xml_file)


if __name__ == "__main__":
    main(sys.argv)
