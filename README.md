![Capture](https://user-images.githubusercontent.com/64356997/144714878-e98f0a35-f6c1-4693-8ff5-3e7fad7a7a67.PNG)
# Project-Aperture
### `THEME : IMAGE SEARCH AND ANALYSIS`

`Project-Aperture` Project Aperture intends to provide an automated platform for the procedure of tagging and labelling the images by use of Image processing and Machine Learning to extract information from the images, using Convolutional Neural Networks and Natural Language Processing to generate labels and similar tags built by <b>Team Alfredo</b>


Contents
========

 * [Installation](#installation)
 * [Tech-Stacks Used](#Tech-Stacks-Used)
 * [Features Added](#Features-Added)
 * [Snapshots](#Snapshots)


### Installation
---
1. Clone the repository
2. Open the Project Path where manage.py is present in python console. (ex- C:\Users\sanim\Desktop\EYGDS\Project-Aperture)
3. Create a .env file where the subscription and API key need to go.
4. Run `python manage.py makemigrations` then `python manage.py migrate`.
5. In python console type, `python manage.py runserver`
6. The website link should be displayed on the side. Copy it and paste in the web browser.

`.env file datas hasn't been pushed`
<br/>


### Tech-Stacks Used
---
<ol>
<li> Django Templating language
<li>Django Rest Framework 
<br/>
<li>MySQL lite 
<br/>
<li>OpenCV
<br/>
<li>Azure Cognetive services
<br/>
</ol>

### Features Added
---
<ol>
    
<li>Reverse Image Search – If the user intends to find relevant images to the one he uploads, we have also provided him with the option to do so.
</li></br>
<li>Search by keyword - One can still find the appropriate images even if they commit a spelling mistake. The misspelled word gets converted to the most meaningful word present in database and results are displayed accordingly.
</li></br>
<li>Contribute - We have provided an option to the user where they can either choose to upload a single image or in a bulk
</li></br>
<li>Recently Uploaded - We Keep track of the latest image and tags uploaded to our website and we can see all the recently uploaded image in this section.
</li></br>
<li>Spell Correction (Did you Mean) – One can still find the appropriate images even if they commit a spelling mistake. The misspelled word gets converted to the most meaningful word present in database and results are displayed accordingly.
</li></br>
<li>Related tags – If the user searches for a keyword, related tags from the database are shown to them.
</li></br>
<li>Edit/Delete Tags – If the user is not satisfied with the AI generated tags, they have the option to add or delete the generated tags.  
</li></br>
<li>Similar Image band on tap – If the user wants to see the similar images, al he has to do is tap the current and they will be redirected to a page where similar images are shown.
</li></br>
<li>Most Viewed - We keep track of the image count of each image in the database. Enabling the user to view all the popular images if they wish to do so. They can also see the number of times a image is viewed and also they can see the most popular tag.
</li></br>
<li>Phrase search from images – The user can search a phase (with more than 2 words) and the related image will be displayed. Even if they make a spelling mistake or grammatical error, our model corrects it.
</li></br>
<li>Image extraction from pdfs  – If the user wants to see the images in a pdf, all they have to do is upload the pdf and then the images are extracted and displayed.
</li></br>
<li>Search image in pdf- The user can search and images and f the image is present in a pdf then they wil be shown the pdf where there will be option for the user to download the pdf as well.
</li></br>
</ol>

### Snapshots
---
Some of the snapshots of website.
</br>
![Picture1](https://user-images.githubusercontent.com/64356997/144715261-c9c9e9dd-f681-4d87-974c-cf0807f47748.png) 

![Picture2](https://user-images.githubusercontent.com/64356997/144715263-58b35fb6-a5d1-4324-b361-1711ed288549.png) <br/> - Contribute
& Recently Uploaded 

![Picture3](https://user-images.githubusercontent.com/64356997/144715264-51b1fd59-8090-42b7-b1ef-359e67779f1c.png) <br/> - Spell Correction (Did you Mean)
& Related tags

![Picture4](https://user-images.githubusercontent.com/64356997/144715269-53820aad-a8e1-492d-b95c-97304a90ec8f.png) <br/> - Edit/Delete Tags

![Picture5](https://user-images.githubusercontent.com/64356997/144715270-62a7d224-2413-4a7c-bb85-6d0ac5b2794e.png) <br/> - Similar Image band on tap
& Most Viewed

![Picture6](https://user-images.githubusercontent.com/64356997/144715272-7901d89b-1d16-4018-ac50-39f4ad5f99f3.png) <br/> - Phrase search from images

![Picture7](https://user-images.githubusercontent.com/64356997/144715273-51e720c3-46fe-4a65-9585-d4048dd5b393.png) <br/> - Image extraction from pdfs
& Search image in pdf
