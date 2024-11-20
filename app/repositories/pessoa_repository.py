from sqlalchemy.orm import Session
from app.models.models import Pessoa
from app.schemas.pessoa_schemas import PessoaCreate, PessoaUpdate


class PessoaRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, pessoa_data: PessoaCreate) -> Pessoa:
        pessoa = Pessoa(**pessoa_data.dict())
        self.db_session.add(pessoa)
        self.db_session.commit()
        self.db_session.refresh(pessoa)
        return pessoa

    def get_by_id(self, pessoa_id: int) -> Pessoa:
        return self.db_session.query(Pessoa).filter_by(id=pessoa_id).first()

    def update(self, pessoa_id: int, pessoa_data: PessoaUpdate) -> Pessoa:
        pessoa = self.get_by_id(pessoa_id)
        if pessoa:
            for key, value in pessoa_data.dict(exclude_unset=True).items():
                setattr(pessoa, key, value)
            self.db_session.commit()
            self.db_session.refresh(pessoa)
        return pessoa

    def delete(self, pessoa_id: int):
        pessoa = self.get_by_id(pessoa_id)
        if pessoa:
            self.db_session.delete(pessoa)
            self.db_session.commit()
        return pessoa

    def list_all(self):
        return self.db_session.query(Pessoa).all()
