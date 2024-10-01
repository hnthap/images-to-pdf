import unittest

from display import beautify_size_bytes


class TestDisplay(unittest.TestCase):
    def setUp(self) -> None:
        self.fn = beautify_size_bytes
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_zero_bytes(self):
        self.assertEqual(self.fn(0), '0 B')
        self.assertEqual(self.fn(0, decimal=True), '0 B')
        self.assertEqual(self.fn(0, force_int=True), '0 B')
        self.assertEqual(
            self.fn(0, force_int=True, decimal=True), '0 B')

    def test_one_byte(self):
        self.assertEqual(self.fn(1), '1 B')
        self.assertEqual(self.fn(1, decimal=True), '1 B')
        self.assertEqual(self.fn(1, force_int=True), '1 B')
        self.assertEqual(
            self.fn(1, force_int=True, decimal=True), '1 B')

    def test_one_kibibyte_or_kilobyte(self):
        self.assertEqual(self.fn(1024), '1.00 KiB')
        self.assertEqual(self.fn(1000, decimal=True), '1.00 KB')
        self.assertEqual(self.fn(1024, force_int=True), '1 KiB')
        self.assertEqual(
            self.fn(1000, force_int=True, decimal=True), '1 KB')

    def test_one_mebibyte_or_megabyte(self):
        self.assertEqual(self.fn(1024 * 1024), '1.00 MiB')
        self.assertEqual(
            self.fn(1000 * 1000, decimal=True), '1.00 MB')
        self.assertEqual(
            self.fn(1024 * 1024, force_int=True), '1 MiB')
        self.assertEqual(
            self.fn(1000 * 1000, force_int=True, decimal=True), 
            '1 MB')

    def test_one_gibibyte_or_gigabyte(self):
        self.assertEqual(self.fn(1024 * 1024 * 1024), '1.00 GiB')
        self.assertEqual(
            self.fn(1000 * 1000 * 1000, decimal=True), '1.00 GB')
        self.assertEqual(
            self.fn(1024 * 1024 * 1024, force_int=True), '1 GiB')
        self.assertEqual(
            self.fn(
                1000 * 1000 * 1000, force_int=True, decimal=True), 
            '1 GB')

    def test_negative_bytes(self):
        self.assertEqual(self.fn(-1), '-1 B')
        self.assertEqual(self.fn(-1, decimal=True), '-1 B')
        self.assertEqual(self.fn(-1, force_int=True), '-1 B')
        self.assertEqual(
            self.fn(-1, force_int=True, decimal=True), '-1 B')

    def test_negative_one_kibibyte_or_kilobyte(self):
        self.assertEqual(self.fn(-1024), '-1.00 KiB')
        self.assertEqual(self.fn(-1000, decimal=True), '-1.00 KB')
        self.assertEqual(self.fn(-1024, force_int=True), '-1 KiB')
        self.assertEqual(
            self.fn(-1000, force_int=True, decimal=True), '-1 KB')

    def test_1025_bytes_to_kibibytes(self):
        self.assertEqual(self.fn(1025), '1.00 KiB')
        self.assertEqual(self.fn(1025, force_int=True), '1.00 KiB')

    def test_1000100_bytes_to_megabytes(self):
        self.assertEqual(self.fn(1000100, decimal=True), '1.00 MB')
        self.assertEqual(
            self.fn(1000100, decimal=True, force_int=True), '1.00 MB')


if __name__ == '__main__':
    unittest.main()
