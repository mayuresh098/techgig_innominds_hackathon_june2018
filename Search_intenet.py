################################# stackoverflow_code
SCHEME = 'http://'
VERIFY_SSL_CERTIFICATE = False
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import argparse
import glob
import os
import datetime
import json
import random
import re
import requests
from collections import OrderedDict
#import requests_cache
import sys
#from . import __version__
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#from pygments import highlight
#from pygments.lexers import guess_lexer, get_lexer_by_name
#from pygments.formatters.terminal import TerminalFormatter
#from pygments.util import ClassNotFound
from pyquery import PyQuery as pq
#from requests.exceptions import ConnectionError
#from requests.exceptions import SSLError
#from urllib.request import getproxies

import requests

#from helloworld import settings


def index(request):
    return HttpResponse(" Django 2")


### in opytohn 2 only
def u(x):
    return x

def _extract_links(html, search_engine):
    if search_engine == 'bing':
        return _extract_links_from_bing(html)
    return _extract_links_from_google(html)

def get_proxies():
    proxies = getproxies()
    filtered_proxies = {}
    for key, value in proxies.items():
        if key.startswith('http'):
            if not value.startswith('http'):
                filtered_proxies[key] = 'http://%s' % value
            else:
                filtered_proxies[key] = value
    return filtered_proxies


USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
                'Chrome/19.0.1084.46 Safari/536.5'),
               ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
                'Safari/536.5'), )

SEARCH_URLS = {
    'bing': SCHEME + 'www.bing.com/search?q=site:{0}%20{1}',
    'google': SCHEME + 'www.google.com/search?q=site:{0}%20{1}'
}


STAR_HEADER =""# u('\u2605')
ANSWER_HEADER = u('{2}  Answer from {0} {2}\n{1}')
NO_ANSWER_MSG = '< no answer given >'
XDG_CACHE_DIR = os.environ.get('XDG_CACHE_HOME',
                               os.path.join(os.path.expanduser('~'), '.cache'))
CACHE_DIR = os.path.join(XDG_CACHE_DIR, 'web')
CACHE_FILE = os.path.join(CACHE_DIR, 'cache{0}'.format(
    sys.version_info[0] if sys.version_info[0] == 3 else ''))
SCHEME = 'http://'
VERIFY_SSL_CERTIFICATE = False
session = requests.session()
##############################################################################################3

import re
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

def sortFreqDict(freqdict):
    '''
    does not need it anyway
    '''
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


def return_count(str1):
    str1= stripNonAlphaNum(str1)
    str1=removeStopwords(str1,stopwords)
    str1= wordListToFreqDict(str1)
    str1=sortFreqDict(str1)
    return str1
###############################################################################################
def _get_result(url):
    try:
        return session.get(url, headers={'User-Agent': random.choice(USER_AGENTS)}, 
                                  verify=VERIFY_SSL_CERTIFICATE).text
    except Exception as e:
        #print('[ERROR] Encountered an SSL Error. Try using HTTP instead of ''HTTPS by setting the environment variable "web_DISABLE_SSL".\n',e
        raise e

def web(args):
    args['query'] = ' '.join(args['query']).replace('?', '')
    try:
        return _get_instructions(args) or 'Sorry, I am not able to find anything \n'
    except (ConnectionError, SSLError):
        return 'Failed to establish network connection\n'

def _is_question(link):
    return re.search('questions/\d+/', link)




def _get_links(query):
    search_engine = os.getenv('web_SEARCH_ENGINE', 'google')
    search_url = _get_search_url(search_engine)

    result = _get_result(search_url.format(URL, url_quote(query)))
    html = pq(result)
    return _extract_links(html, search_engine)

def _get_instructions(args):
    links = _get_links(args['query'])
    if not links:
        return False

def _get_search_url(search_engine):
    return SEARCH_URLS.get(search_engine, SEARCH_URLS['google'])


def _get_links(query):
    search_engine = os.getenv('web_SEARCH_ENGINE', 'google')
    search_url = _get_search_url(search_engine)

    result = _get_result(search_url.format(URL, (query)))
    html = pq(result)
    return _extract_links(html, search_engine)

def _extract_links_from_bing(html):
    html.remove_namespaces()
    return [a.attrib['href'] for a in html('.b_algo')('h2')('a')]


def _extract_links_from_google(html):
    return [a.attrib['href'] for a in html('.l')] or \
        [a.attrib['href'] for a in html('.r')('a')]

def _get_questions(links):
    return [link for link in links if _is_question(link)]

def _get_text(element):
    ''' return inner text in pyquery element '''
    return element.text(squash_space=False)


def get_link_at_pos(links, position):
    if not links:
        return False

    if len(links) >= position:
        link = links[position - 1]
    else:
        link = links[-1]
    return link



def answers(query):
    URL = os.getenv('web_URL') or  'serverfault.com' #'stackoverflow.com'

    search_engine = os.getenv('web_SEARCH_ENGINE', 'google')
    search_url = _get_search_url(search_engine)

    result = _get_result(search_url.format(URL, (query)))
    html = pq(result)
    #print html

    #print "##################################################"

    links=  _extract_links(html, search_engine)

    if not links:
        return "nothing found"

    question_links = _get_questions(links)
    #print question_links
    if not question_links:
        return "no questions found"



    link = get_link_at_pos(links, 1)
    if not link:
        return "no link found"

    page = _get_result(link + '?answertab=votes')
    html = pq(page)

    first_answer = html('.answer').eq(0)

    #print first_answer

    instructions = first_answer.find('pre') or first_answer.find('code')

    if not instructions:
            text = _get_text(first_answer.find('.post-text').eq(0))

    return instructions.text()


##
#How to filter http traffic in Wireshark?
#How to determine JAVA_HOME on Debian/Ubuntu?
#
##return_Res=answers("How to filter http traffic in Wireshark?")
##print return_Res





##
##
##
##
##def query(request):
##    
##    if 'q' in request.GET:
##        query=request.GET['q']
##        query.lower()
##        ans=answers(query)
##        ans=str(ans)
##        ans="<br />".join(ans.split("\n"))
##        message = ans
##    else:
##        message = 'You submitted an empty query'
##    return HttpResponse(message)
##
#####################################new features
##
##def stats(request):
##       
##    return render(request, 'stats.html')
##    #return HttpResponse(content)
##
##def res_ret(request):
##    # This is the url to which the query is made
##    url = "https://data.stertorous51.hasura-app.io/v1/query"
##
##    # This is the json payload for the query
##    re
##    }
##    }
##
##    # Setting headers
##    headers = {
##        "Content-Type": "application/json",
##        "Authorization": "",<<<<<<<<<---------youir auth here
##        "X-Hasura-Role": "admin"
##    }
##
##    # Make the query and store response in resp
##    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
##
##    # resp.content contains the json response.
##    #content= resp.content# not working
##    content=resp.json()
##    ##########sorting the date data
##    my_dict=dict()
##        
##
##    for x in content:
##        key= x['date']
##        if key in my_dict:
##            my_dict[key] += 1
##        else:
##            my_dict[key] = 1
##    print my_dict
##    my_dict = OrderedDict(sorted(my_dict.items(), key=lambda t: t[0]))
##    print my_dict
##    #my_dict.items()
##
##    return HttpResponse(json.dumps(my_dict.items()), content_type="application/json") 
##
##
##def res_ret2(request):
##    # This is the url to which the query is made
##    url = "https://data.stertorous51.hasura-app.io/v1/query"
##
##    # This is the json payload for the query
##    requestPayload = {
##       "type": "select",
##    "args": {
##        "table": "quer",
##        "columns": [ 
##            "quer1"
##        ]
##       
##    }
##    }
##
##    # Setting headers
##    headers = {
##        "Content-Type": "application/json",
##        "Authorization": "",<<<<<<<<<---------youir auth here
##        "X-Hasura-Role": "admin"
##    }
##
##    # Make the query and store response in resp
##    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
##
##    # resp.content contains the json response.
##    #content= resp.content# not working
##    content=resp.json()
##    ##########sorting the date data
##    all_words=""
##    for x in content:
##        quer_s= str(x['quer1'])
##        #quer_s.decode('utf8')
##        print type(quer_s)
##        all_words=all_words+" "+(quer_s)
##        
##        
##        #all_words=+str(quer_s)
##    freq_count= return_count(all_words)
##    #freq_count=10
##
##    #print content
##    #my_dict.items()
##
##    return HttpResponse(json.dumps(freq_count), content_type="application/json") 
##    
##
