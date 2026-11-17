# === Stage 7: Сортировка записей ===
# Project: BrewLog
def sort_brews(brews, key="name", reverse=False):
    return sorted(brews, key=lambda b: b.get(key, ""), reverse=reverse)


def sort_brews_by_date(brews, reverse=False):
    return sorted(brews, key=lambda b: b.get("date", ""), reverse=reverse)


def sort_brews_by_name(brews, reverse=False):
    return sorted(brews, key=lambda b: b.get("name", "").lower(), reverse=reverse)


def sort_brews_by_date_then_name(brews, reverse=False):
    return sorted(
        brews,
        key=lambda b: (b.get("date", ""), b.get("name", "").lower()),
        reverse=reverse,
    )


def sort_brews_by_name_then_date(brews, reverse=False):
    return sorted(
        brews,
        key=lambda b: (b.get("name", "").lower(), b.get("date", "")),
        reverse=reverse,
    )


def sort_brews_by_name_and_date(brews, name_reverse=False, date_reverse=False):
    return sorted(
        brews,
        key=lambda b: (b.get("name", "").lower(), b.get("date", "")),
        reverse=name_reverse,
    )


def sort_brews_by_name_desc(brews):
    return sort_brews_by_name(brews, reverse=True)


def sort_brews_by_date_desc(brews):
    return sort_brews_by_date(brews, reverse=True)


def sort_brews_by_date_asc(brews):
    return sort_brews_by_date(brews, reverse=False)


def sort_brews_by_name_asc(brews):
    return sort_brews_by_name(brews, reverse=False)


def sort_brews_by_name_then_date_asc(brews):
    return sort_brews_by_name_then_date(brews, reverse=False)


def sort_brews_by_name_then_date_desc(brews):
    return sort_brews_by_name_then_date(brews, reverse=True)


if __name__ == "__main__":
    sample = [
        {"name": "IPA", "date": "2024-01-15"},
        {"name": "Stout", "date": "2024-01-10"},
        {"name": "Lager", "date": "2024-01-12"},
    ]
    print(sort_brews_by_name_asc(sample))
    print(sort_brews_by_date_asc(sample))
    print(sort_brews_by_name_then_date_asc(sample))
    print(sort_brews_by_name_then_date_desc(sample))
