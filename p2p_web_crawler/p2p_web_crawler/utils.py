from .db_helper import WEB_PAGES
from .formatter import Formatter


# extract links in the crawled web page
def extract_links(response):
    links = []
    try:  # in case there is not links in the response
        for sel in response.xpath("//a/@href"):
            link = ''.join(sel.extract()).strip()
            if link.startswith("http"):
                links.append(link)
    except Exception:
        pass
    return links


# def extract_content(response):
#     url = response.url
#     title = '.'.join(response.xpath("//head/title/text()").extract()).strip()
#     body = str(response.body)
#     return url, title, body


# def save_content(reponse):
#     url, title, body = extract_content(reponse)
#     save_to_database(url, title, body)
#
#
# def save_to_database(url, title, body):
#     print("saving" + url + "to database!")
#     WEB_PAGES.insert_one(Formatter.format(url, title, body))