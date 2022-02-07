# Python CLI tool to Scrap weather info from Google


def query(keywords):
    import requests
    from bs4 import BeautifulSoup

    user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    google_url='https://www.google.com/search?q=%s' % keywords
    response=requests.get(google_url, headers=user_agent)
    response.raise_for_status()

    soup=BeautifulSoup(response.text, 'html.parser')
    div = soup.find(id='knowledge-currency__updatable-data-column')
    if div is not None:
        childs = list(div.children)[:2]
        output = ''
        for i in childs:
            output += ' ' + i.text.strip()
        print(output.replace('equals', '\u2248').split('·')[0].strip())
    else:
        # may be user requested a crypto exchange repeatone
        div = soup.find(id='crypto-updatable_2')
        print(list(div.div.children)[1].text.strip())

def main():
  import sys
  try:
    query('+'.join(sys.argv[1:]))
  except Exception as ex:
    print('I can not understand.')
if __name__== "__main__":
    main()
