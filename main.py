import json
from bs4 import BeautifulSoup
import requests
""" 
OODLESBOT PYTHON 1.0

Copyright Stenoip Company 2026, All rights reserved
"""
url = [
    "https://stenoip.com",
    "https://quotes.toscrape.com",
    "https://books.toscrape.com",
    "https://scrapethissite.com",
    "https://webscraper.io",
    "https://kinsta.com/blog/crawler-list/#1-googlebot"
]

print("Search anything in Oodles")
question = input("Search:")

def crawl_and_index():
    # Define headers with a standard browser User-Agent string
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    
        
        search_results = {
            "total": 0,
            "page": 1,
            "pageSize": 10,
            "items": []
        }
    
        for i in range(len(url)):
            # Pass the headers dictionary into requests.get
            result = requests.get(url[i], headers=headers)
            doc = BeautifulSoup(result.text, "html.parser")
            
            title = doc.title
            page_text = doc.get_text()
    
            
            search_results["items"].append({
                "title": str(title),
                "url": url[i],
                "snippet": page_text.strip().replace("\n", " ")[:150] + "..."
            })
            # Increment the total count using simple addition
            search_results["total"] = search_results["total"] + 1

               
            print("Saved and crawled " + str(title) + "!")
    
        # Save the completed dictionary into index.json after the loop finishes
        with open("index.json", "w") as f:
            json.dump(search_results, f, indent=4)
            print("\nResults successfully saved to index.json!")

# I will move this function to a new file soon: crawl_and_index();

def search():
    
    with open("index.json", "r") as json_file:
        index = json.load(json_file)

    # print(index)

    
    for i in range(len(index["items"])):
        print(" ")
        page_title = index["items"][i]["title"]
    
        
        if question.lower() in page_title.lower():
            print("Found it at!")
            print(page_title)
            
           
            
        else:
            print(" ")
    
    
        




search()