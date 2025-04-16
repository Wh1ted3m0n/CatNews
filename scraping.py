from bs4 import BeautifulSoup
import requests
import fake_useragent
import config
import lxml

class ScrappNwSt:
# init ----------------------------------------------------------------------------\
    def __init__(self):
        
#name web news ---------------------------------------------------------------------\
        self._name_news= 'linux Today'
#config requst ---------------------------------------------------------------------\
        self.web1 = config.web_new1
        self.user = fake_useragent.UserAgent().random
        self.headers = {'User-Agent':self.user}
#retun scrapping---------------------------------------------------------------------\
        self.sp_name_post = []
        self.sp_datetime_post = []
        self.sp_description_post = []
        self.sp_link_post= []
#function scrapping -----------------------------------------------------------------\    
    def scrapWeb1(self):
        self.response1 = requests.get(self.web1,headers=self.headers)
        self.soup1 = BeautifulSoup(self.response1.text,'lxml')
        
        self.block = self.soup1.find_all("div",class_='td_block_inner td-mc1-wrap')

        self.div = self.block[1].find_all("div",class_='td_module_flex td_module_flex_1 td_module_wrap td-animation-stack td-cpt-user_post')
        
        for i in self.div:
            self._title = i.find('h3', class_="entry-title td-module-title")
            self.sp_name_post.append(self._title.text.strip())
        for i in self.div:
            self._time_post = i.find('time', class_="entry-date updated td-module-date")
            self.sp_datetime_post.append(self._time_post.text)
        for i in self.div:
            self._desc = i.find('div', class_="td-excerpt")
            self.sp_description_post.append(self._desc.text.strip())
        for i in self.div:
            self._tit = i.find('h3', class_="entry-title td-module-title")
            self._link = self._tit.find('a')
            self.sp_link_post.append(self._link.get('href'))
        
        return [self._name_news,self.sp_name_post,self.sp_datetime_post,self.sp_description_post, self.sp_link_post]


class ScrappHackerNews:
    def __init__(self):

        
        self._news_name = "Hacker News"
        self._web = config.web_new2
        self._user = fake_useragent.UserAgent().random
        self._headers = {'User-Agent':self._user}
        self._sp_name_post = []
        self._sp_datetime_post = []
        self._sp_description_post = []
        self._sp_link_post= []
        self.ne = []
        
    def scrapWeb2(self):
        self.response1 = requests.get(self._web,headers=self._headers)
        self._soup = BeautifulSoup(self.response1.text,'lxml')
        self._block = self._soup.find('table')
        self._post_name = self._block.find_all('tr',class_='athing submission')
        
        for i in self._post_name:
            self.__title = i.find('span',class_='titleline')
            self._sp_name_post.append(self.__title.find('a').text)
            self._sp_link_post.append(self.__title.find('a').get('href'))
            self.ne.append(None)

        self.__subline = self._block.find_all('td', class_='subtext')
        for i in self.__subline:
            self.__sp_datetime_post = i.find('span',class_='age')
            self._sp_datetime_post.append(self.__sp_datetime_post.find('a').text)       
        return [self._news_name,self._sp_name_post,self._sp_datetime_post,self.ne,self._sp_link_post]