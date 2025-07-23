from typing import Annotated

from pydantic import Field

from workout_api.contrib.schemas import BaseModel


class Categoria(BaseModel):
    nome: Annotated[str, Field(description='Nome da Categoria', example='Scale', max_length=10)]
    