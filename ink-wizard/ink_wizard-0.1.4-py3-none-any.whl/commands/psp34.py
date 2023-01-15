from ..template_generators.psp34 import PSP34
from .base import Base

class PSP34Command(Base):
    
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def run_command(cls, **kwargs) -> None:
        cls = cls()
        contract_name = cls.typer.prompt("Please enter name of contract")
        metadata = cls.typer.confirm("Do you want to store Metadata?")
        mintable = cls.typer.confirm("Do you want it to be mintable?")
        burnable = cls.typer.confirm("Do you want it to be burnable?")
        enumrable = cls.typer.confirm("Do you want it to be enumrable?")
        if metadata == False and mintable == False and burnable == False and enumrable == False:
            PSP34.generate_code(contract_name=contract_name, basic=True)
        else:
            PSP34.generate_code(contract_name=contract_name, mintable=mintable, metadata=metadata, burnable=burnable, enumrable=enumrable)
        print("psp34 contract scaffolded")
