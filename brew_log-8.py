# === Stage 8: Текстовый поиск ===
# Project: BrewLog
import re


def highlight_matches(text: str, needles) -> str:
    """Подсвечивает все совпадения указанных слов в тексте.

    Поиск ведётся без учёта регистра. Каждое найденное вхождение
    оборачивается в ANSI-последовательности, выделяющие его жёлтым
    на тёмном фоне. Совпадения не перекрываются.
    """
    if not text:
        return text

    flags = re.IGNORECASE
    result = []
    pattern = "|".join(re.escape(needle) for needle in needles) if needles else ""
    if not pattern:
        return text

    regex = re.compile(f"({pattern})", flags)

    last = 0
    for match in regex.finditer(text):
        start, end = match.span()
        result.append(text[last:start])
        result.append(
            f"\033[33;40m{match.group()}\033[0m"
        )
        last = end

    result.append(text[last:])
    return "".join(result)


def find_brews_by_text(brews, fields, needles) -> list:
    """Фильтрует список варок по текстовым полям без учёта регистра.

    fields — список имён полей для поиска (например, ['название', 'стиль']).
    needles — список искомых слов; ищутся во всех указанных полях.
    Возвращает список варок, в которых хотя бы в одном из полей
    встречается хотя бы одно из искомых слов (регистронезависимо).
    """
    matches = []
    for brew in brews:
        found = False
        for field in fields:
            value = getattr(brew, field, "")
            if isinstance(value, str) and any(needle in value.lower() for needle in needles):
                found = True
                break
        if found:
            matches.append(brew)
    return matches


def format_brew(brew) -> str:
    """Форматирует варку в читаемую строку для вывода в журнал."""
    return (
        f"{brew.название} "
        f"[{brew.стиль}] "
        f"{brew.объём} л "
        f"{brew.дата}"
    )


def search_and_display(brews, fields, needles) -> str:
    """Выполняет поиск варок по текстовым полям и строит отчёт.

    Выводит результаты, применяя подсветку совпадений к строкам
    каждой найденной варки. Совпадения выделяются жёлтым цветом.
    """
    matches = find_brews_by_text(brews, fields, needles)

    if not matches:
        return "Ничего не найдено."

    report = f"Найдено {len(matches)} варок по запросу: {' '.join(needles)}\n"
    for brew in matches:
        report += highlight_matches(format_brew(brew), needles) + "\n"
    return report
