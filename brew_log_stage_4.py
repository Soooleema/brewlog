# === Stage 4: Удаление и восстановление ===
# Project: BrewLog
from datetime import datetime


class BrewSession:
    def __init__(self, name, style, volume_ml, date):
        self.name = name
        self.style = style
        self.volume_ml = volume_ml
        self.date = date
        self.soft_deleted = False
        self.deleted_at = None

    def mark_deleted(self):
        self.soft_deleted = True
        self.deleted_at = datetime.now()

    def restore(self):
        self.soft_deleted = False
        self.deleted_at = None

    def is_active(self):
        return not self.soft_deleted

    def __repr__(self):
        status = "активна" if self.is_active() else "удалена"
        return f"<BrewSession {self.name} [{status}]>"


class BrewLogStore:
    def __init__(self):
        self._sessions = {}

    def add_session(self, session):
        self._sessions[session.name] = session

    def get_session(self, name):
        return self._sessions.get(name)

    def list_sessions(self, active_only=True):
        result = []
        for session in self._sessions.values():
            if active_only and not session.is_active():
                continue
            result.append(session)
        return result

    def delete_session(self, name):
        session = self.get_session(name)
        if session is None:
            raise KeyError(f"Варка '{name}' не найдена")
        session.mark_deleted()

    def restore_session(self, name):
        session = self.get_session(name)
        if session is None:
            raise KeyError(f"Варка '{name}' не найдена")
        if session.is_active():
            raise ValueError(f"Варка '{name}' уже активна")
        session.restore()

    def count_active(self):
        return sum(1 for s in self._sessions.values() if s.is_active())

    def count_deleted(self):
        return sum(1 for s in self._sessions.values() if not s.is_active())
