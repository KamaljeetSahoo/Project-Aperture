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
2. Open with code editor and run following commands on the terminal.
    + ` npm install `
    + ` node index.js`
3. Open the localhost link.

`.env file datas hasn't been pushed`
<br/>
You can provide your own env file of your razorpay account and mongodb database.

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
<liSearch image in pdf- The user can search and images and f the image is present in a pdf then they wil be shown the pdf where there will be option for the user to download the pdf as well.
</li></br>
</ol>

### Snapshots
---
Some of the snapshots of website.
</br>
![search](https://user-images.githubusercontent.com/68842515/144702889-4bcac9cc-c8db-487c-b090-a0d0d4b1f637.jpeg) - Search Feature
