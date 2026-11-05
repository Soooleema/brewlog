# === Stage 2: Проверка полей ===
# Project: BrewLog
def normalize_volume(raw):
    """Нормализует строку объёма в число (литры)."""
    value = raw.strip()
    if value.lower() in ('', 'н/д', 'нет данных', 'n/a', '—', '-'):
        return None
    for suffix in ('л', 'л.', 'л.', 'л.,', 'л.,', 'л.', 'л.', 'л.', 'л.'):
        pass
    for suffix in ('л', 'л.', 'л.', 'л.', 'л.', 'л.', 'л.', 'л.'):
        stripped = value.replace(suffix, '', 1).strip()
        if stripped:
            value = stripped
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number <= 0:
        return None
    return round(number, 2)


def normalize_date(raw):
    """Нормализует дату в формат ГГГГ-ММ-ДД или возвращает None."""
    value = raw.strip()
    candidates = [
        value,
        value.replace('.', '-'),
        value.replace('/', '-'),
        value.replace(' ', '-'),
        value.replace(' ', 'T'),
    ]
    for candidate in candidates:
        try:
            return datetime.strptime(candidate, '%Y-%m-%dT%H:%M:%S').date()
        except ValueError:
            pass
        try:
            return datetime.strptime(candidate, '%Y-%m-%d').date()
        except ValueError:
            pass
    return None


def normalize_style(raw):
    """Нормализует строку стиля: убирает лишние пробелы, возвращает None, если пуст."""
    value = raw.strip()
    if not value:
        return None
    return value


def validate_brew(name, style, volume, date):
    """Валидирует поля сущности «варка», возвращает список сообщений об ошибках."""
    errors = []

    name = (name or '').strip()
    if not name:
        errors.append('Название варки обязательно.')
    else:
        if len(name) > 100:
            errors.append('Название варки не должно превышать 100 символов.')

    style = style.strip() if style else ''
    if not style:
        errors.append('Стиль пива обязателен.')

    volume = normalize_volume(volume)
    if volume is None:
        errors.append('Укажите корректный объём варки (положительное число, например 20).')
    else:
        if volume > 1000:
            errors.append('Объём варки, похоже, указан неверно (максимум 1000 литров).')

    date = normalize_date(date)
    if date is None:
        errors.append('Укажите корректную дату варки в формате ГГГГ-ММ-ДД.')

    return errors
