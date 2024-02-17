from Shizuku.call_api import ScrapingGoogleMap
import unittest


class TesterScrapingGoogleMap(unittest.TestCase):
    def setUp(self):
        self.query = "Kopi Kenangan"
        self.lat = (-7.275612,)
        self.long = (112.6302807,)
        self.num_pages = (5,)
        self.results_per_page = 20

    def tester_query_None(self):
        with self.assertRaises(ValueError, msg="masukan kata kunci nya"):
            ScrapingGoogleMap(
                lat=self.lat,
                long=self.long,
                num_pages=self.num_pages,
                results_per_page=self.results_per_page,
                query=None,
            )


if __name__ == "__main__":
    unittest.main()
