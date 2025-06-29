# trendlyneScrapper2

A robust web scraper for Trendlyne.com, designed to extract sector and company-specific data.

## Project Structure

- `main.py`: The main entry point for running the scraper.
- `src/`: Contains the core scraping logic.
  - `scraper.py`: Functions for fetching sector and company data.
- `data/`: Stores input CSVs (e.g., `sectors.csv`) and generated output CSVs (e.g., `telecom_companies.csv`).
- `requirements.txt`: Lists the Python dependencies.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/trendlyneScrapper2.git
    cd trendlyneScrapper2
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    -   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the scraper and extract company data for a specific sector, provide the Trendlyne sector URL as a command-line argument:

```bash
python main.py <sector_url>
```

**Example:**

```bash
python main.py https://trendlyne.com/equity/sector/10/telecom-services/
```

This will generate a CSV file (e.g., `telecom-services_companies.csv`) in the `data/` directory containing the scraped company information.

## Important Notes

-   **SSL Verification:** The scraper currently disables SSL verification (`verify=False`) for requests. This is generally **not recommended for production environments** due to security risks. It's used here for demonstration purposes or in cases where SSL certificate issues prevent data access. Consider enabling SSL verification if possible.