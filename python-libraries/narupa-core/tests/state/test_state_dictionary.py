import time
from concurrent.futures.thread import ThreadPoolExecutor

import pytest
from narupa.core.key_lockable_map import ResourceLockedError
from narupa.core.change_buffers import DictionaryChange
from narupa.core.state_dictionary import StateDictionary


BACKGROUND_THREAD_ACTION_TIME = .1

ACCESS_TOKEN_1 = object()
ACCESS_TOKEN_2 = object()

INITIAL_STATE = {
    'hello': 100,
    'test': {'baby': 'yoda'},
}


@pytest.fixture
def state_dictionary() -> StateDictionary:
    state_dictionary = StateDictionary()
    change = DictionaryChange(INITIAL_STATE, set())
    state_dictionary.update_state(None, change)
    return state_dictionary


def test_initial_state(state_dictionary):
    """
    Test that the initial state of the dictionary gets set.
    """
    with state_dictionary.lock_content() as current_state:
        assert current_state == INITIAL_STATE


def test_update_unlocked(state_dictionary):
    """
    Test that unlocked keys can be changed and removed.
    """
    update = DictionaryChange({'hello': 50}, {'test'})
    state_dictionary.update_state(ACCESS_TOKEN_1, update)

    with state_dictionary.lock_content() as current_state:
        assert current_state == {'hello': 50, }


def test_partial_lock_atomic(state_dictionary):
    """
    Test that an update attempt has no effect if the whole update cannot be
    made.
    """
    state_dictionary.update_locks(ACCESS_TOKEN_2, {'hello': 10}, set())
    update = DictionaryChange({'hello': 50, 'goodbye': 50}, set())

    with pytest.raises(ResourceLockedError):
        state_dictionary.update_state(ACCESS_TOKEN_1, update)

    with state_dictionary.lock_content() as current_state:
        assert current_state == INITIAL_STATE


def test_unheld_releases_ignored(state_dictionary):
    """
    Test that attempting to release locks on keys which are not locked with this
    access token will not prevent the update from occurring.
    """
    update = DictionaryChange({'hello': 50}, {'goodbye'})
    state_dictionary.update_state(ACCESS_TOKEN_1, update)

    with state_dictionary.lock_content() as current_state:
        assert current_state['hello'] == 50


def test_locked_content_is_unchanged(state_dictionary):
    """
    Test that background changes to the StateDictionary do not take effect while
    an exclusive lock is held on the entire state.
    """
    thread_pool = ThreadPoolExecutor(max_workers=1)

    def meddle_with_state(state_dictionary):
        state_dictionary.update_state(
            ACCESS_TOKEN_1,
            DictionaryChange({'hello': 50}, set()),
        )

    with state_dictionary.lock_content() as content:
        thread_pool.submit(meddle_with_state, state_dictionary)
        time.sleep(BACKGROUND_THREAD_ACTION_TIME)
        assert content == INITIAL_STATE


def test_locked_content_changes_after(state_dictionary):
    """
    Test that changes to the StateDictionary attempted while an exclusive lock
    was held on the entire state will take effect once the lock is released.
    """
    thread_pool = ThreadPoolExecutor(max_workers=1)

    def meddle_with_state(state):
        state.update_state(
            ACCESS_TOKEN_1,
            DictionaryChange({'hello': 50}, set()),
        )

    with state_dictionary.lock_content() as content:
        thread_pool.submit(meddle_with_state, state_dictionary)
        time.sleep(BACKGROUND_THREAD_ACTION_TIME)

    time.sleep(BACKGROUND_THREAD_ACTION_TIME)

    with state_dictionary.lock_content() as content:
        assert content['hello'] == 50
