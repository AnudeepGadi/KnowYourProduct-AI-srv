from bs4 import BeautifulSoup
import json
from ecommerce_processor.strategies.base_parser import ProductParser
from typing import Dict, Any
from ecommerce_processor.models.product import Product
from parsel import Selector


class WalmartProductParser(ProductParser):
    def parse(self, html_content: str) -> Product:
        sel = Selector(text=html_content)
        data = sel.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        data = json.loads(data)
        _product_raw = data["props"]["pageProps"]["initialData"]["data"]["product"]
        _idml_raw = data["props"]["pageProps"]["initialData"]["data"]["idml"]

        wanted_product_keys = [
            "name",
            "shortDescription",
            "brand",
            "model",
            "priceInfo",
        ]

        wanted_idml_keys = ["directions", "longDescription", "specifications"]

        product = {k: v for k, v in _product_raw.items() if k in wanted_product_keys}
        idml = {k: v for k, v in _idml_raw.items() if k in wanted_idml_keys}

        product["price"] = product["priceInfo"]["currentPrice"]["priceDisplay"]
        product["currency"] = product["priceInfo"]["currentPrice"]["currencyUnit"]
        del product["priceInfo"]
        product["description"] = product["shortDescription"]
        del product["shortDescription"]

        specifications = "\n".join(
            [f"{dic['name']}:{dic['value']}" for dic in idml["specifications"]]
        )
        description = BeautifulSoup(idml["longDescription"], "html.parser").text
        directions = "\n".join(
            [f"{dic['name']}:{dic['value']}" for dic in idml["directions"]]
        )

        product["specifications"] = (
            specifications + "\n" + description + "\n" + directions
        )

        # Create and return the Product object
        return Product.from_dict(product)
