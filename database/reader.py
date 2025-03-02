from sqlalchemy.ext.asyncio import AsyncSession


class DBReader:
    def __init__(self, query):
        self.query = query

    async def get_population_data(self, session: AsyncSession) -> list:
        result = await session.execute(self.query)
        data = result.fetchall()
        if len(data) > 0:
            return list(data)
        raise Exception("There was an error fetching data from database")

    @staticmethod
    def format_population_data(data: list) -> list:
        formatted_data = []

        for row in data:
            formatted_row = (
                row[0],
                int(row[1]),
                row[2],
                row[3],
                row[4],
                row[5]
            )
            formatted_data.append(formatted_row)

        return formatted_data

