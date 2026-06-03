import csv


def parse_banner_mapping():
    mapping = {}
    with open("data/banner_redirects.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row or len(row) != 2:
                continue
            identifier, url = row
            mapping[identifier.strip()] = url.strip()
    return mapping


def read_urls(csv_file_path):
    """
    Reads the two-column CSV file and returns a list of dictionaries
    containing URLs and their corresponding expected disclaimers.
    """
    try:
        with open(csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            # Extract URL and disclaimer, ensuring the row contains both elements
            extracted_urls = [
                {"url": row[0].strip(), "disclaimer": row[1].strip()}
                for row in reader if row and len(row) >= 2 and row[0].strip()
            ]
        print(f"Successfully loaded {len(extracted_urls)} test entries from {csv_file_path}.")
        return extracted_urls
    except FileNotFoundError:
        assert False, f"The data file source was not found at: {csv_file_path}"
