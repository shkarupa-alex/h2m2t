from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter

from h2m2t.table import tables_to_dense


def _prettify_html(html: str, root: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    html = soup.find(root).prettify(formatter=HTMLFormatter(indent=4))
    return html.strip().splitlines()


@pytest.mark.parametrize(
    "deduplicate",
    [False, True],
)
@pytest.mark.parametrize(
    "case",
    [
        "deep",
        "iv",
        "order",
        "overflow1",
        "overflow2",
        "overflow3",
        "parts",
        "row1",
        "row2",
        "rowcol1",
        "rowcol2",
        "rowcol3",
        "rowcol4",
        "rowcol5",
        "rowcol6",
        "simple",
    ],
)
@pytest.mark.parametrize(
    "parser",
    ["html.parser", "lxml", "html5lib"],
)
def test_span(parser: str, case: str, deduplicate: bool, root: str = "table", unwrap: bool = False) -> None:  # noqa: FBT001, FBT002
    test_path = Path(__file__).resolve().parent.parent / "tests" / "tables_to_dense"

    src_path = test_path / f"{case}_src.html"
    src_html = src_path.read_text()

    ddp_path = test_path / f"{case}_ddp.html"
    gt_path = ddp_path if deduplicate and ddp_path.exists() else test_path / f"{case}_gt.html"
    expected = _prettify_html(gt_path.read_text(), root)

    soup = BeautifulSoup(src_html, parser)
    tables_to_dense(soup, deduplicate=deduplicate, unwrap=unwrap)
    result = _prettify_html(str(soup), root)

    assert expected == result


@pytest.mark.parametrize(
    "deduplicate",
    [False, True],
)
@pytest.mark.parametrize(
    "case",
    ["unwrap1", "unwrap2", "unwrap3"],
)
@pytest.mark.parametrize(
    "parser",
    ["html.parser", "lxml", "html5lib"],
)
def test_unwrap(parser: str, case: str, deduplicate: bool) -> None:  # noqa: FBT001
    test_span(parser=parser, case=case, deduplicate=deduplicate, root="div", unwrap=True)
