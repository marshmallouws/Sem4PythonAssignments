# Happy County assignment
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


url = "https://www.merchbar.com"
browser = webdriver.Firefox()
browser.get(url)
browser.implicitly_wait(3)
query = "breaking benjamin"


def search(query):
    search_field = browser.find_elements_by_tag_name("input")
    for search in search_field:
        if "Search over" in search.get_attribute("placeholder"):
            break

    search.send_keys(query + Keys.RETURN)
    sleep(1)


def get_no_of_products():
    """
    1. Hvor mange produkter kommer frem, 
    når man søger på "breaking benjamin"
    (se URL'en)
    """
    try:
        no_of_products_search = browser.find_element_by_class_name("my-2.row")
    except:
        print("You need to search first")
    else:
        return no_of_products_search.text.split()[0]  # 34


def find_tracks():
    """
    2. Hvor mange TRACKs er der i det første produkt, 
    som ligger i kategorien CDs?
    """
    selects = browser.find_elements_by_class_name("ais-RefinementList-labelText")
    for s in selects:
        if "CDs" in s.text:
            break

    s.click()  # Click cds

    sleep(1)

    browser.find_element_by_class_name(
        "brand-merch-container.page-items-container.col-md-9"
    ).find_element_by_tag_name("img").click()

    sleep(1)

    return browser.find_element_by_class_name("track-list").text


search("breaking benjamin")
# get_no_of_products()

"""
"3. Vis et bar chart der viser: 
- Procentdel af de viste produkter, der rent faktisk 
   indeholder Breaking Benjamin merch
- Procentdel af den merch, der er på tilbud
- Procentdel af den merch, der ikke er på lager
"""


def get_merchandise():
    pass


# browser.close()
