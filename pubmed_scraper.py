import xml.etree.cElementTree as ET
import requests
import re
import time

usage_data = {
                'email': 'email@gmail.com',
                'tool': 'paper_scrape'
             }
pmcids = []
url_base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id='
url_id = '3184399'

# To cycle through a bunch of papers stored in pmcids.txt
with open('pmcids.txt') as f:
    for line in f:
        pmcids.append(line)

for pmcid in pmcids[1:]:
    pass

# Request the page and generate an XML element
page = requests.get(url_base + url_id, headers=usage_data)
root = ET.fromstring(page.text)

# Text processing

# Grab the body element
body = root.findall('./article/body')[0]

# And grab its constituent text
body_text = ''.join(body.itertext()).lower()

# Only care about alphas
body_text = re.split('[^a-zA-Z]', body_text)

# Strip newlines; get rid of any blank elements left over by the previous step, and filter words smaller than
# 2 characters (temporary, naive way to get rid of useless words)
body_text = [t.strip() for t in body_text if t != '' and t != '\n' and len(t) > 2]
print (body_text)

# Let's grab some figures
figures = []
for fig in root.iter('fig'):
    figures.append(fig)

print (total)
print (len(figures)) 
