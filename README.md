# Amazon Price Tracker

A Python script that scrapes the price of any Amazon product and logs it to a CSV file with a timestamp — great for tracking price changes over time.

---

## Features

- Scrapes product name and price from any Amazon product page
- Appends data to a CSV file on every run (does not overwrite)
- Timestamps each entry so you can track price history
- CSV file is saved in the same directory as the script

---

## Requirements

- Python 3.6+
- Install dependencies:

```bash
pip install requests beautifulsoup4 lxml
```

---

## Usage

Run the script from your terminal:

```bash
python tracker.py
```

Each run appends a new row to `product.csv`:

```
product, price, timestamp
Redragon K673 Mechanical Keyboard..., 2999, 2024-06-01 10:30:00
Redragon K673 Mechanical Keyboard..., 2799, 2024-06-02 09:15:00
```

---

## Track Your Own Product

You can use this script to track the price of **any Amazon product** by swapping out the URL:

1. Go to the Amazon product page you want to track
2. Copy the URL from your browser
3. Open `tracker.py` and find this line:

```python
source = requests.get('https://www.amazon.in/...').text
```

4. Replace the URL inside `requests.get(...)` with your copied URL:

```python
source = requests.get('YOUR_AMAZON_PRODUCT_URL_HERE').text
```

5. Save and run the script — it will now track that product's price

> **Tip:** To track prices over time, schedule the script to run automatically using **Task Scheduler** (Windows) or **cron** (Mac/Linux). Running it once a day builds a full price history in your CSV.

### Example cron job (runs daily at 9am):
```bash
0 9 * * * /usr/bin/python3 /path/to/tracker.py
```

---

## Output

Data is saved to `product.csv` in the same folder as the script.

| Column | Description |
|--------|-------------|
| `product` | Full product name scraped from the page |
| `price` | Price as a number (currency symbol removed) |
| `timestamp` | Date and time the data was recorded |

---

## Limitations

- Only works on **Amazon product pages** (the script targets Amazon's specific HTML structure)
- Amazon may block repeated requests — if scraping fails, try adding a `User-Agent` header to the request:

```python
headers = {'User-Agent': 'Mozilla/5.0'}
source = requests.get('YOUR_URL', headers=headers).text
```

- Prices shown may vary based on your region or login status

---

## Project Structure

```
tracker.py        # Main script
product.csv       # Auto-generated price history file
README.md         # This file
```
