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
