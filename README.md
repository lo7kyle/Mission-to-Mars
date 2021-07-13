# Mission-to-Mars
Building a web-scraping project using Python, Mongo, Flask, Splinter, and Beautiful Soup

## Overview:
In this challenge we were given the task to use python and the multiple libarires to scrape data about Mars. We had to use beautiful soup to scrape multiple sources and multiple data types such as tables and images onto our personal webpage. 

## Purpose:
The purpose of this challenge is familiarizing ourselves with webscraping and the different python libraries. We used python and the libraries to connect to our MongoDB and flask to set up our routes to our webpage. From this challenge we were shown how to connect these different applications into one fluid task. 

## Resources
* Data Source: https://redplanetscience.com, https://spaceimages-mars.com, https://galaxyfacts-mars.com, https://marshemispheres.com/
* Software Jupyter 6.3.0, python 3.7.4

## Analysis:
### Overview of Analysis:
The analysis of this project was pretty simple. There wasn't any complex algorithm needed or complex statistical model used. This challenge was more to familiarize ourselves with HTML and the different python libraries. The most challenging part of this analysis was understanding how every library played a different role in creating our webpage. We also had to learn how to install the proper tools and calling outside applications with our app.py file. 

### Results:
The results of this challenge was teaching us the power of webscraping and to develop our creativity with HTML bootstrap. Below is the code I implemented so that we can control our container sizes e.g. When we were asked to create a for loop to place our hemisphere photos, if we chose any other size besides 6, we would have 3 images on the same row, but with the for loop and if statement you can now choose any size that is not 6 and will always fit 2 images on each row. 

    <!--Mars Hemisphere-->
    <div class="container-fluid"> 
        <div class="row m-3" id = "mars-hemispheres">
            <h3 style="font-weight: bold;">Mars Hemispheres</h3>
            {% for hemisphere in mars.hemispheres %}
                <div class="col-md-6">
                    <figure class = "rounded p-3">
                <div class="thumbnail">
                    <img 
                    src="{{hemisphere.img_url | default('static/images/error.png', true)}}" 
                    class="img-responsive rounded" 
                    alt= "Responsive image"/>
                    <figcaption style="font-weight: bold;">{{hemisphere.title}}</figcaption>
                    </div>
                    </figure>
            {% if loop.index == 2 and not loop.last %}
                </div><div class="row m-3">
            {% endif %}
        </div>
        {% endfor %}
    </div>



### Summary:
In summary this challenge was extremely informational and I enjoyed it a lot. I really enjoyed the creative aspect of bootstrap in HTML. I also enjoyed the different webscraping techniques we learned. I can definitely see myself using webscraping and splinter on my own side projects. 