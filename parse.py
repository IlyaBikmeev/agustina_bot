import requests
from bs4 import BeautifulSoup

#Covid 

def getData(array,number):
    return array[number][array[number].find(' ') + 1 : len(array[number])]

def getWholeData():
    result = dict()
    result['sick'] = getData(array,0)
    result['sickChange'] = getData(array,1)
    result['healed'] = getData(array,2)
    result['healedChange'] = getData(array,3)
    result['died'] = getData(array,4)
    result['diedChange'] = getData(array,5)
    return result

def removeSymbols(stats):
    
    stats = stats.replace('"','')
    stats = stats.replace('{','')
    stats = stats.replace(' ','')
    stats = stats.replace(':',' ')
    stats = stats.replace('}',' ')
    return stats

def CoronaStats():
    link = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/information/'
    r = requests.get(link).text

    soup = BeautifulSoup(r,'lxml')
    block = soup.find('small')

    date = block.get_text()

    cv_stats_virus = soup.find('cv-stats-virus')

    stats = cv_stats_virus[':stats-data']
    stats = removeSymbols(stats)

    array = stats.split(',')

    data = getWholeData()
    message = '<b>' + date + '</b>' 
    message += ':\n<i>Выявлено случаев всего:</i> ' 
    message += "<b>" + data['sick'] + "</b>" 
    message += '\n<i>Выявлено случаев за сутки: </i><b>' 
    message += data['sickChange'] + '</b>\n<i>Человек выздоровело всего: </i><b>' 
    message += data['healed'] + "</b>\n"
    message += "<i>Человек выздоровело за сутки: </i>"
    message += "<b>" + data['healedChange'] + "</b>\n"
    message += "<i>Умерло всего:</i> "
    message += "<b>" + data['died']  + "</b>\n"
    message += "<i>Умерло за сутки:</i> "
    message += "<b>" + data['diedChange']  + "</b>"

    return message