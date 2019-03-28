# -*- coding:UTF-8 -*-

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, "words.txt"), "rb").read()


# 结巴分词
wordlist = jieba.cut(text, cut_all=True)
wl = " ".join(wordlist)
# print(wl) #输出分词之后的txt

coloring = np.array(Image.open(path.join(d, "weini.png")))

# 设置停用词
# stopwords = set(STOPWORDS)
# stopwords.add("said")

# 你可以通过 mask 参数 来设置词云形状
# 中文要设置字体，不然会出现口字乱码
wc = WordCloud(background_color="white", max_words=2000, mask=coloring,
                max_font_size=50, random_state=42,font_path='FangSong_GB2312.ttf')

wc.generate(wl)

# create coloring from image
image_colors = ImageColorGenerator(coloring)

# show
# 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

wc.to_file("wordCloud.png")
