# === Stage 6: Фильтрация записей ===
# Project: BrewLog
from datetime import date


def filter_brews(brews, style=None, start_date=None, end_date=None):
    results = []
    for brew in brews:
        if style is not None and brew.get("style") != style:
            continue
        if start_date is not None and brew.get("date") < start_date:
            continue
        if end_date is not None and brew.get("date") > end_date:
            continue
        results.append(brew)
    return results


def filter_brews_by_style(brews, style):
    return [brew for brew in brews if brew.get("style") == style]


def filter_brews_by_date_range(brews, start_date, end_date):
    return [
        brew
        for brew in brews
        if start_date <= brew.get("date") <= end_date
    ]


def filter_brews_combined(brews, style=None, start_date=None, end_date=None):
    filtered = brews
    if style is not None:
        filtered = filter_brews_by_style(filtered, style)
    if start_date is not None:
        filtered = filter_brews_by_date_range(filtered, start_date, end_date)
    return filtered
