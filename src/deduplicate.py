from difflib import SequenceMatcher

def similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a or "", b or "").ratio()

def deduplicate_articles(articles, title_threshold=0.65):
    """Simple dedupe based on title similarity and source+title exact match.
    Returns a list of unique articles.
    """
    unique = []
    seen = set()

    for art in articles:
        title = (art.get("title") or "").strip()
        source = (art.get("source", {}).get("name") or "").strip()

        key = f"{source}||{title}"
        if key in seen:
            continue

        is_dup = False
        for u in unique:
            if similar(title, u.get("title", "")) >= title_threshold:
                is_dup = True
                break

        if not is_dup:
            unique.append(art)
            seen.add(key)

    return unique
