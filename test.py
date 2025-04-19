import asyncio
import json
import httpx
from typing import List, Dict
from parsel import Selector

def parse_product(html_text: str) -> Dict:
    """parse walmart product"""
    sel = Selector(text=html_text)
    data = sel.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
    data = json.loads(data)
    _product_raw = data["props"]["pageProps"]["initialData"]["data"]["product"]
    _idml_raw = data["props"]["pageProps"]["initialData"]["data"]["idml"]
    print(data["props"]["pageProps"]["initialData"]["data"].keys())
    # There's a lot of product data, including private meta keywords, so we need to do some filtering:
    keys = _idml_raw.keys()
    # for key in keys:
    #      print(f"{key}: {_idml_raw[key]}\n")
    wanted_product_keys = [
        "name",
        "shortDescription",
        "brand",
        "model",
        "priceInfo"
    ]

    wanted_idml_keys = [
        "directions",
        "longDescription",
        "specifications"
    ]

    product = {k: v for k, v in _product_raw.items() if k in wanted_product_keys}
    idml = {k: v for k, v in _idml_raw.items() if k in wanted_idml_keys}

    
    product["price"] = product["priceInfo"]["currentPrice"]["priceDisplay"]
    product["currency"] = product["priceInfo"]["currentPrice"]["currencyUnit"]
    del product["priceInfo"]
    product["description"] = product["shortDescription"]
    del product["shortDescription"]
    
    specifications = "\n".join([f"{dic['name']}:{dic['value']}" for dic in idml["specifications"]])
    from bs4 import BeautifulSoup
    description = BeautifulSoup(idml["longDescription"], "html.parser").text
    directions = "\n".join([f"{dic['name']}:{dic['value']}" for dic  in idml["directions"]])
    
    product["specifications"] = specifications + "\n" + description + "\n" + directions

    return product

with open(r"C:\Users\agadi\Downloads\walmart_product.txt", "r", encoding="utf-8") as f:
    html_text = f.read()
    product = parse_product(html_text)
    for key, value in product.items():
        print(f"{key}: {value}")