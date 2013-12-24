from bs4 import BeautifulSoup
from urllib2 import urlopen


BASE_URL = "http://162.144.5.233/~ritzb/gold_eagle/product-category/buy-palladium/"


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

product_links = []

soup = make_soup(BASE_URL)
product_links_currpage = [li.a["href"] for li in soup.findAll("li", {"class": "product_item"})]
print "\n".join(x for x in product_links_currpage)
print "----" + str(len(product_links_currpage)) + "--------"
for item in product_links_currpage:
    product_links.append(item)

# for i in xrange(2, 64):
#     soup = make_soup(BASE_URL + "/page/" + str(i) + "/")
#     product_links_currpage = [li.a["href"] for li in soup.findAll("li", {"class": "product_item"})]
#     print "\n".join(x for x in product_links_currpage)
#     print "----" + str(len(product_links_currpage)) + "--------" + str(i)
#     for item in product_links_currpage:
#         product_links.append(item)

print len(product_links)

f = open('Palladium\palladium_prod_links', 'w')
for item in product_links:
    print>>f, item
f.close()