import datetime
import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Date
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import REAL

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
Base = declarative_base()

AsyncSessionFactory = async_sessionmaker(engine, expire_on_commit=False)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    created: Mapped[datetime.date] = mapped_column(Date, server_default=func.now())


class Mkd(Base):
    __tablename__ = "mkd"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer)
    login = Column(String)
    form_of_ownership = Column(String)  # 755 форма собственности
    year_built = Column(Integer)  # 756 постройки
    year_reconstructed = Column(Integer)  # 757 год реконструкции
    series_of_project_id = Column(
        Integer, ForeignKey("series_of_projects.id")
    )  # 758 серия проекта
    series_of_project = relationship(
        "SeriesOfProjects", back_populates="mkds", lazy="selectin"
    )
    num_floors = Column(Integer)  # 759 кол-во этажей
    num_entrances = Column(Integer)  # 760 кол-во подъездов
    num_apartments = Column(Integer)  # 761 кол-во квартир
    total_area = Column(REAL)  # 762 общая площадь
    living_area = Column(REAL)  # 763 общая площадь жилая
    non_living_area = Column(REAL)  # 764 общая площадь нежилая
    building_volume = Column(Integer)  # 765 строительный объем
    wear_and_tear = Column(Integer)  # 766 износ объекта
    energy_efficiency = Column(String)  # 767 класс энергоэффективности
    wall_material_id = Column(
        Integer, ForeignKey("wall_material.id")
    )  # 769 материал стен
    wall_material = relationship("WallMaterial", back_populates="mkds", lazy="selectin")
    accident_rate_id = Column(
        Integer, ForeignKey("accident_rate.id")
    )  # 770 признак аварийности
    accident_rate = relationship("AccidentRate", back_populates="mkds", lazy="selectin")
    num_passenger_elevators = Column(Integer)  # 771 кол-во пассажирских лифтов
    num_freight_passenger_elevators = Column(Integer)  # 772 кол-во грузо-пассажирских
    roof_cleaning_id = Column(
        Integer, ForeignKey("roof_cleaning.id")
    )  # 775 очередь уборки кровли
    roof_cleaning = relationship("RoofCleaning", back_populates="mkds", lazy="selectin")
    roofing_material_id = Column(
        Integer, ForeignKey("roofing_material.id")
    )  # 781 материалы кровли
    roofing_material = relationship(
        "RoofingMaterial", back_populates="mkds", lazy="selectin"
    )
    unom = Column(Integer, unique=True)  # 782 UNOM

    housing_stock_id = Column(
        Integer, ForeignKey("housing_stock.id")
    )  # 2463 тип жилого фонда
    housing_stock = relationship("HousingStock", back_populates="mkds", lazy="selectin")
    mkd_status_id = Column(Integer, ForeignKey("mkd_status.id"))  # 3163 статус МКД
    mkd_status = relationship("MkdStatus", back_populates="mkds", lazy="selectin")
    mkd_management_status_id = Column(
        Integer, ForeignKey("mkd_management_status.id")
    )  # 3243 статус управдения МКД
    mkd_management_status = relationship(
        "MkdManagementStatus", back_populates="mkds", lazy="selectin"
    )
    num_freight_elevators = Column(Integer)  # 3363 кол-во грузовых лифтов
    reason_for_status_change = Column(String)  # 3468 причины изменения статуса
    mkd_category_id = Column(
        Integer, ForeignKey("mkd_category.id")
    )  # 103506 категория МКД
    mkd_category = relationship("MkdCategory", back_populates="mkds", lazy="selectin")
    overhauls = relationship("Overhaul", back_populates="mkds")
    incidents = relationship("Incident", back_populates="mkds")


class SeriesOfProjects(Base):
    __tablename__ = "series_of_projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mkds = relationship("Mkd", back_populates="series_of_project")


class WallMaterial(Base):
    __tablename__ = "wall_material"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mkds = relationship("Mkd", back_populates="wall_material")


class AccidentRate(Base):
    __tablename__ = "accident_rate"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mkds = relationship("Mkd", back_populates="accident_rate")


class RoofCleaning(Base):
    __tablename__ = "roof_cleaning"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mkds = relationship("Mkd", back_populates="roof_cleaning")


class RoofingMaterial(Base):
    __tablename__ = "roofing_material"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mkds = relationship("Mkd", back_populates="roofing_material")


class HousingStock(Base):
    __tablename__ = "housing_stock"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mkds = relationship("Mkd", back_populates="housing_stock")


class MkdStatus(Base):
    __tablename__ = "mkd_status"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mkds = relationship("Mkd", back_populates="mkd_status")


class MkdManagementStatus(Base):
    __tablename__ = "mkd_management_status"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mkds = relationship("Mkd", back_populates="mkd_management_status")


class MkdCategory(Base):
    __tablename__ = "mkd_category"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mkds = relationship("Mkd", back_populates="mkd_category")


class Overhaul(Base):
    __tablename__ = "overhaul"

    id = Column(Integer, primary_key=True)
    period = Column(Integer)
    name = Column(String, nullable=False)
    num_entrance = Column(Integer)
    elev_num = Column(String)
    plan_start = Column(Date)
    plan_end = Column(Date)
    fact_start = Column(Date)
    fact_end = Column(Date)
    unom = Column(Integer, ForeignKey("mkd.unom"))
    mkds = relationship("Mkd", back_populates="overhauls", lazy="selectin")


class Incident(Base):
    __tablename__ = "incident"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    source = Column(String)
    opened = Column(Date)
    closed = Column(Date)
    unom = Column(Integer, ForeignKey("mkd.unom"))
    mkds = relationship("Mkd", back_populates="incidents", lazy="selectin")


class Coordinate(Base):
    __tablename__ = "coordinate"
    unom = Column(Integer, primary_key=True)
    latitude = Column(REAL)
    longitude = Column(REAL)


class IncidentPredict(Base):
    __tablename__ = "incident_predict"
    unom = Column(Integer, primary_key=True)
    works_list = Column(String)
    num_works = Column(Integer)


class FeaturePredict(Base):
    __tablename__ = "feature_predict"
    unom = Column(Integer, primary_key=True)
    works_list = Column(String)
    num_works = Column(Integer)

class UnionPredict(Base):
    __tablename__ = "union_predict"
    unom = Column(Integer, primary_key=True)
    works_list = Column(String)
    num_works = Column(Integer)
