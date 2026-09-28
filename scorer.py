from rapidfuzz import fuzz, utils


MATCH_THRESHOLD = 95


def _normalize(text: str) -> str:
    """Normalize punctuation and common equivalent contractions."""
    normalized = utils.default_process(text) or ""
    return normalized.replace("doesn t", "does not")


def _contains_expected_facts(expects: str, text: str) -> bool:
    """Return whether text contains every semicolon-separated expected fact."""
    expected_facts = [fact.strip() for fact in expects.split(";") if fact.strip()]
    if not expected_facts or not text.strip():
        return False

    return all(
        fuzz.token_set_ratio(
            fact,
            text,
            processor=_normalize,
        )
        >= MATCH_THRESHOLD
        for fact in expected_facts
    )


def judge(question, expects, answer, results) -> bool:
    """Apply criteria 1, 2, and 5 from criteria.md to one evaluation run."""
    del question  # Required by the scorer interface but unused here.
    return (
        retrieval_hit(expects, results)
        and names_source(answer, results)
        and _contains_expected_facts(expects, answer)
    )


def retrieval_hit(expects, results) -> bool:
    """Criterion 1: one retrieved chunk contains every expected fact."""
    return any(_contains_expected_facts(expects, chunk.text) for chunk in results)


def names_source(answer, results) -> bool:
    """Criterion 2: the answer names at least one retrieved source document."""
    normalized_answer = answer.casefold()
    return any(chunk.source.casefold() in normalized_answer for chunk in results)