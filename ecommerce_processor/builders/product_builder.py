from typing import Dict, Any
from ecommerce_processor.models.product import Product
from ecommerce_processor.strategies.base_parser import ProductParser

class ProductDataBuilder:
    def __init__(self, parser: ProductParser):
        self.parser:ProductParser = parser
        self.prompt:str = None
        self.data:Product = None
        self.prompt_template:str = None

    def parse_html(self, html_content: str) -> 'ProductDataBuilder':
        self.data = self.parser.parse(html_content)
        return self

    def generate_prompt(self, template_path: str) -> 'ProductDataBuilder':
        if template_path:
            with open(template_path, 'r', encoding="utf-8") as file:
                self.prompt_template = file.read()
        return self

    def build(self) -> str:
        self.prompt = self.prompt_template.format(**{k: (v if v is not None else "Not specified") for k, v in Product.to_dict(self.data).items()})
        return self.prompt