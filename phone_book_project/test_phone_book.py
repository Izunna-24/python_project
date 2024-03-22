import unittest

from phone_book_project import phone_book


class TestPhoneBook(unittest.TestCase):

    def test_that_phone_book_can_save_contact(self):
        contact_name = phone_book.get_contact_name()
        contact_number = phone_book.get_contact_number()
        assert len(contact_name) == 0
        assert len(contact_number) == 0

        phone_book.add_contact('Duncan', '09023849568')
        assert len(contact_name) == 1
        assert len(contact_number) == 1

    def test_that_phone_book_can_delete_contact(self):
        assert len(phone_book.get_contact_name()) == 0
        assert len(phone_book.get_contact_number()) == 0

        phone_book.add_contact('Duncan', '09023849568')
        assert len(phone_book.get_contact_name()) == 1
        assert len(phone_book.get_contact_number()) == 1

        phone_book.delete_contact('Duncan', '09023849568')
        assert len(phone_book.get_contact_number()) == 0
        assert len(phone_book.get_contact_number()) == 0

    def test_that_phone_book_can_get_all_contacts(self):
        assert len(phone_book.get_contact_name()) == 0
        assert len(phone_book.get_contact_number()) == 0

        phone_book.add_contact('Duncan', '09023849568')
        assert len(phone_book.get_contact_name()) == 1
        assert len(phone_book.get_contact_number()) == 1

        phone_book.search_contact('Duncan')
        assert len(phone_book.get_contact_name()) == phone_book.search_contact('Duncan')




