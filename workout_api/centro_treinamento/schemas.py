from typing import Annotated

from pydantic import Field

from workout_api.contrib.schemas import BaseModel


class CentroTreinamento(BaseModel):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT King', max_length=50)]
    endereço: Annotated[str, Field(description='Endereço', example='Rua teste, 6', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietário', example='João', max_length=30)]
    