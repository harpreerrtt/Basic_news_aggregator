import requests # used for api .get request to server
from bs4 import BeautifulSoup  # work with html,xml for good output

def main():

    #website link
    url = "https://news.ycombinator.com"
    #sending get request and capturing response
    response = requests.get(url)

    if response.status_code == 200:
        #response has different methods like status_code, text
        # this can be check using comand print(dir(__classname__)) or print(type(__classname__))
        page_content  = response.text
        #this just beautify the content like add \n between tags
        soup = BeautifulSoup(page_content,"html.parser")
        # print(soup.prettify())

        articles = soup.find_all("tr", class_="athing")

        for article in articles:
            titleline = article.find("span", class_="titleline")
            url  = titleline.find("a")['href']
            title = titleline.text

            print(f"{title}\n{url}\n")

    else:
        print(f"Failed to fetch detail from {url}")


if __name__ == "__main__" :
    main()

