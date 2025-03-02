from bs4 import BeautifulSoup

from schemas import StatisticsTimesSchema
from scrapers.base_scraper import BaseScraper


class StatisticsTimesScraper(BaseScraper):

    def parse(self, html: str) -> list:
        soup = BeautifulSoup(html, "lxml")
        rows = soup.select("table#table_id tbody tr")

        parsed_data = []

        for row in rows:
            cols = []
            for cell in row.find_all(["td", "th"]):
                link = cell.find("a")
                text = link.get_text() if link else cell.get_text()
                cols.append(text)

            serialized_data = StatisticsTimesSchema(
                country=cols[0],
                population_2023=self.parse_int(cols[1]),
                population_2024=self.parse_int(cols[3]),
                change=self.parse_int(cols[6]),
                region=cols[8],
            )

            parsed_data.append(serialized_data)

        return parsed_data
