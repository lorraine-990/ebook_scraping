# ebook_scraping

This project scrapes **Chinese-language eBooks** from [Project Gutenberg](https://www.gutenberg.org/).  
A total of **362 books** were successfully collected.

## Concept and Step
1. **Scrape book titles and links**  
   Use `requests` and `BeautifulSoup` to get all book titles and links from the [Chinese-language listing page](https://www.gutenberg.org/browse/languages/zh).

2. **Filter only Chinese titles and book IDs**  
   Use `regex` to keep only the titles that are fully in Chinese, and find each book’s ID.

3. **Make a folder**  
   Create a local directory to store all downloaded book files.

4. **Download eBook text files**  
   Use a `for` loop to go through each book ID, fetch its `.txt` file, and save it into local files.

5. **Verify file content**  
   Randomly open three downloaded files to check if they are truly in Chinese.

## Environment

Developed using **Python 3.13.3**

| Package         | Version   |
|-----------------|-----------|
| beautifulsoup4  | 4.13.4    |
| lxml            | 5.4.0     |
| regex           | 2024.11.6 |
| requests        | 2.32.3    |


## Demo

Check out the demo on YouTube:  
👉 [Gutenberg_eBook_Scraping_AIPE01](https://www.youtube.com/watch?v=HNtYq-gViOQ)

