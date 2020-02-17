 
from urllib.request import urlopen  
from urllib import parse
from bs4 import BeautifulSoup
import json


class WebSpyder():

    JSONRESULT = "./result/enlaces.json"
    def getYoutube(self, url):

        youtubepage = self.getDoc(url)
        soup = BeautifulSoup(youtubepage, 'html.parser')

        video = soup.find('iframe')
        enlace = video.get('src')

        return enlace

    def getDoc(self, url):
    
        response = urlopen(url)

        htmlBytes = response.read()

        htmlString = htmlBytes.decode("utf-8") 
              
        return htmlString
     

    def toJson(self,name, listjson):

        with open(name, 'w') as json_file:
            json.dump(listjson, json_file)

    def createList(self,basepage):

        enlacelist = []
        enlace = {
            "desc": "",
            "enlace": "",
            "video": ""
        }

        soup = BeautifulSoup(basepage, 'html.parser')

        for link in soup.find_all('a'):
            enlace["desc"] = link.string
            enlace["enlace"] = link.get('href')
            enlace["video"] = self.getYoutube(enlace["enlace"]) 
            enlacelist.append(enlace.copy())

        return enlacelist

    def spider(self,url):  
        
        basepage = self.getDoc(url)
        
        enlacelist = self.createList(basepage)
        
        self.toJson(self.JSONRESULT,enlacelist)
        

if __name__ == "__main__":
    myspider = WebSpyder()
    myspider.spider("file:///C:/Users/aquesada/Proyectos/Pruebas/WebSpyder/Python/testpage/htmltest.html")