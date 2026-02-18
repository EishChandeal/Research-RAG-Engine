import requests
from lxml import etree #type: ignore

def get_grobid_tree(pdf_path, service = "processFulltextDocument"):
    url = f"http://localhost:8070/api/{service}"
    with open(pdf_path,'rb') as f:
        files = {'input':f}
        params = {"teiCoordinates":1, "consolidateHeader": 1} # for specific location and verified header values
        response = requests.post(url , files= files, data=params) # Professional Tip: Use 'data' for multi-part form parameters in GROBID

        if response.status_code == 200: 
            return etree.fromstring(response.content)  # to convert tree structure which is traversable out of bytes wtihin
        else: 
            raise Exception(f"Grobid Erro {response.status_code} : {response.text}")
        
ns = {"tei" : "http://www.tei-c.org/ns/1.0"}
tree = get_grobid_tree(".\\samples\\Understanding_param_sharing.pdf")
abstract_nodes = tree.xpath("//tei:abstract//tei:p/text()", namespaces = ns) # // > to select all , tei:abstract > the particular section, text() to get that as text
abs_text = " ".join(abstract_nodes) # remove the "text()" specifier in the end to receive it in raw XML form , from where we can select "attributes" if required. Attributes give away specific co-ordinates
print(f" Abstract Text: {abs_text}")

attribute_specifier_verifier_thing = "{http://www.w3.org/XML/1998/namespace}"
figures = tree.xpath("//tei:figure", namespaces = ns)  # namespace to mention the convention being used, to point to the id in expanded form basically 
# for fig in figures: 
#     fig_id = fig.get(f"{attribute_specifier_verifier_thing}id")
#     lable = fig.xpath(".//tei:label/text()")