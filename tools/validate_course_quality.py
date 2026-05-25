"""Course quality validation.

Run as `python3 tools/validate_course_quality.py` from the course root, or as
`python3 ai_llm_rag_agentic_engineer_course/tools/validate_course_quality.py`
from the workspace root.

Exits non-zero with a list of specific issues if any checked invariant fails.
Designed to catch the failure modes called out in the handoff prompt:

- repeated fill-in question structures across the bank;
- duplicate question text within a file;
- generic placeholder dictionary definitions;
- missing numbered references;
- missing answer key sections;
- too-short dictionaries / project labs / deep dives;
- deep_dive files that do not include a production failure modes section;
- chapters missing any required file;
- identical templated blocks reused across chapters (e.g. Practical Debug
  Questions or project_lab introductions).
"""

from pathlib import Path
import re
import sys
from collections import Counter, defaultdict


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"


REQUIRED_CHAPTER_FILES = [
    "README.md",
    "lesson.md",
    "deep_dive.md",
    "examples.md",
    "homework.md",
    "quiz.md",
    "question_bank.md",
    "projects.md",
    "project_lab.md",
    "dictionary.md",
    "resources.md",
    "references_numbered.md",
]


FORBIDDEN_PATTERNS = [
    "To master `",
    "To master AI engineering",
    "document its definition, implementation role, failure mode, metric, and ________ reference",
    "A core term in",
    "Beginner Level",
    "Intermediate Level",
    "Advanced Level",
    # Catch the renamed-but-still-template version that previously slipped through.
    "Beginner Requirements",
    "Intermediate Requirements",
    "Advanced Requirements",
]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def find_sections(text: str) -> dict[str, str]:
    """Return {section title -> body} for every '## Heading' in the file."""
    sections: dict[str, str] = {}
    matches = list(re.finditer(r"^## (?P<title>.+)$", text, flags=re.M))
    for i, m in enumerate(matches):
        title = m.group("title").strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[title] = text[start:end].strip()
    return sections


def numbered_items(block: str) -> list[str]:
    """Collect numbered list items from a section body (handles multi-line items)."""
    items: list[str] = []
    current: list[str] = []
    for line in block.splitlines():
        if re.match(r"^\s*\d+\. ", line):
            if current:
                items.append(" ".join(current).strip())
            current = [line.strip()]
        elif current and line.strip():
            current.append(line.strip())
        elif current and not line.strip():
            items.append(" ".join(current).strip())
            current = []
    if current:
        items.append(" ".join(current).strip())
    return items


def stem_prefix(line: str, words: int = 6) -> str:
    text = re.sub(r"^\s*\d+\.\s*", "", line)
    return " ".join(text.split()[:words]).lower()


# -------------------- per-file checks --------------------

def check_forbidden(path: Path, text: str) -> list[str]:
    return [
        f"{rel(path)}: forbidden generic pattern {p!r}"
        for p in FORBIDDEN_PATTERNS
        if p in text
    ]


def check_chapter_files(chapter_dir: Path) -> list[str]:
    errors: list[str] = []
    for fname in REQUIRED_CHAPTER_FILES:
        if not (chapter_dir / fname).exists():
            errors.append(f"{rel(chapter_dir)}/{fname}: required chapter file missing")
    return errors


def check_question_bank(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    errors.extend(check_forbidden(path, text))
    sections = find_sections(text)

    required_sections = [
        "Multiple Choice",
        "Applied Multiple Choice",
        "Fill In The Blanks",
        "Short Answer",
        "Scenario Questions",
        "Practical Debug Questions",
        "Answer Key",
        "References",
    ]
    for sec in required_sections:
        if sec not in sections:
            errors.append(f"{rel(path)}: missing section '## {sec}'")

    # Fill-in-the-blank checks
    fill_lines = numbered_items(sections.get("Fill In The Blanks", ""))
    if len(fill_lines) < 6:
        errors.append(
            f"{rel(path)}: expected at least 6 fill-in-the-blank items, got {len(fill_lines)}"
        )
    if len(fill_lines) != len(set(fill_lines)):
        errors.append(f"{rel(path)}: duplicate fill-in-the-blank items in same file")
    if fill_lines:
        prefixes = [stem_prefix(line, 6) for line in fill_lines]
        common_prefix, count = Counter(prefixes).most_common(1)[0]
        # Allow at most one duplicated stem prefix; flag if the same opening
        # appears in half or more of the items.
        if count >= max(3, (len(prefixes) + 1) // 2):
            errors.append(
                f"{rel(path)}: fill-in-the-blank items share the same template "
                f"({count}/{len(prefixes)} start with {common_prefix!r})"
            )

    # Multiple choice checks
    mcq_lines = numbered_items(sections.get("Multiple Choice", ""))
    if len(mcq_lines) < 6:
        errors.append(
            f"{rel(path)}: expected at least 6 multiple-choice items, got {len(mcq_lines)}"
        )
    if mcq_lines:
        prefixes = [stem_prefix(line, 5) for line in mcq_lines]
        common_prefix, count = Counter(prefixes).most_common(1)[0]
        if count >= max(3, (len(prefixes) + 1) // 2):
            errors.append(
                f"{rel(path)}: multiple-choice items share the same stem template "
                f"({count}/{len(prefixes)} start with {common_prefix!r})"
            )

    applied_lines = numbered_items(sections.get("Applied Multiple Choice", ""))
    if len(applied_lines) < 4:
        errors.append(
            f"{rel(path)}: expected at least 4 applied multiple-choice items, got {len(applied_lines)}"
        )

    scenario_lines = numbered_items(sections.get("Scenario Questions", ""))
    if len(scenario_lines) < 4:
        errors.append(
            f"{rel(path)}: expected at least 4 scenario questions, got {len(scenario_lines)}"
        )
    if scenario_lines:
        prefixes = [stem_prefix(line, 6) for line in scenario_lines]
        common_prefix, count = Counter(prefixes).most_common(1)[0]
        if count >= max(3, (len(prefixes) + 1) // 2):
            errors.append(
                f"{rel(path)}: scenario items share the same template "
                f"({count}/{len(prefixes)} start with {common_prefix!r})"
            )

    short_lines = numbered_items(sections.get("Short Answer", ""))
    if len(short_lines) < 4:
        errors.append(
            f"{rel(path)}: expected at least 4 short-answer items, got {len(short_lines)}"
        )

    debug_lines = numbered_items(sections.get("Practical Debug Questions", ""))
    if len(debug_lines) < 4:
        errors.append(
            f"{rel(path)}: expected at least 4 practical debug questions, got {len(debug_lines)}"
        )

    answer_key = sections.get("Answer Key", "")
    for sub in ("Multiple Choice", "Applied Multiple Choice", "Fill In The Blanks"):
        if sub not in answer_key:
            errors.append(f"{rel(path)}: answer key missing '{sub}' subsection")

    return errors


def check_dictionary(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    errors.extend(check_forbidden(path, text))

    rows = [line for line in text.splitlines() if line.startswith("| `")]
    if len(rows) < 5:
        errors.append(f"{rel(path)}: dictionary has only {len(rows)} terms; expected at least 5")

    placeholder_phrases = [
        "specific concept in",
        "needs an explicit, non-generic definition",
        "unclear concepts create unclear architecture",
    ]
    for phrase in placeholder_phrases:
        if phrase in text:
            errors.append(f"{rel(path)}: contains placeholder definition phrase {phrase!r}")

    definitions = []
    for row in rows:
        cells = [c.strip() for c in row.split("|")[1:-1]]
        if len(cells) >= 2:
            definitions.append(cells[1])
    if len(definitions) != len(set(definitions)):
        errors.append(f"{rel(path)}: duplicate definition column values across terms")

    return errors


def check_deep_dive(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    errors.extend(check_forbidden(path, text))
    sections = find_sections(text)
    for required in ("Thesis", "Core Concepts", "Production Failure Modes", "References"):
        if required not in sections:
            errors.append(f"{rel(path)}: missing section '## {required}'")
    failure_body = sections.get("Production Failure Modes", "")
    if len(failure_body) < 200:
        errors.append(
            f"{rel(path)}: 'Production Failure Modes' is too short ({len(failure_body)} chars)"
        )
    if len(text) < 1500:
        errors.append(f"{rel(path)}: deep_dive too short ({len(text)} chars)")
    return errors


def check_project_lab(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    errors.extend(check_forbidden(path, text))
    sections = find_sections(text)
    if "References" not in sections:
        errors.append(f"{rel(path)}: missing '## References'")
    if len(text) < 2500:
        errors.append(f"{rel(path)}: project_lab too short ({len(text)} chars)")
    for needed in ("Acceptance Criteria", "Metric", "Failure"):
        if needed.lower() not in text.lower():
            errors.append(f"{rel(path)}: project_lab missing concrete element '{needed}'")
    return errors


def check_lesson(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    errors.extend(check_forbidden(path, text))
    if "## Numbered References" not in text and "## References" not in text:
        errors.append(f"{rel(path)}: lesson missing numbered references section")
    return errors


def check_references_numbered(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    entries = re.findall(r"^\[\d+\]", text, flags=re.M)
    if len(entries) < 4:
        errors.append(
            f"{rel(path)}: expected at least 4 numbered reference entries, got {len(entries)}"
        )
    return errors


# -------------------- cross-file checks --------------------

def check_cross_file_uniqueness() -> list[str]:
    errors: list[str] = []

    # Practical Debug Questions used to be the same five questions in every chapter.
    debug_blocks: dict[str, list[str]] = defaultdict(list)
    for qb in CHAPTERS.glob("*/question_bank.md"):
        sections = find_sections(qb.read_text(encoding="utf-8"))
        block = sections.get("Practical Debug Questions", "").strip()
        if block:
            debug_blocks[block].append(rel(qb))
    for block, paths in debug_blocks.items():
        if len(paths) > 3:
            errors.append(
                f"'Practical Debug Questions' block is byte-identical in {len(paths)} chapters "
                f"(e.g. {paths[0]}). Vary content per chapter."
            )

    # Project lab opening paragraph used to be identical across all 17 chapters.
    lab_intros: dict[str, list[str]] = defaultdict(list)
    for lab in CHAPTERS.glob("*/project_lab.md"):
        text = lab.read_text(encoding="utf-8")
        lines = [l for l in text.splitlines() if l.strip() and not l.startswith("#")]
        if lines:
            lab_intros[lines[0].strip()].append(rel(lab))
    for intro, paths in lab_intros.items():
        if len(paths) > 3:
            errors.append(
                f"Project lab opening line is identical in {len(paths)} chapters "
                f"(e.g. {paths[0]}). Make each chapter's framing concrete."
            )

    return errors


# -------------------- main --------------------

def main() -> int:
    errors: list[str] = []

    chapter_dirs = sorted(p for p in CHAPTERS.iterdir() if p.is_dir())
    if not chapter_dirs:
        print(f"no chapters found under {CHAPTERS}")
        return 1

    for chapter in chapter_dirs:
        errors.extend(check_chapter_files(chapter))

    for path in CHAPTERS.glob("*/question_bank.md"):
        errors.extend(check_question_bank(path))
    for path in CHAPTERS.glob("*/dictionary.md"):
        errors.extend(check_dictionary(path))
    for path in CHAPTERS.glob("*/deep_dive.md"):
        errors.extend(check_deep_dive(path))
    for path in CHAPTERS.glob("*/project_lab.md"):
        errors.extend(check_project_lab(path))
    for path in CHAPTERS.glob("*/lesson.md"):
        errors.extend(check_lesson(path))
    for path in CHAPTERS.glob("*/references_numbered.md"):
        errors.extend(check_references_numbered(path))

    errors.extend(check_cross_file_uniqueness())

    if errors:
        print(f"course quality validation FAILED: {len(errors)} issue(s)")
        for e in sorted(errors):
            print(f"  - {e}")
        return 1

    print("course quality validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
