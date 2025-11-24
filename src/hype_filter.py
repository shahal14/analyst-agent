def hype_filter(article):
    """Return True if article passes the information-density filter.
    Heuristics: not too short, contains at least one named entity-like token (capitalized token),
    and avoid pure marketing keywords.
    """
    text = article.get('content') or article.get('description') or article.get('title') or ""
    text = (text or "").strip()
    if not text:
        return False

    # Minimum words
    if len(text.split()) < 40:
        return False

    low_info_keywords = [
        'celebrate', 'celebrating', 'launch', 'announcement', 'award', 'partnership',
        'announce', 'happy to', 'proud to', 'join us', 'signing'
    ]

    lowered = text.lower()
    for kw in low_info_keywords:
        if kw in lowered:
            return False

    # Quick heuristic: require at least one capitalized word that is not start of sentence
    tokens = text.split()
    capitalized = [t for t in tokens[1:20] if t[0].isupper()]
    if len(capitalized) == 0:
        return False

    return True
