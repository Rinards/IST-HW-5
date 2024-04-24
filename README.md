# IST-HW-5

Internet Search Techniques 5th Assignment prototype

## Setup

### 1. Migrate

Run

```
python manage.py makemigrations
python manage.py migrate
```

### 2. Adding data files

Add the CSV files from Kaggle to `app/data` directory

- [amazon_prime_titles.csv](https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows)
- [disney_plus_titles.csv](https://www.kaggle.com/datasets/shivamb/disney-movies-and-tv-shows)
- [netflix_titles.csv](https://www.kaggle.com/datasets/shivamb/netflix-shows)

### 3. Import data from CSVs

`python manage.py import_data`
