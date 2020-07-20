from pysnoonotes.core import SnooNotes
import pytest
from pysnoonotes.errors import LoginFailedError


class TestSnooNotes:
    def _sub_notes(self, subreddit, cache, key):
        return SnooNotes("pysnoonotestest", key).get_notes_for_subreddit(subreddit, use_cache=cache)["SubName"] == subreddit

    def test_sub_notes(self, key):
        assert self._sub_notes("pysnoonotes_test", False, key)

    def test_sub_notes_caching(self, key):
        # Uses the previous cache
        assert self._sub_notes("pysnoonotes_test", True, key)

    # Usernotes check
    def test_dictionary_return(self, key):
        assert isinstance(SnooNotes("pysnoonotestest", key).get_notes_for_user("pysnoonotestest"), dict)

    def test_multiple_users_dict_return(self, key):
        assert isinstance(SnooNotes("pysnoonotestest", key).get_notes_for_user(["pysnoonotestest", "pysnoonotestest"]), dict)

    # Login Fail check
    def test_should_raise_login_error(self):
        with pytest.raises(LoginFailedError):
            SnooNotes("wrong_username", "wrong_password").get_access_token()
    
    # Test note addition and deletion for a user.
    def test_adding_note(self, key):
        initial_notes = len(SnooNotes("pysnoonotestest", key).get_notes_for_user("pysnoonotestest")['pysnoonotestest'])
        SnooNotes("pysnoonotestest", key).add_note_for_user("pysnoonotestest", "4763", "pysnoonotes_test", "pytest", "https://old.reddit.com/r/pysnoonotes_test/comments/hugnjr/test/")
        assert len(SnooNotes("pysnoonotestest", key).get_notes_for_user("pysnoonotestest")['pysnoonotestest']) == initial_notes + 1

    def test_deleting_note(self, key):
        note_list = SnooNotes("pysnoonotestest", key).get_notes_for_user("pysnoonotestest")['pysnoonotestest']
        initial_notes = len(note_list)
        SnooNotes("pysnoonotestest", key).delete_note_for_user("pysnoonotestest", note_list[-1]["NoteID"])
        assert len(SnooNotes("pysnoonotestest", key).get_notes_for_user("pysnoonotestest")['pysnoonotestest']) == initial_notes - 1

    # Token shouldn't refresh if last refresh was less than an hour ago
    def test_no_tokens_refresh(self, key):
        sn = SnooNotes("pysnoonotestest", key)
        sn.get_access_token()
        assert sn.refresh_access_token() == 0
