from pydantic import BaseModel


class WikiPopulationSchema(BaseModel):
    country: str
    population_2022: int
    population_2023: int
    change: float
    continental_region: str | None
    statistical_region: str | None


class StatisticsTimesSchema(BaseModel):
    country: str
    population_2023: int
    population_2024: int
    change: int
    region: str
