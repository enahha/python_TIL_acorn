import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager

font_name = font_manager.FontProperties(fname='/Users/j.ena/Library/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

# wordcloud = 메타 데이터에서 얻어진 태그들을 분석하여 중요도나 인기도 등을 고려하여 시각적으로 늘어놓아 표시하는 것이다.
#             보통은 2차원의 표와 같은 형태로 태그들이 배치되며 이때 순서는 알파벳/가나다 순으로 배치된다.
#             시각적인 중요도를 강조를 위해 각 태그들은 그 중요도(혹은 인기도)에 따라 글자의 색상이나 굵기 등 형태가 변한다.


from wordcloud import WordCloud, STOPWORDS
#pip install wordcloud 

msg = '''
cherry 제리톰 cherry 목요일 leurto  adsf 가을 cherry 토요일  sldj
일요일 sld 제리 jfldf 목요일일 leurto  adslfj
목요일 789 ldfjlqwewtry upu fdgjld
cherry 일요일 sld cherry jfldf 목요일 leurto  adslfj 
weoruwoeru  weoripti cherry
qazx 제리토 가을 koetiet 9734 234 목요일 톰 제리톰 adslfj cherry 가을
bc  토요일 하늘 lsdjlfjp 월요일 eirp cherry 토요일 weoripti
'''
# 시각화 - 지도맵, 차트, wordCloud 
# 파일처리(txt,csv,피클,json) 
# pip install WordCloud

file = open('/Users/j.ena/Desktop/python_study/study1129/data/navercm.txt', 'r', encoding='utf-8')
rfile=file.read()
print(rfile)

spwords = set(STOPWORDS)

wc = WordCloud(max_font_size=350,stopwords=spwords, font_path='C:/windows/Fonts/malgun.ttf', background_color='black', width=800, height=800)   
#~~/malgun.ttf', background_color='black', width=800, height=800)   

wc.generate(msg)
plt.figure(figsize=(12,8))
plt.imshow(wc)
plt.show()