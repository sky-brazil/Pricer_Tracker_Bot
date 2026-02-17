import os
import tempfile
import unittest

from main import load_products
from scraper import parse_price_text


class ParsePriceTextTestCase(unittest.TestCase):
    def test_us_decimal_format(self):
        self.assertEqual(parse_price_text("$1,299.99"), 1299.99)

    def test_eu_decimal_format(self):
        self.assertEqual(parse_price_text("US$ 1.299,99"), 1299.99)

    def test_thousands_without_decimals(self):
        self.assertEqual(parse_price_text("1,299"), 1299.0)
        self.assertEqual(parse_price_text("1.299"), 1299.0)

    def test_invalid_price(self):
        self.assertIsNone(parse_price_text("n/a"))


class LoadProductsTestCase(unittest.TestCase):
    def test_load_products_skips_invalid_or_disabled_rows(self):
        csv_content = (
            "name,url,target_price,currency,selector,enabled\n"
            '"Valid One","https://example.com/a","99.90","USD","span.price",true\n'
            '"Disabled","https://example.com/b","100","USD","span.price",false\n'
            '"Broken","https://example.com/c","n/a","USD","span.price",true\n'
        )

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".csv", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write(csv_content)
            tmp_path = tmp.name

        try:
            products = load_products(tmp_path, default_currency="USD")
            self.assertEqual(len(products), 1)
            self.assertEqual(products[0].name, "Valid One")
            self.assertEqual(products[0].target_price, 99.9)
            self.assertEqual(products[0].selector, "span.price")
        finally:
            os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
