from lxml import etree
import requests

with open('movie.txt','w',encoding='utf-8') as f:
    for p in range(25,225,25):
        url = 'https://movie.douban.com/top250?start=0&filter={}'.format(p)

        data = requests.get(url).text
        page = etree.HTML(data)
        file = page.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
        pf = page.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
        num = page.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[4]/text()')
        words = page.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')


        for i in range(25):
            f.write("\n""{} {} {} {}".format(file[i],pf[i],num[i],words[i]))