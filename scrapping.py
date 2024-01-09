import requests
from bs4 import BeautifulSoup

URL=f"https://in.indeed.com/jobs?q=python+developer&l=India&from=searchOnHP&vjk=a7d36bf719cf3408"
r=requests.get(URL)
soup=BeautifulSoup(r.content,'html.parser')
print(soup)
divs=soup.find_all('div',class_= 'job_seen_beacon')
for item in divs:
    title=item.find('a').text
    company=item.find('span', class_="css-1x7z1ps eu4oa1w0")
    company_location=item.find('div', class_='css-t4u72d eu4oa1w0')
    salary=item.find('div',class_='css-1ihavw2 eu4oa1w0')
    description=item.find('div',class_='job-snippet')
    job_listing={
        'title':title,
        'company':company,
        'location':company_location,
        'salary':salary,
        'description':description
    }
    job.append(job_listing)

