from dataclasses import dataclass
from typing import List, Dict

"""
This module defines the Product class, which represents a product with various attributes.
"""
@dataclass
class Product:
    name: str = 'unknown'
    brand: str = 'unknown'
    model: str = 'unknown'
    description: str = 'unknown'
    price: str = 'unknown' 
    currency: str = 'unknown'
    specifications: str = 'unknown'

    @staticmethod
    def from_dict(data: Dict) -> 'Product':
        """
        Creates a Product instance from a dictionary.
        """
        return Product(
            name=data.get('name', ''),
            brand=data.get('brand', ''),
            model=data.get('model', ''),
            description=data.get('description', ''),
            price=data.get('price', ''),
            currency=data.get('currency', ''),
            specifications=data.get('specifications', '')
        )
    
    @staticmethod
    def to_dict(product: 'Product') -> Dict:
        """
        Converts a Product instance to a dictionary.
        """
        return {
            'name': product.name,
            'brand': product.brand,
            'model': product.model,
            'description': product.description,
            'price': product.price,
            'currency': product.currency,
            'specifications': product.specifications
        }
        