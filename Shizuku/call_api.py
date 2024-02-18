from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
from typing import Optional, Union
from pathlib import Path
import pandas as pd


def scraping_google_map(
    query: str,
    api_key: Optional[str] = None,
    lat: Optional[float] = None,
    long: Optional[float] = None,
    num_pages: int = 1,
    results_per_page: int = 10,
    saving_option: Optional[bool] = True,
) -> Union[None, pd.DataFrame]:
    """
    Perform Google Maps scraping based on the given parameters.

    Args:
        query (str): The search query.
        api_key (str, optional): Google API key. If not provided, it will be loaded from environment.
        lat (float, optional): Latitude.
        long (float, optional): Longitude.
        num_pages (int): Number of pages to scrape.
        results_per_page (int): Results per page.
        saving_option (bool): Whether to save the results to a CSV file.

    Returns:
        Union[None, pd.DataFrame]: DataFrame containing the results or None if saving_option is True.
    """
    if api_key is None:
        dotenv_path = Path("Shizuku/secret_key/.env")
        load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("SERPAPI_KEY")

    # Check if lat and long are provided
    if lat is None or long is None:
        raise ValueError("Please provide both latitude and longitude.")

    # Check if the number of pages is valid
    if num_pages <= 0:
        raise ValueError("Number of pages should be greater than 0.")

    # Check data types for lat and long
    if not isinstance(lat, (int, float)) or not isinstance(long, (int, float)):
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
    df = pd.DataFrame(
        results,
        columns=[
            "position",
            "title",
            "place_id",
            "reviews_link",
            "photos_link",
            "gps_coordinates",
            "place_id_search",
            "provider_id",
            "rating",
            "reviews",
            "price",
            "type",
            "types",
            "address",
            "open_state",
            "hours",
            "operating_hours",
            "phone",
            "website",
            "description",
            "service_options",
            "order_online",
            "thumbnail",
        ],
    )
    if saving_option:
        df.to_csv("maps-results.csv", index=False)
    else:
        return df


def scraping_google_map_review(
    place_ids: Union[pd.DataFrame, list],
    api_key: Optional[str] = None,
    save_option: Optional[bool] = True,
) -> Union[None, pd.DataFrame]:
    """
    Perform Google Maps reviews scraping based on the given place IDs.

    Args:
        place_ids (Union[pd.DataFrame, list]): DataFrame or list of place IDs.
        api_key (str, optional): Google API key. If not provided, it will be loaded from environment.
        save_option (bool): Whether to save the results to a CSV file.

    Returns:
        Union[None, pd.DataFrame]: DataFrame containing the reviews or None if save_option is True.
    """
    if api_key is None:
        dotenv_path = Path("Shizuku/secret_key/.env")
        load_dotenv(dotenv_path=dotenv_path)
        api_key = os.environ.get("SERPAPI_KEY")

    reviews_data = []

    for place_id in place_ids:
        params = {"engine": "google_maps_reviews", "place_id": place_id, "api_key": api_key}
        search = GoogleSearch(params)
        results = search.get_dict()
        place_reviews = results.get("reviews", [])
        reviews_data.extend(place_reviews)

    df = pd.DataFrame(reviews_data)

    if save_option:
        df.to_csv("reviews-maps.csv", index=False)
    else:
        return df


def main():
    results = scraping_google_map(
        query="Mixue",
        lat=-7.275612,
        long=112.6302807,
        num_pages=5,
        results_per_page=20,
    )
    result_id = scraping_google_map_review(results["place_id"], save_option=True)


if __name__ == "__main__":
    main()
