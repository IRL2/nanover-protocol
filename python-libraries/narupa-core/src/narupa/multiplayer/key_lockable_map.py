import time
from threading import RLock


class ResourceLockedException(Exception):
    pass


class KeyLockableMap:
    def __init__(self):
        self._lock = RLock()
        self._key_lock_owners = dict()
        self._key_lock_timeouts = dict()
        self._values = dict()

    def _remove_lock(self, key):
        with self._lock:
            self._key_lock_owners.pop(key, None)
            self._key_lock_timeouts.pop(key, None)

    def _check_lock_timeout(self, key):
        with self._lock:
            now = time.monotonic()
            timeout = self._key_lock_timeouts.get(key, None)
            if timeout and now > timeout:
                self._remove_lock(key)

    def player_can_lock_key(self, player_id, key):
        with self._lock:
            self._check_lock_timeout(key)
            return self._key_lock_owners.get(key, player_id) == player_id

    def lock_key(self, owner_id, key, duration=None):
        with self._lock:
            if not self.player_can_lock_key(owner_id, key):
                raise ResourceLockedException
            self._key_lock_owners[key] = owner_id
            if duration:
                self._key_lock_timeouts[key] = time.monotonic() + duration

    def release_key(self, owner_id, key):
        with self._lock:
            if not self.player_can_lock_key(owner_id, key):
                raise ResourceLockedException
            self._remove_lock(key)

    def remove_owner(self, owner_id):
        with self._lock:
            locked_keys = {key for key, owner in self._key_lock_owners.items() if owner == owner_id}
            for key in locked_keys:
                self._remove_lock(key)

    def set(self, owner_id, key, value):
        with self._lock:
            if not self.player_can_lock_key(owner_id, key):
                raise ResourceLockedException
            self._values[key] = value

    def get(self, resource_id, default=None):
        with self._lock:
            return self._values.get(resource_id, default)

    def get_all(self):
        with self._lock:
            return dict(self._values)
