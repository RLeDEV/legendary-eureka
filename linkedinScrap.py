import urllib.request
import re
from bs4 import BeautifulSoup

def scrap(jobsURL):
    try:
        page = urllib.request.urlopen(jobsURL)
        soup = BeautifulSoup(page, 'html.parser')
        if soup is not None:
            return soup
        else:
            return None
    except:
        print('Error while scraping information from LinkedIn')

def getJobs(soup):
    if soup is not None:
        jobTitleRegex = re.compile('^result-card__full-card-link')
        jobsList = soup.find_all('a', attrs={'class': jobTitleRegex})
        companyTitleRegex = re.compile('COMPANY-*')
        companysList = soup.find_all('label', attrs={'for': companyTitleRegex})
        linksList = []
        for link in jobsList:
            linksList.append(link.get('href'))
        finalList = []
        for job,company,link in zip(jobsList,companysList,linksList):
            finalList.append('Job Title: ' + str(job.getText()) + ',Comapny: ' + str(company.getText()) + ', Link:' + link)
        return finalList
    else:
        return None

def printJobs(finalList):
    if finalList is not None:
        for job in finalList:
            print(job)
        print('DONE!')
    else:
        return None
