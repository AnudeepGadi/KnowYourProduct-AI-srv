from ecommerce_processor.factories.processor_factory import EcommerceProcessorFactory
from typing import Dict

def process_message(payload: Dict):
    builder = EcommerceProcessorFactory.create_processor(payload['source'])
    prompt = (
        builder.parse_html(payload['html_content'])
               .generate_prompt("templates/product_prompt.md")
               .build()
    )
    return prompt