from pathlib import Path
from runpy import run_path
from typing import cast

PLAN_SCRIPT = Path(__file__).parents[1] / "scripts" / "plan.py"
NOTES_TEMPLATE = cast(str, run_path(str(PLAN_SCRIPT))["NOTES_TEMPLATE"])


def test_notes_template__section_headings__have_blank_line_boundaries() -> None:
    headings = [line for line in NOTES_TEMPLATE.splitlines() if line.startswith("## ")]

    assert headings
    for heading in headings:
        assert f"\n\n{heading}\n\n" in NOTES_TEMPLATE
