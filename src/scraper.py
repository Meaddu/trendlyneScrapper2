import requests
from bs4 import BeautifulSoup
import json
import sys

def get_sectors(url, verify_ssl=True):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, verify=verify_ssl)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"

    api_url = "https://trendlyne.com/react/v1/getnonauthstockgroup/"
    try:
        api_response = requests.get(api_url, headers=headers, verify=verify_ssl)
        api_response.raise_for_status()
        data = api_response.json()
        if 'body' in data and 'data' in data['body']:
            for category in data['body']['data']:
                if category.get('label') == 'Sectors':
                    sectors = []
                    for sector_info in category.get('options', []):
                        sector_name = sector_info.get('optiontext')
                        if sector_name and sector_name not in ["Coal", "Third party funds"]:
                            sectors.append({'name': sector_name, 'url': sector_info.get('value')})
                    return sectors
        else:
            return "'body' or 'data' key not found in API response."
    except requests.exceptions.RequestException as e:
        return f"Error fetching API data: {e}"
    except ValueError as e:
        return f"Error decoding JSON from API response: {e}. Response content: {api_response.text}"

    return "No sectors found from API data."

def get_companies_in_sector(sector_url, verify_ssl=True):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        response = requests.get(sector_url, headers=headers, verify=verify_ssl)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        companies = []
        treemap_div = soup.find('div', class_='highcharts-treemap-node')

        if treemap_div and 'data-treemapdict' in treemap_div.attrs:
            try:
                treemap_data_str = treemap_div['data-treemapdict']
                treemap_data = json.loads(treemap_data_str)
                if 'chart' in treemap_data:
                    for item in treemap_data['chart']:
                        if 'tooltip_stock_name' in item and 'cell_url' in item:
                            company_name = item['tooltip_stock_name']
                            company_url = item['cell_url']
                            companies.append({'name': company_name, 'url': company_url})
            except json.JSONDecodeError as e:
                return f"Error decoding JSON from data-treemapdict: {e}"
        else:
            return "Could not find the highcharts-treemap-node div or data-treemapdict attribute."

        return companies
    except requests.exceptions.RequestException as e:
        return f"Error fetching sector page: {e}"
