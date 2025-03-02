import asyncio
import os

from dotenv import load_dotenv
from tabulate import tabulate

from database.queries import WIKIPEDIA_DATA_QUERY, STATISTICS_TIMES_DATA_QUERY
from database.reader import DBReader
from database.session import get_db

HEADERS = [
    "Region",
    "Total Population",
    "Biggest Country",
    "Largest Population",
    "Smallest Country",
    "Smallest Population",
]


async def print_data():
    load_dotenv()

    DATA_ORIGIN = os.getenv("DATA_ORIGIN")
    OUTPUT_FORMAT = os.getenv("OUTPUT_FORMAT")
    query = None

    if DATA_ORIGIN == "wikipedia":
        query = WIKIPEDIA_DATA_QUERY
    elif DATA_ORIGIN == "statisticstimes":
        query = STATISTICS_TIMES_DATA_QUERY

    if query is None:
        raise Exception("A valid data origin has no been specified.")

    reader = DBReader(query)
    data = None
    async for session in get_db():
        data = await reader.get_population_data(session)
    formatted_data = reader.format_population_data(data)

    if OUTPUT_FORMAT == "line-by-line":
        [print(line) for row in formatted_data for line in row]
    elif OUTPUT_FORMAT == "table":
        print(tabulate(formatted_data, headers=HEADERS, tablefmt="grid"))


if __name__ == "__main__":
    asyncio.run(print_data())
