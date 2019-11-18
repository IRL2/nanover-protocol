# Copyright (c) Intangible Realities Lab, University Of Bristol. All rights reserved.
# Licensed under the GPL. See License.txt in the project root for license information.
"""
Module providing utility classes used by the multiplayer service to create a
shared key/value store between multiple clients.
"""
from __future__ import annotations
from contextlib import contextmanager
from threading import Lock, Condition
from typing import Any, Set, Dict, ContextManager, Tuple, Iterator

from narupa.core.timing import yield_interval

KeyUpdates = Dict[str, Any]
KeyRemovals = Set[str]
DictionaryChange = Tuple[KeyUpdates, KeyRemovals]


class ObjectFrozenException(Exception):
    """
    Raised when an operation on an object cannot be performed because the
    object has been frozen.
    """
    pass


class DictionaryChangeMultiView:
    """
    Provides a means to acquire multiple independent DictionaryChangeBuffers
    tracking a shared dictionary.
    """
    _content: Dict[str, Any]
    _frozen: bool
    _lock: Lock
    _views: Set

    def __init__(self):
        self._content = {}
        self._frozen = False
        self._lock = Lock()
        self._views = set()

    @contextmanager
    def create_view(self) -> ContextManager[DictionaryChangeBuffer]:
        """
        Returns a new DictionaryChangeBuffer that tracks changes to the
        shared dictionary, starting with the initial values.
        """
        with self._lock:
            view = DictionaryChangeBuffer()
            view.update(self._content)
            if self._frozen:
                view.freeze()
            self._views.add(view)
        yield view
        self.remove_view(view)

    def remove_view(self, view: DictionaryChangeBuffer):
        """
        Freeze the given change buffer and stop providing updates to it.
        """
        with self._lock:
            self._views.remove(view)
            view.freeze()

    def subscribe_changes(self, interval: float = 0) \
            -> Iterator[DictionaryChange]:
        """
        Iterates over changes to the shared dictionary, starting with the
        initial values. Waits at least :interval: seconds between each
        iteration.
        """
        with self.create_view() as view:
            yield from view.subscribe_changes(interval)

    def update(self, updates: KeyUpdates, removals: KeyRemovals = frozenset()):
        """
        Updates the shared dictionary with key values pairs from :updates:.
        """
        with self._lock:
            if self._frozen:
                raise ObjectFrozenException()
            self._content.update(updates)
            for view in set(self._views):
                try:
                    view.update(updates, removals)
                except ObjectFrozenException:
                    self._views.remove(view)

    def freeze(self):
        """
        Prevent any further updates to the shared dictionary, ensuring that
        future views and subscriptions are frozen and provide a single update
        with the final values.
        """
        with self._lock:
            self._frozen = True
            for view in self._views:
                view.freeze()


class DictionaryChangeBuffer:
    """
    Tracks the latest values of keys that have changed between checks.
    """
    _frozen: bool
    _lock: Lock
    _any_changes: Condition
    _changes: Dict[str, Any]
    _removals: Set[str]

    def __init__(self):
        self._frozen = False
        self._lock = Lock()
        self._any_changes = Condition(self._lock)
        self._changes = {}
        self._removals = set()

    def freeze(self):
        """
        Freeze the buffer, ensuring that it cannot be updated with any more
        changes.

        It will still be possible to flush changes one last time if there were
        any unflushed at the time of freezing.
        """
        with self._lock:
            self._frozen = True
            self._any_changes.notify()

    def update(self, updates: KeyUpdates, removals: KeyRemovals = frozenset()):
        """
        Update the known changes from a dictionary of keys that have changed
        to their new values.
        """
        with self._lock:
            if self._frozen:
                raise ObjectFrozenException()
            self._changes.update(updates)
            self._removals.update(removals)
            self._any_changes.notify()

    def flush_changed_blocking(self) -> DictionaryChange:
        """
        Wait until there are changes and then return them, clearing all
        tracked changes.
        """
        with self._any_changes:
            while not self._changes and not self._removals:
                if self._frozen:
                    raise ObjectFrozenException()
                self._any_changes.wait()
            changes = self._changes
            removals = self._removals
            self._changes = dict()
            self._removals = set()
            return changes, removals

    def subscribe_changes(self, interval: float = 0) \
            -> Iterator[DictionaryChange]:
        """
        Iterates over changes to the buffer. Waits at least :interval: seconds
        between each iteration.
        """
        for dt in yield_interval(interval):
            try:
                yield self.flush_changed_blocking()
            except ObjectFrozenException:
                break
