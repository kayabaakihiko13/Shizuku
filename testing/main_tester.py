import unittest
from testing.test_call_api import TesterScrapingGoogleMap

if __name__ == "__main__":
    testing_Scraping_api = [
        TesterScrapingGoogleMap,
    ]

    # Membuat TestSuite dan menambahkan tes dari kelas-kelas pengujian
    all_tests = unittest.TestSuite(
        unittest.TestLoader().loadTestsFromTestCase(test_case)
        for test_case in testing_Scraping_api
    )

    # Menjalankan semua tes dengan TextTestRunner
    unittest.TextTestRunner(verbosity=2).run(all_tests)
