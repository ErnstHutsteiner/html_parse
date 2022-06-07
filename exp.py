a_text = '<a href="https://www.speisekarte.de/m%C3%BCnchen/restaurant/frau_li" onclick="">    Frau Li'
raw_string = a_text.strip('<a, </a>, href=, > ')
ref_list = raw_string.split('>')
loc_name = ref_list[1]
link_part = ref_list[0].split()
print(loc_name.strip())
print(link_part[0])