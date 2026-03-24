from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'http://books.toscrape.com'

response = requests.get(URL)
text_response = response.content
# print(text_response)
soup = BeautifulSoup(text_response, 'html.parser')

book_products = soup.find_all("article", class_ = 'product_pod')
# print(book_products)
data_books = []
for i_book in book_products:
    # print(i_book)
    # name
    name = i_book.h3.a["title"]
    print(name)

    # price
    price = i_book.find("p", class_ = "price_color").text
    print(price)

    # star rating
    star_rating = i_book.find("p", class_ = "star-rating")['class'][1]
    print(star_rating)

    # in stock
    instock_availability = str(i_book.find("p", class_ = "instock availability").text).replace("\n", "").strip()
    print(instock_availability)
    print("____________________________________________________________--")

    data_dict = {
        "title": name,
        "price": price,
        "star_rating": star_rating,
        "instock_availability": instock_availability
    }
    data_books.append(data_dict)

print(data_books)
print("____________________________________________________________--")

df_input = pd.DataFrame(data=data_books)
print(df_input)

# lấy dữ liệu trong 5 trang