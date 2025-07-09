from pathlib import Path

import pytest

from h2m2t.h2t import html_to_text


@pytest.mark.parametrize(
    "case",
    [
        "article2",
        "article3",
        "article4",
        "break",
        "comment1",
        "comment2",
        "empty",
        "no_space",
        "space",
    ],
)
def test_text(case: str) -> None:
    test_path = Path(__file__).resolve().parent.parent / "tests" / "html_to_text"

    src_path = test_path / f"{case}.html"
    src_html = src_path.read_text()

    gt_path = test_path / f"{case}.txt"
    expected = gt_path.read_text()

    result = html_to_text(src_html, "html.parser")

    dbg_path = test_path / f"{case}_.txt"
    if result != expected:
        dbg_path.write_text(result)
    elif dbg_path.exists():
        dbg_path.unlink()

    assert expected.splitlines() == result.splitlines()


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
def test_hard(case: str) -> None:
    test_path = Path(__file__).resolve().parent.parent / "tests"

    src_path = test_path / "html_to_markdown" / f"{case}.html"
    src_html = src_path.read_text()

    gt_path = test_path / "html_to_text" / f"{case}.txt"
    expected = gt_path.read_text()

    result = html_to_text(src_html, "html.parser")

    dbg_path = test_path / "html_to_text" / f"{case}_.txt"
    if result != expected:
        dbg_path.write_text(result)
    elif dbg_path.exists():
        dbg_path.unlink()

    assert expected.splitlines() == result.splitlines()
