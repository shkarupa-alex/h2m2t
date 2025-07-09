from pathlib import Path

import pytest

from h2m2t.m2t import markdown_to_text


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
        "extra",
        "no_space",
        "space",
    ],
)
def test_text(case: str) -> None:
    test_path = Path(__file__).resolve().parent.parent / "tests" / "markdown_to_text"

    src_path = test_path / f"{case}.md"
    src_md = src_path.read_text()

    gt_path = test_path / f"{case}.txt"
    expected = gt_path.read_text()

    result = markdown_to_text(src_md)

    dbg_path = test_path / f"{case}_.txt"
    if result != expected:
        dbg_path.write_text(result)
    elif dbg_path.exists():
        dbg_path.unlink()

    assert expected.splitlines() == result.splitlines()
