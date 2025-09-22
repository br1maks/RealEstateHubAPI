from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    """Base class for all DB models with dynamic table naming and default PK."""
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
    # @declared_attr
    # def id(cls) -> Mapped[int]:
    #     return mapped_column(primary_key=True)
