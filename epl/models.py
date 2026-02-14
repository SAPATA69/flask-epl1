from epl.extensions import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional  # ← เพิ่ม Optional

class Club(db.Model):
    __tablename__ = 'club'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    stadium: Mapped[str] = mapped_column(String(50), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    logo: Mapped[str] = mapped_column(String(255), nullable=False)

    players: Mapped[List['Player']] = relationship(back_populates='club')

    def __repr__(self):
        return f'<Club: {self.name}>'

class Player(db.Model):
    __tablename__ = 'player'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    position: Mapped[str] = mapped_column(String(20), nullable=False)
    nationality: Mapped[str] = mapped_column(String(50), nullable=False)
    goals: Mapped[int] = mapped_column(Integer, default=0, nullable=True)
    squad_no: Mapped[int] = mapped_column(Integer, nullable=True)
    img: Mapped[str] = mapped_column(String(255), nullable=False)

    # ✅ เพิ่ม clean_sheets — nullable เพราะใช้แค่ Goalkeeper
    clean_sheets: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, default=None)

    club_id: Mapped[int] = mapped_column(Integer, ForeignKey(Club.id))
    club: Mapped[Club] = relationship(back_populates='players')

    def __repr__(self):
        return f'<Player: {self.name}>'