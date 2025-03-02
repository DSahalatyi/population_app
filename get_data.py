import asyncio
import os

from dotenv import load_dotenv

from database.models import PopulationWiki, PopulationStatisticsTimes
from database.session import get_db
from scrapers.statisticstimes_scraper import StatisticsTimesScraper
from scrapers.wikipedia_scraper import WikipediaScraper


async def get_data():
    load_dotenv()

    DATA_ORIGIN = os.getenv("DATA_ORIGIN")
    scraper = None
    model = None

    if DATA_ORIGIN == "wikipedia":
        url = os.getenv("WIKI_URL")
        scraper = WikipediaScraper(url)
        model = PopulationWiki
    elif DATA_ORIGIN == "statisticstimes":
        url = os.getenv("STATS_TIMES_URL")
        scraper = StatisticsTimesScraper(url)
        model = PopulationStatisticsTimes

    if scraper is None or model is None:
        raise Exception("A valid data origin has no been specified.")

    response = await scraper.async_send_request()
    parsed_data = scraper.parse(response)
    async for session in get_db():
        for population_schema in parsed_data:
            await scraper.async_save_to_db(session, model, population_schema)


if __name__ == "__main__":
    asyncio.run(get_data())