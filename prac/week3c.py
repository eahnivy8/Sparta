import requests
from bs4 import BeautifulSoup

html = """
        <html>
            <head>
                <title>The Dormouse's story 
            </head> 
            <body>
                <h1>this is h1 area</h1> 
                <h2>this is h2 area</h2> 
                <p class="title"><b>The Dormouse's story</b></p>
                <p class="story">Once upon a time, there were three little sisters.</p>
                    <a href="http://example.com/elsie" class="sister id="link1">Elsie</a>
                    <a href="http://example.com/elsie" class="sister id="link2">Elsie</a>
                    <a data-io="link3" href="http://example.com/little" class="sister id="link3">Title</a>
                </p>
            </body> 
        </html>
        """    

# bs4 초기화 (html, 타입(xml인지html인지).parser)
soup = BeautifulSoup(html, 'html.parser')

print('soup', type(soup))
print('prettify', soup.prettify())


# import requests
# from bs4 import BeautifulSoup

# # URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup = BeautifulSoup(data.text, 'html.parser')

# # select를 이용해서, tr들을 불러오기
# movies = soup.select('#old_content > table > tbody > tr')

# # movies (tr들) 의 반복문을 돌리기
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         # a의 text를 찍어본다.
#         print (a_tag.text)