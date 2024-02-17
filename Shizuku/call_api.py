from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
from typing import Optional
import csv


def ScrapingGoogleMap(
    query: str,
    api_key: Optional[str] = None,
    lat: Optional[float] = None,
    long: Optional[float] = None,
    num_pages: int = 1,
    results_per_page: int = 10,
) -> None:
    # Check if api_key is provided, otherwise load from environment
    if query is None:
        raise ValueError("masukan kata kunci nya")
    if api_key is None:
        load_dotenv()
        api_key = os.environ.get("SERPAPI_KEY")

    # Check if lat and long are provided
    if lat is None or long is None:
        raise ValueError("Please provide both latitude and longitude.")

    # Check if the number of pages is valid
    if num_pages <= 0:
        raise ValueError("Number of pages should be greater than 0.")

    # Check data types for lat and long
    if not isinstance(lat, float) or not isinstance(long, float):
        raise ValueError("Please provide valid latitude and longitude.")

    results = []

    for page in range(num_pages):
        start_index = page * results_per_page
        params = {
            "engine": "google_maps",
            "q": query,
            "api_key": api_key,
            "ll": f"@{lat},{long},15.1z",
            "start": start_index,
        }
        search = GoogleSearch(params)
        result = search.get_dict()
        local_results = result.get("local_results", [])
        results.extend(local_results)

        # Check if there are more pages
        if len(local_results) < results_per_page:
            break
    # saving data in csv
    with open("maps-results.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        # membuat header pada data csv
        csv_writer.writerow(
            [
                "title",
                "place_id",
                "gps_coordinates",
                "rating",
                "reviews",
                "type",
                "address",
                "operating_hours",
                "phone",
                "website",
                "description",
                "service_options",
            ]
        )
        for place in results:
            csv_writer.writerow(
                [
                    place.get("title"),
                    place.get("place_id"),
                    place.get("gps_coordinates", {}).get("latitude"),
                    place.get("gps_coordinates", {}).get("longitude"),
                    place.get("rating"),
                    place.get("reviews"),
                    place.get("type"),
                    place.get("address"),
                    place.get("operating_hours"),
                    place.get("phone"),
                    place.get("website"),
                    place.get("description"),
                    place.get("service_options", {}).get("dine_in"),
                    place.get("service_options", {}).get("takeout"),
                    place.get("service_options", {}).get("no_contact_delivery"),
                ]
            )


def main():
    results = ScrapingGoogleMap(
        query="Mixue", lat=-7.275612, long=112.6302807, num_pages=5, results_per_page=20
    )
    print(results)


if __name__ == "__main__":
    main()
