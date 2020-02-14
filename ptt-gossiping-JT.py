#抓取PTT八卦版的網頁原始碼 (HTML)
import urllib.request as req
def getData (url):
    #建立一個Request物件, 附加Requet Headers的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼,取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") #讓BeautifulSoup協助我們解析HTML格式文件
    titles=root.find_all("div", class_="title")

    #抓取上一頁的網址
    nextLink=root.find("a",string="‹ 上頁") #找到內文是‹ 上頁的標籤
    return nextLink["href"]

def getresult (url,result):
    #建立一個Request物件, 附加Requet Headers的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1", #夾帶已滿18歲的cookie
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼,取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") #讓BeautifulSoup協助我們解析HTML格式文件
    titles=root.find_all("div", class_="title")

    
    for title in titles:
        if title.a !=None: #如果標題包含a標籤 (文章沒有被刪除),則印出來
            result+=title.a.string+"\n"
            
            # print(result)
            # print(title.a.string)
    return result
#抓取一個頁面的標題
pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"
page=int(input("請輸入要查詢幾頁: "))
count=0
Current=1
result="\n"
Result=str()

while count<page:
    Currentpage = "page %d \n" % Current
    result =   Currentpage + getresult(pageurl,result) + "\n" 
    pageurl="https://www.ptt.cc"+getData(pageurl)
    count+=1
    Current+=1
    Result += result
    result = "\n"

print(Result)

with open ("gossiping2.txt","w",encoding="utf-8") as file:
    file.write(Result)

