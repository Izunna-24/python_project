from unittest import TestCase
from back_to_sender_store.logistics import BLogistics


class TestBLogistics(TestCase):
    def test_hasRiders(self):
        b_logistics = BLogistics()
        self.assertTrue(b_logistics.hasriders())

    def test_paymentForDeliveryLessThan50Is_160(self):
        b_logistics = BLogistics()
        self.assertEqual(6_440, b_logistics.daily_payment(9))

    def test_paymentForDeliveryLessThan59(self):
        b_logistics = BLogistics()
        actual = b_logistics.daily_payment(57)
        expected = 16_400
        self.assertEqual(expected, actual)

    def test_paymentForDeliveryLessThan69(self):
        b_logistics = BLogistics()
        actual = b_logistics.daily_payment(69)
        expected = 22_250
        self.assertEqual(expected, actual)

    def test_paymentForDeliveryGreaterThan69(self):
        b_logistics = BLogistics()
        actual = b_logistics.daily_payment(70)
        expected = 40_000
        self.assertEqual(expected, actual)

    def test_paymentForDeliveryLessThan0ThrowsException(self):
        b_logistics = BLogistics()
        with self.assertRaises(ValueError):
            b_logistics.daily_payment(-1)

    def test_paymentForDeliveryGreaterThan100ThrowsException(self):
        b_logistics = BLogistics()
        with self.assertRaises(ValueError):
            b_logistics.daily_payment(105)
