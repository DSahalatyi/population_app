from schemas import WikiPopulationSchema
from scrapers.base_scraper import BaseScraper
from bs4 import BeautifulSoup


class WikipediaScraper(BaseScraper):

    def parse(self, html: str) -> list:
        soup = BeautifulSoup(html, "lxml")
        rows = soup.select("table.wikitable tbody tr")

        for br in soup.find_all("br"):
            br.replace_with(" ")

        parsed_data = []

        # Skipping the table headings row
        for row in rows[1:]:
            cols = []
            for cell in row.find_all(["td", "th"]):
                link = cell.find("a")
                text = link.get_text() if link else cell.get_text()
                cleaned_text = self.clean_text(text)
                cols.append(cleaned_text if cleaned_text else "")

            serialized_data = WikiPopulationSchema(
                country=cols[0],
                population_2022=self.parse_int(cols[1]),
                population_2023=self.parse_int(cols[2]),
                change=self.parse_float(cols[3]),
                continental_region=cols[4],
                statistical_region=cols[5],
            )

            parsed_data.append(serialized_data)

        return parsed_data

    @staticmethod
    def clean_text(text: str) -> str | None:
        text = text.replace("\n", "")
        text = None if text == "–" else text
        return text
