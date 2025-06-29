import os
import csv
import argparse
from urllib.parse import urlparse
from src.scraper import get_sectors, get_companies_in_sector

def main():
    parser = argparse.ArgumentParser(description="Scrape company data from a given Trendlyne sector URL.")
    parser.add_argument("sector_url", type=str, help="The URL of the Trendlyne sector page to scrape.")
    args = parser.parse_args()

    # Define paths
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    
    # Extract sector name from URL for dynamic filename
    parsed_url = urlparse(args.sector_url)
    path_segments = parsed_url.path.strip('/').split('/')
    
    sector_name = "companies"
    if len(path_segments) >= 4 and path_segments[-3] == 'sector':
        sector_name = path_segments[-1]
    
    output_csv_filename = f"{sector_name}_companies.csv"
    output_csv_path = os.path.join(data_dir, output_csv_filename)

    # Example usage of get_sectors (commented out for now, but kept for reference)
    # sectors = get_sectors("https://trendlyne.com/")
    # if isinstance(sectors, str):
    #     print(f"Error getting sectors: {sectors}")
    # else:
    #     print("Sectors found:")
    #     for sector in sectors:
    #         print(f"- {sector['name']} ({sector['url']})")
    #     with open(os.path.join(data_dir, 'sectors.csv'), 'w', newline='', encoding='utf-8') as csvfile:
    #         fieldnames = ['name', 'url']
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         writer.writeheader()
    #         writer.writerows(sectors)
    #     print(f"Sector data saved to {os.path.join(data_dir, 'sectors.csv')}")

    # Scrape companies from the provided sector URL
    # Disabling SSL verification for demonstration/troubleshooting. Not recommended for production.
    companies = get_companies_in_sector(args.sector_url, verify_ssl=False)

    if isinstance(companies, str):
        print(f"Error getting companies: {companies}")
    else:
        if companies:
            print(f"Companies found in {sector_name} sector:")
            for company in companies:
                print(f"- {company['name']} ({company['url']})")

            with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['name', 'url']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(companies)
            print(f"\nCompany data saved to {output_csv_path}")
        else:
            print(f"No companies found in the {sector_name} sector.")

if __name__ == "__main__":
    main()
