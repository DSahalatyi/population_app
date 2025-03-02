from sqlalchemy import Integer, Column, BigInteger, Float, String

from database.base import Base


class PopulationWiki(Base):
    __tablename__ = "population_wiki"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String)
    population_2022 = Column(BigInteger)
    population_2023 = Column(BigInteger)
    change = Column(Float)
    continental_region = Column(String)
    statistical_region = Column(String)

class PopulationStatisticsTimes(Base):
    __tablename__ = "population_stats_times"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String)
    population_2023 = Column(BigInteger)
    population_2024 = Column(BigInteger)
    change = Column(BigInteger)
    region = Column(String)
