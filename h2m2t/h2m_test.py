from pathlib import Path

import pytest

from h2m2t.h2m import html_to_markdown


@pytest.mark.parametrize(
    "case",
    [
        "citilink",
        "dns",
        "drive2",
        "gazeta",
        "habr",
        "iv1",
        "iv2",
        "iv3",
        "iv4",
        "iv5",
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
@pytest.mark.parametrize(
    "parser",
    ["html.parser", "lxml", "html5lib"],
)
def test_md(parser: str, case: str) -> None:
    test_path = Path(__file__).resolve().parent.parent / "tests" / "html_to_markdown"

    src_path = test_path / f"{case}.html"
    src_html = src_path.read_text()

    gt_path = test_path / f"{case}_{parser}.md"
    if not gt_path.exists():
        gt_path = test_path / f"{case}.md"
    expected = gt_path.read_text()

    result = html_to_markdown(src_html, parser)

    # if result != expected:
    #     (test_path / f"{case}_{parser}_.md").write_text(result)
    # elif (test_path / f"{case}_{parser}_.md").exists():
    #     (test_path / f"{case}_{parser}_.md").unlink()

    assert expected.splitlines() == result.splitlines()
