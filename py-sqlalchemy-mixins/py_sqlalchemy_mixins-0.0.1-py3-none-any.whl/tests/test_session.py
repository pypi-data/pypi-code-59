from tests import MockSession
from mixins.session import SessionMixin, SessionNotSetError
import unittest


class SampleModel(SessionMixin):
    pass


class TestSession(unittest.TestCase):

    def test_session_is_none_by_default(self):
        model = SampleModel()
        assert model._session is None

    def test_session_access(self):
        with self.assertRaises(SessionNotSetError):
            with SampleModel.get_session():
                pass

        with self.assertRaises(SessionNotSetError):
            with SampleModel().get_session():
                pass

    def test_rollback_called_on_error(self):
        mock_session = MockSession()
        SampleModel.set_session(mock_session)

        assert SampleModel._session is not None

        with self.assertRaises(ValueError):
            with SampleModel.get_session():
                raise ValueError("Oopsie")

        # invalid changes are rolled back
        assert mock_session.rollback_called
        # but not committed
        assert not mock_session.commit_called

    def test_commit_called(self):
        mock_session = MockSession()
        SampleModel.set_session(mock_session)

        assert SampleModel._session is not None

        with SampleModel.get_session():
            # do something
            pass

        # valid changes are not rolled back
        assert not mock_session.rollback_called
        # but committed and persisted
        assert mock_session.commit_called

    def tearDown(self) -> None:
        SampleModel._session = None
