import os
import requests
from dotenv import load_dotenv, dotenv_values
from lxml import html

sections_names = [
    'reference', 
    'properties', 
    'at-rules_and_descriptors', 
    'functions',
    'data_types_and_values', 
    'html_attributes', 
    'interfaces', 
    'related_concepts'
]

h2_sections_names = [
    'reference',
    'related_concepts'
]

main_page_content = 'article[@class="main-page-content"]'

load_dotenv()

rt = requests.get("https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_anchor_positioning", headers={os.getenv("HEADERS_PROPERTY"): os.getenv("HEADERS_VALUE")})
tree = html.fromstring(rt.content)

# при отсутствии элемента на разметке после tree.xpath будет выходить []
main_sections = []
for i in sections_names:
    head_elem = ""
    if i in h2_sections_names:
        head_elem = "h2"
    else:
        head_elem = "h3"
    main_sections.append("".join(tree.xpath(f'//{main_page_content}/section[@aria-labelledby="{i}"]/{head_elem}/a/text()')))

print("Выберите раздел статьи: ", main_sections)

# print(tree.xpath(f'//{main_page_content}/section/h2/a/text()'))
# print(tree.xpath(f'//{main_page_content}/section/h3/a/text()'))


# with open("css_author_positioning.txt", "wb") as html_file:
#     html_file.write(rt.content)

# tree = html.fromstring()