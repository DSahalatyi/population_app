from httpx import AsyncClient
from pydantic import BaseModel
from sqlalchemy import insert, text
from sqlalchemy.ext.asyncio import AsyncSession

from database.base import Base


class BaseScraper:

    def __init__(self, url):
        self.url = url

    def parse(self):
        pass

    async def async_send_request(self):
        async with AsyncClient() as client:
            response = await client.get(self.url)
            if response.status_code == 200:
                return response.text

    async def async_save_to_db(
        self, db: AsyncSession, model: Base, schema: BaseModel
    ) -> None:
        query = insert(model).values(schema.model_dump())
        try:
            await db.execute(query)
        except Exception as e:
            print(f"Error occurred while saving to DB: {e}")
        await db.commit()

    @staticmethod
    def parse_int(value: str) -> int | None:
        try:
            return int(value.replace(",", ""))
        except ValueError:
            return None

    @staticmethod
    def parse_float(value: str) -> float | None:
        try:
            return float(value.replace("−", "-").replace("%", "").strip())
        except ValueError as e:
            print(e)
            return None
