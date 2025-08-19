from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = """
Artificial Intelligence is transforming the world. 
Python makes it easy to explore data, build ML models, 
and create amazing applications for future technology.
"""

# Generate word cloud
wc = WordCloud(width=600, height=400, background_color="black", colormap="plasma").generate(text)

# Display
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
