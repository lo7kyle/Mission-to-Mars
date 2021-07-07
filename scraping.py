
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

# Defining scrape all function to connect to mongo and establish communication between our code and db
# Set up Splinter Executable path
def scrape_all():
    #initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = True) # setting true so we dont see scraping in action. happens behind the scene
    # setting our two variables to the two function returned by mars_news
    news_title, news_paragraph = mars_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }
    # When we create the HTML template, we'll create paths to the dictionary's values,
    # which lets us present our data on our template.
    #stops webdriver and return data
    browser.quit()
    return data

# Function that gets the Mars news
def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Search all elements with the tag div with attribute list_text, then wait 1 second before searching components
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # set up html parser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    # Add error handling if webpage's format changes and no longer matches HTML elements
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # CSS works from right to left, such as returning the last item on the list instead of the first. 
        # When using select_one, the first matching element returned will be a <li /> element with a class of slide 
        # and all nested elements within it

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    # if there is an error, python will continue to run rest of code, however if AttributeError, return nothing
    except AttributeError:
        return None,None
    return news_title, news_p

# Function that gets Mars image
def featured_image(browser):
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
    # print(img_soup.prettify())

    try:
        # Find the relative image url
        # .get('src') pulls the link to the image
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        # img_url_rel
    except AttributeError:
        return None
    # the above pulls the link to the image by pointing BeautifulSoup to where the image will be, 
    # instead of grabbing the URL directly. So when it updates we get an updated image.
    # if we copy and paste this link into a browser, it won't work. This is because it's only a partial link, 
    # as the base URL isn't included

    # Create base url:
    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

# Create Mars Facts function:
def mars_facts():
    # instead of scraping an entire table, we can just import it into pandas
    try:
        # Use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    # This is a general exception 
    except BaseException:
        return None

    # Assigns columns and set index of df
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    # df

    # The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML.
    # By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, or the first item in the list

    # you can convert a table back into it's html format, add bootstrap
    return df.to_html(classes="table table-striped")

# quit once you're done to free computer memory
# browser.quit()

# Our Main class that will run the code: 
if __name__ == "__main__":
    # if running as script, print scraped data
    print(scrape_all())