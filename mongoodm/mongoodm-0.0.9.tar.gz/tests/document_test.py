import unittest
import mongoodm

DEFAULT_UNSAVED_OBJ = {
    '_saved': False
}

class TestDocument(unittest.TestCase):
    def setUp(self):
        class TestUser(mongoodm.Document):
            username = ""
            email = ""
        
        self.TestUser = TestUser
        self.db = mongoodm.MongoODM(provider="mongomock")

    def test_save_attribute(self):
        user = self.TestUser()
        new_username = "new_username"
        new_password = "averyunsecurepassword"
        user.username = new_username
        user.password = new_password
        pass

    def test_unsaved_attributes(self):
        user = self.TestUser()
        new_username = "new_username"
        new_password = "averyunsecurepassword"
        self.assertEqual(DEFAULT_UNSAVED_OBJ, user._unsavedItems)

        user.username = new_username
        user.password = new_password

        self.assertIn("username", user._unsavedItems)
        self.assertIn("password", user._unsavedItems)

    def test_unsaved_items(self):
        user = self.TestUser()
        new_username = "new_username"
        new_password = "averyunsecurepassword"
        self.assertEqual(DEFAULT_UNSAVED_OBJ, user._unsavedItems)

        user["username"] = new_username
        user["password"] = new_password

        self.assertIn("username", user._unsavedItems)
        self.assertIn("password", user._unsavedItems)

    def test_can_saved(self):
        pass

