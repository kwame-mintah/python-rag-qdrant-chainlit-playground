import requests
from bs4 import BeautifulSoup
from html2text import html2text
from pydantic_core import Url
from requests import HTTPError

from config import EnvironmentVariables


def parse_wikimedia_page_and_output_as_markdown(
    url: Url,
    page: str,
    output: str = "data",
) -> None:
    try:
        response = requests.get(
            url=str(url),
            params={
                "action": "parse",
                "page": page,
                "format": "json",
                "prop": "text",
            },
        )

        response.raise_for_status()
        html = response.json()["parse"]["text"]["*"]

        soup = BeautifulSoup(html, features="html.parser")

        # Remove 'highlights' mini view of information.
        for span in soup.find_all(name="span", class_="noexcerpt"):
            span.decompose()
        markdown_text = html2text(str(soup))

        with open(f"{output}/{page}.md", mode="w+", encoding="utf-8") as f:
            f.write(markdown_text)

    except HTTPError as exception:
        print(f"An error occurred when attempting to fetch Wiki {exception}")


if __name__ == "__main__":
    parse_wikimedia_page_and_output_as_markdown(
        url=EnvironmentVariables().WIKIPEDIA_PAGE_API_URL, page="Story_and_History"
    )
