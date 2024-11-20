from sqlalchemy.orm import Session
from app.models.models import Instituicao
from app.schemas.instituicao_schemas import InstituicaoCreate, InstituicaoUpdate


class InstituicaoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, instituicao_data: InstituicaoCreate) -> Instituicao:
        instituicao = Instituicao(**instituicao_data.dict())
        self.db_session.add(instituicao)
        self.db_session.commit()
        self.db_session.refresh(instituicao)
        return instituicao

    def get_by_id(self, instituicao_id: int) -> Instituicao:
        return self.db_session.query(Instituicao).filter_by(id=instituicao_id).first()

    def update(self, instituicao_id: int, instituicao_data: InstituicaoUpdate) -> Instituicao:
        instituicao = self.get_by_id(instituicao_id)
        if instituicao:
            for key, value in instituicao_data.dict(exclude_unset=True).items():
                setattr(instituicao, key, value)
            self.db_session.commit()
            self.db_session.refresh(instituicao)
        return instituicao

    def delete(self, instituicao_id: int):
        instituicao = self.get_by_id(instituicao_id)
        if instituicao:
            self.db_session.delete(instituicao)
            self.db_session.commit()
        return instituicao

    def list_all(self):
        return self.db_session.query(Instituicao).all()
