import datetime

from sqlalchemy import Integer, UUID, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4
from app.database import db

class Paciente(db.Model):
    id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), unique=True, nullable=False)
    data_nascimento: Mapped[datetime.datetime] = mapped_column(Date, nullable=False)
    telefone: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f'<Paciente {self.nome}>'
