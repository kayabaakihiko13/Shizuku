from serpapi import GoogleSearch
import os
from dotenv import load_dotenv


def ScarapingGoogleMap(query: str, api_key: str, lat: float, long: float):
    if api_key is None:
        api_key = os.environ.get("SERPAPI_KEY")

    params = {
        "engine": "google_maps",
        "q": query,
        "api_key": api_key,
        "ll": f"@{lat},{long},15.1z",
    }
    search = GoogleSearch(params)
    result = search.get_dict()
    return result.get("local_results", [])


def main():
    try:
        # Load environment variables
        load_dotenv()
        api_key = os.environ.get("SERPAPI_KEY")

        if not api_key:
            raise ValueError("SerpApi key not found in environment variables.")

        # Set search parameters
        params = {
            "engine": "google_maps",
            "q": "Mixue",
            "api_key": api_key,
            "ll": f"@{-7.2575},{112.7521},15.1z",
        }

        # Perform the Google Maps search
        search = GoogleSearch(params)
        result = search.get_dict()

        # Print local results
        local_results = result.get("local_results", [])
        print("Local results:")
        for place in local_results:
            print(place)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
