from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt


class Wordcloud:
    def __init__(self):
        pass
        self.word_count = 100
    
    def make_cloud(self, words, name):
        counts = Counter(words)
        tags = counts.most_common(self.word_count)

        wc = WordCloud(font_path='C:\\Windows\\Fonts\\BMHANNA_11yrs_ttf.ttf', background_color='white', width=800, height=600)
        cloud = wc.generate_from_frequencies(dict(tags))
        plt.figure(figsize=(10, 8))
        plt.axis('off')
        plt.imshow(cloud)
        plt.savefig("results\\%s.png" %name)
