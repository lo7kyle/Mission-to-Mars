
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter Executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Search all elements with the tag div with attribute list_text, then wait 1 second before searching components
browser.is_element_present_by_css('div.list_text', wait_time=1)

# set up html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# CSS works from right to left, such as returning the last item on the list instead of the first. 
# When using select_one, the first matching element returned will be a <li /> element with a class of slide 
# and all nested elements within it

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# after clicking full image we can now parse the full-sized image
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
print(img_soup.prettify())

# Find the relative image url
# .get('src') pulls the link to the image
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# the above pulls the link to the image by pointing BeautifulSoup to where the image will be, 
# instead of grabbing the URL directly. So when it updates we get an updated image.
# if we copy and paste this link into a browser, it won't work. This is because it's only a partial link, 
# as the base URL isn't included

# Create base url:
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# instead of scraping an entire table, we can just import it into pandas
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML.
# By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, or the first item in the list

# you can convert a table back into it's html code
df.to_html()

# quit once you're done to free computer memory
browser.quit()