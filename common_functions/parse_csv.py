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
    Reads the CSV file and returns a list of dictionaries.
    Handles both 1-column (Signup) and 2-column (Opt-in) structures.
    """
    try:
        with open(csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            extracted_urls = []
            for row in reader:
                if not row or not row[0].strip():
                    continue
                # If it's an Opt-in style CSV (2+ columns)
                if len(row) >= 2:
                    extracted_urls.append({
                        "url": row[0].strip(),
                        "disclaimer": row[1].strip()
                    })
                # If it's a Signup style CSV (1 column)
                else:
                    extracted_urls.append({
                        "url": row[0].strip()
                    })
        print(f"Successfully loaded {len(extracted_urls)} test entries from {csv_file_path}.")
        return extracted_urls
    except FileNotFoundError:
        assert False, f"The data file source was not found at: {csv_file_path}"
