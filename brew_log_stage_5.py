# === Stage 5: Связанная сущность ===
# Project: BrewLog
import datetime


class DensityReading:
    def __init__(self, original_gravity, final_gravity, date, batch_id):
        self.original_gravity = original_gravity
        self.final_gravity = final_gravity
        self.date = date
        self.batch_id = batch_id


def add_density_reading(readings, batch, original_gravity, final_gravity, date):
    if original_gravity <= final_gravity:
        raise ValueError("Начальная плотность должна быть больше конечной")
    if not (0.0 <= original_gravity <= 2.0):
        raise ValueError("Плотность должна быть в диапазоне от 0.0 до 2.0")
    reading = DensityReading(original_gravity, final_gravity, date, batch.id)
    readings.append(reading)
    return reading


def calculate_apparent_density(reading):
    if reading.original_gravity == reading.final_gravity:
        return None
    attenuation = (reading.original_gravity - reading.final_gravity) / reading.original_gravity
    return reading.final_gravity / (1 - 0.004 * attenuation)


def calculate_abv(reading):
    if reading.original_gravity == reading.final_gravity:
        return None
    return (reading.original_gravity - reading.final_gravity) * 131.25


def format_reading(reading):
    return (
        f"Замер #{len(reading.batch.density_readings) + 1} "
        f"от {reading.date.strftime('%d.%m.%Y')}: OG={reading.original_gravity}, "
        f"FG={reading.final_gravity}, ABV={calculate_abv(reading):.1f}%"
    )
