import math
from scrapingbee.scrapingbee_client import ScrapingbeeClient
from bs4 import BeautifulSoup
import pandas as pd
import datetime

l = []
k = []
current_time = datetime.datetime.now()


def sub_string_parser(s):
    final_date = ""
    if ("second" or "seconds" or "minute" or "minutes" or "hour" or "hours") in s:
        final_date = current_time.strftime("%b") + "-" + current_time.strftime("%Y")
    elif ("day" or "days") in s:
        temp = int(s[0])
        d = datetime.timedelta(days=temp)
        day = current_time - d
        final_date = day.strftime("%b") + "-" + day.strftime("%Y")
    elif ("week" or "weeks") in s:
        temp = int(s[0])
        d = datetime.timedelta(days=7 * temp)
        week = current_time - d
        final_date = week.strftime("%b") + "-" + week.strftime("%Y")
    elif ("month" or "months") in s:
        if s[1] != " ":
            temp = int(s[0] + s[1])
        else:
            temp = int(s[0])
        if temp in (1, 3, 5, 7, 8, 10, 12):
            days = 31
        elif temp == 2:
            days = 28
        else:
            days = 30
        d = datetime.timedelta(days=days * temp)
        month = current_time - d
        final_date = month.strftime("%b") + "-" + month.strftime("%Y")
    elif ("year" or "years") in s:
        if s[1] != " ":
            temp = int(s[0] + s[1])
        else:
            temp = int(s[0])
        d = datetime.timedelta(days=365 * temp)
        year = current_time - d
        final_date = year.strftime("%b") + "-" + year.strftime("%Y")
    return final_date


client = ScrapingbeeClient(
    api_key='DPRV25AFHLBID0SLZYOIYI6RAAGZT2H4B3FJ92E5P5XD4NH0D66YXZBZTNZPJT36T6VBHK1S8684G52V'
)

html_api_controller = client.html_api
url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=quality%20assurance&location=Pakistan&geoId=101022442&currentJobId=3732848394&start={}'

render_js = False

json_response = False
i = 0
while i < 125:
    result = html_api_controller.json_response(
        url.format(i),
        render_js,
        json_response
    )
    soup = BeautifulSoup(result, 'html.parser')
    all_jobs_on_this_page = soup.find_all("li")
    print(len(all_jobs_on_this_page))
    for x in range(0, len(all_jobs_on_this_page)):
        if all_jobs_on_this_page[x].find("div", {"class": "base-card"}) is not None:
            jobid = all_jobs_on_this_page[x].find("div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
            l.append(jobid)
    i += 25
target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
for j in range(0, 100):
    o = {}
    # print(l[j])
    target = target_url.format(l[j])
    # print(target)
    resp = html_api_controller.json_response(
        target,
        render_js,
        json_response
    )
    # print(resp)
    soup = BeautifulSoup(resp, 'html.parser')

    try:
        o["company"] = soup.find("div", {"class": "topcard__flavor-row"}).find("a", {
            "class": "topcard__org-name-link"}).text.strip()
    except:
        o["company"] = ""

    try:
        o["job_title"] = soup.find("div", {"class": "top-card-layout__entity-info"}).find("a").text.strip()
    except:
        o["job_title"] = ""

    try:
        raw_date = soup.find("span", {"class": "posted-time-ago__text"}).text.strip()
        date = sub_string_parser(raw_date)
        o["posted_date"] = date
    except:
        o["posted_date"] = ""

    try:
        o["level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find("li").text.replace(
            "Seniority level", "").strip()
    except:
        o["level"] = ""
    try:
        raw_location = soup.find("div", {"class": "topcard__flavor-row"}).find("span", {
            "class": "topcard__flavor topcard__flavor--bullet"}).text.replace(", Pakistan", "").strip()
        location_split = raw_location.split(", ", 2)
        if len(location_split) == 1 or len(location_split) == 0:
            o["city"] = "Remote"
            o["province"] = "Remote"
        else:
            o["city"] = location_split[0]
            o["province"] = location_split[1]
    except:
        o["city"] = ""
        o["province"] = ""
    try:
        o["description"] = soup.find("div", {"class": "show-more-less-html__markup"}).text.strip()
    except:
        o["description"] = ""

    k.append(o)


df = pd.DataFrame(k)
df.to_csv('jobs_QualityAssurance.csv', index=False, encoding='utf-8')
print(k)

data = pd.read_csv("jobs_QualityAssurance.csv")
df = pd.DataFrame(data)
df.dropna(subset="posted_date", inplace=True)  # deletes nulls
df["posted_date"] = pd.to_datetime(df["posted_date"], format='%b-%Y')  # convert date from string to date
df.sort_values(by="posted_date", ascending=False, inplace=True)  # sort date
df["job_title"] = df['job_title'].str.replace('â€“', '')  # remove typos
df["city"] = df['city'].str.replace('ā', 'a')  # remove typos
df["province"] = df['province'].str.replace('ā', 'a')  # remove typos
df = df.drop_duplicates()  # remove duplicates

print(df)

df.to_csv('jobs_QualityAssurance.csv', index=False, encoding='utf-8')
