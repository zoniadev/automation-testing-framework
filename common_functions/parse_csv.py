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
        Reads the single-column CSV file and stores the URLs in the Behave context.
        """
    try:
        with open(csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            # Extract URLs into a clean list, ignoring empty lines
            extracted_urls = [row[0].strip() for row in reader if row and row[0].strip()]
        print(f"Successfully loaded {len(extracted_urls)} URLs from {csv_file_path}.")
        return extracted_urls
    except FileNotFoundError:
        assert False, f"The data file source was not found at: {csv_file_path}"
