from ecommerce_processor.strategies.walmart_parser import WalmartProductParser
from ecommerce_processor.builders.product_builder import ProductDataBuilder

class EcommerceProcessorFactory:
    @staticmethod
    def create_processor(source: str) -> ProductDataBuilder:
        if source == "walmart":
            return ProductDataBuilder(WalmartProductParser())
        raise ValueError(f"Unsupported source: {source}")