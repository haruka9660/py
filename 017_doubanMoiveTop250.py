import requests
# 网页层次结构分析库
import parsel

url = "https://movie.douban.com/top250"

# 进行网页验证，防止机器人自动爬虫，用于反爬虫
# 右键->检查->网络->刷新->top250->useragent
headers = {'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'}
response = requests.get(url=url, headers=headers) #获取的源文件

# 显示爬出来的网页信息 
# print(response.text)

# 放到文件里
# f = open("top250.txt", "a", encoding="utf-8") 
# f.write(response.text)
# f.close()

html = parsel.Selector(response.text)
datas = html.xpath('//ol[@class="grid_view"]/li') # 这一层有25个li
for data in datas:
    # get()获取数据
    data_title = data.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()').get()
    # print(data_title)

    data_info = data.xpath('div/div[2]/div[@class="bd"]/p[1]/text()').get()

    with open("top250.txt", "a", encoding="utf-8") as f:
        f.write(f"{data_title}\n{data_info.strip()}\n\n")
print("Entry saved successfully!")