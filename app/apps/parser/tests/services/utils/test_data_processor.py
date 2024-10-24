from django.test          import TestCase

from apps.parser.services import DataProcessor


class DataProcessorTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.processor = DataProcessor()

    def test_rm_html_chars(self) -> None:
        valid_data = self.processor.clean("Test \xa0text")

        self.assertIsInstance(valid_data, str), self.assertTrue(valid_data), self.assertIsNotNone(valid_data)
        self.assertEqual(valid_data, "Test text")

    def test_convert_to_kg(self) -> None:
        valid_data = self.processor.to_kg("72.733 кг")

        self.assertIsInstance(valid_data, float), self.assertTrue(valid_data), self.assertIsNotNone(valid_data)
        self.assertEqual(valid_data, 72.733)

        valid_data = self.processor.to_kg("72 кг")

        self.assertIsInstance(valid_data, float), self.assertTrue(valid_data), self.assertIsNotNone(valid_data)
        self.assertEqual(valid_data, 72.0)

        valid_data = self.processor.to_kg("990 г")

        self.assertIsInstance(valid_data, float), self.assertTrue(valid_data), self.assertIsNotNone(valid_data)
        self.assertEqual(valid_data, 0.99)

        with self.assertRaises(ValueError):
            self.processor.to_kg("кг")

    def test_serialize_date(self) -> None:
        valid_data = self.processor.serialize("7.07.24")

        self.assertIsInstance(valid_data, str), self.assertTrue(valid_data), self.assertIsNotNone(valid_data)
        self.assertEqual(valid_data, "2024-07-7")

        with self.assertRaises(IndexError):
            self.processor.serialize("2024")