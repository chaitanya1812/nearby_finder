from osm_utils import get_nearby_places

def main():
    query = input("Enter what you're looking for (e.g., fuel stations): ")
    location = input("Enter the location (e.g., HSR Layout Bengaluru): ")
    results = get_nearby_places(query, location)
    if results:
        print("Found the following places:")
        for place in results:
            print(f"{place['name']} at {place['address']}")
    else:
        print("No places found.")

if __name__ == "__main__":
    main()
