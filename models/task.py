from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Tasks(Base):
    __tablename__ = "Tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    pomodoro_count: Mapped[int] = mapped_column()
    category_id: Mapped[int] = mapped_column()


class Categories(Base):
    __tablename__ = "Categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    type_name: Mapped[Optional[str]] = mapped_column()
    name: Mapped[str] = mapped_column()
