import urllib
import urllib2
import re
import xlwt

page = 1
url = 'http://www.babymarkt.de/ernaehrung/babynahrung?page='+ str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('2">2</a></li><li>.*?</li><li><a href=".*?page=(.*?)"', re.S)
    results = re.findall(pattern, content)
    file = open('webContent.txt','w')
    file.write(content.encode('utf-8'))
    file.close()
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
    sheet.write(0,0,'Product')
    sheet.write(0,1,'Price')
    row = 1
    for page in range(1, int(results[0])+1):
    	url = 'http://www.babymarkt.de/ernaehrung/babynahrung?page='+ str(page)
    	request = urllib2.Request(url, headers = headers)
    	response = urllib2.urlopen(request)
    	content = response.read().decode('utf-8')
    	pattern = re.compile('article class="product" data-product-id=.*?title="(.*?)">.*?class="product__price">(.*?)</div>', re.S)
    	results = re.findall(pattern, content)
    	print page
    	for result in (results):
    		sheet.write(row, 0, result[0])
    		sheet.write(row, 1, result[1])
    		row+=1
	book.save('allProducts.xls')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
