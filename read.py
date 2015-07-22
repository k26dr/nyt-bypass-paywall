#!/usr/bin/env python3

import sys

def get_article_text(url):
    import requests
    from bs4 import BeautifulSoup

    # remove parameters from url
    if '?' in url:
        url = url[0:url.find('?')]

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')
    paras = [p.text for p in soup.find_all('p', {'class': 'story-body-text'})]
    
    # replace common unicode characters and ignore the rest
    trans = { '\u2014': '--', '\u201d': '"', '\u201c': '"', '\u2019': "'"}
    for find,replace in trans.items():
        paras = [p.replace(find,replace) for p in paras]
    paras = [p.encode('ascii', 'ignore').decode('ascii') for p in paras]
    return '\n\n'.join(paras)
    

def help():
    return """
        Usage: python3 read.py \"<url>\"
        Example: python3 read.py \"http://www.nytimes.com/2015/07/22/books/el-doctorow-author-of-historical-fiction-dies-at-84.html\"
        """

if __name__ == '__main__':
    if sys.argv[1] in ['--help', '-h']:
        print(help())
    else:
        print(get_article_text(sys.argv[1]))
