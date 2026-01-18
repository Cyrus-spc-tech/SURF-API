
from pydantic import BaseModel,Field
from typing import Annotated

class Product(BaseModel):
    id:str 
    sku:Annotated[
        str,
        Field(
            min_length=6,
            max_length=30,
            title="Suk",
            description="Stock keeping Unit",
            examples=["345678-56789-56789", "asdf-asd-sdfg"]
        )
    ]
    name:str