import os
import csv
from src.scraper import get_sectors, get_companies_in_sector

def main():
    # Define paths
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    sectors_csv_path = os.path.join(data_dir, 'sectors.csv')
    telecom_companies_csv_path = os.path.join(data_dir, 'telecom_companies.csv')

    # Example usage of get_sectors
    # sectors = get_sectors("https://trendlyne.com/")
    # if isinstance(sectors, str):
    #     print(f"Error getting sectors: {sectors}")
    # else:
    #     print("Sectors found:")
    #     for sector in sectors:
    #         print(f"- {sector['name']} ({sector['url']})")
    #     with open(sectors_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    #         fieldnames = ['name', 'url']
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         writer.writeheader()
    #         writer.writerows(sectors)
    #     print(f"Sector data saved to {sectors_csv_path}")

    # Example usage of get_companies_in_sector (Telecom Services)
    telecom_sector_url = "https://trendlyne.com/equity/sector/10/telecom-services/"
    # Disabling SSL verification for demonstration/troubleshooting. Not recommended for production.
    companies = get_companies_in_sector(telecom_sector_url, verify_ssl=False)

    if isinstance(companies, str):
        print(f"Error getting companies: {companies}")
    else:
        if companies:
            print("Companies found in Telecom Services sector:")
            for company in companies:
                print(f"- {company['name']} ({company['url']})")

            with open(telecom_companies_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['name', 'url']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(companies)
            print(f"\nCompany data saved to {telecom_companies_csv_path}")
        else:
            print("No companies found in the Telecom Services sector.")

if __name__ == "__main__":
    main()
