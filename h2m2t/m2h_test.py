from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter

from h2m2t.m2h import markdown_to_html


def _prettify_html(html: str, root: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    html = soup.find(root).prettify(formatter=HTMLFormatter(indent=4))
    return html.strip().splitlines()


@pytest.mark.parametrize(
    "case",
    [
        "citilink",
        "dns",
        "drive2",
        "gazeta",
        # "habr",
        "iv1",
        "iv2",
        "iv3",
        # "iv4",
        # "iv5",
        "kinopoisk",
        "kommersant",
        "kp",
        "lenta",
        "livejournal1",
        "livejournal2",
        "livejournal3",
        "mk",
        "ozon",
        "rbc",
        "ria",
        "sport",
        "vc",
        "wb",
        "woman",
        "zen",
    ],
)
def test_html(case: str) -> None:
    test_path = Path(__file__).resolve().parent.parent / "tests"

    src_path = test_path / "html_to_markdown" / f"{case}.md"
    src_html = src_path.read_text()

    gt_path = test_path / "markdown_to_html" / f"{case}.html"
    expected = gt_path.read_text()
    expected = _prettify_html(expected, "body")

    result = markdown_to_html(src_html)
    result = _prettify_html(result, "body")

    dbg_path = test_path / "markdown_to_html" / f"{case}_.html"
    if result != expected:
        dbg_path.write_text("\n".join(result))
    elif dbg_path.exists():
        dbg_path.unlink()

    assert expected == result


def test_setex() -> None:
    test_path = Path(__file__).resolve().parent.parent / "tests"

    src_html = "Код доступа: 053174  \n\n--  \n======================  \nС уважением, аналитик службы продаж"

    gt_path = test_path / "markdown_to_html" / "setex.html"
    expected = gt_path.read_text()
    expected = _prettify_html(expected, "body")

    result = markdown_to_html(src_html)
    result = _prettify_html(result, "body")

    dbg_path = test_path / "markdown_to_html" / "setex_.html"
    if result != expected:
        dbg_path.write_text("\n".join(result))
    elif dbg_path.exists():
        dbg_path.unlink()

    assert expected == result
