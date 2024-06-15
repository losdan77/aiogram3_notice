from sqlalchemy import ForeignKey, Date
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

class Type_notice(Base):
    __tablename__ = 'type_notice'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class Accouting_notice(Base):
    __tablename__ = 'accouting_notice'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_type: Mapped[int] = mapped_column(ForeignKey('type_notice.id'),
                                          nullable=False)
    id_user: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=True)
    date_birthday: Mapped[datetime] = mapped_column(Date, nullable=True)
    date_notice: Mapped[datetime] = mapped_column(Date, nullable=True)
     