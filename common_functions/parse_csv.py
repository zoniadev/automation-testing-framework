import csv
import os


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
    Opt-in.csv rows are "url,disclaimer". Signup.csv rows are "url,type",
    where type selects which disclaimer template applies (see SIGNUP_DISCLAIMERS
    in pages/verify_disclaimer_page.py). Single-column rows yield just "url".
    """
    is_signup_file = "signup" in os.path.basename(csv_file_path).lower()
    second_column_key = "type" if is_signup_file else "disclaimer"
    try:
        with open(csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            extracted_urls = []
            for row in reader:
                if not row or not row[0].strip():
                    continue
                if len(row) >= 2:
                    extracted_urls.append({
                        "url": row[0].strip(),
                        second_column_key: row[1].strip()
                    })
                else:
                    extracted_urls.append({
                        "url": row[0].strip()
                    })
        print(f"Successfully loaded {len(extracted_urls)} test entries from {csv_file_path}.")
        return extracted_urls
    except FileNotFoundError:
        assert False, f"The data file source was not found at: {csv_file_path}"
