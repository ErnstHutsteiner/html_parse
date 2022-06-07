
from bs4 import BeautifulSoup
import pandas as pd

data_frame = pd.DataFrame()

with open("sample.html", "r") as this_file:
    work_doc = BeautifulSoup(this_file, "html.parser")

def parse_a(a_text):
    raw_string = a_text.strip('<a, </a>, href=, > ')
    ref_list = raw_string.split('>')
    loc_name = ref_list[1]
    link_part = ref_list[0].split()
    return link_part[0], loc_name.strip()


def parse_address(p_tag, kind):
    span_tag = p_tag.find_all('span', itemprop=kind)
    raw_string = str(span_tag[0])
    # prep_string = raw_string.strip('<span,</span>')
    prep_string = raw_string.replace('<span itemprop="'+kind +'"', '')
    prep_string = prep_string.replace('</span>', '')
    prep_string = prep_string.replace('>', '')
    return prep_string 

my_tags = work_doc.find_all('div', class_='card search-result')

for tag in my_tags:
    my_dictionary = dict()
    a_tag = tag.find_all("a")
    p_tag = tag.find_all("p", class_= 'text-muted mb-2')
    link_part, loc_name = parse_a(str(a_tag[0]))
    street = parse_address(p_tag[0], 'streetAddress') 
    zip =  parse_address(p_tag[0], 'postalCode')
    city = parse_address(p_tag[0], 'addressLocality')
    # print(link_part)
    # print(loc_name)
    # print(street)
    # print(zip)
    # print(city)

    my_dictionary = {
        "Name" : loc_name,
        "Street" : street,
        "Zip" : zip,
        "City" : city,
        "URL" : link_part
    }
    # print(data_frame2)

    data_frame = data_frame.append(my_dictionary, ignore_index=True)

# print(data_frame)
data_frame.to_csv('result.csv')



