from abc import ABC, abstractmethod
from typing import Dict, Any

class ProductParser(ABC):
    @abstractmethod
    def parse(self, html_content: str) -> Dict[str, Any]:
        pass