# FitClub - Code Institute MileStone 4 Project 

![here](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/FitClubLanding.png)

FitClub is a health business designed to provide fitness training plans and/or dietary eating plans to customers looking to get fitter and lose weight. 

The website is primarily designed to allow any user to buy plans. The USP for the buisness is to build the 'Club' ethos and encourage users to sign up after purchasing a plan and use the forum to talk to others and share experiences, creating a fitness/shared community.

This deployed site has a fully functioning and tested products, bag, checkout, profie and forum apps. The future development plan includes, adding exercise equipment for purchase, merchandise and integrating the individual plans in to a tracker system with associated mobile app/web interface to keep users motivated. 

Further ideas are included in the User stories document but identified as for future development.
 
## UX

The UX design follows a standardised approach to usability. A simple one page landing with all of the product/sales info and then single pages for each part of the site. The site further navigates from a fixed top bar with associated dropdown menus for the account options and a permanent shopping bag displayed. 

The UX has 3 types of user. Owner, anonymous user and registered user. The design is focused on the 2 groups of users for this project. Due to the pre-built Django admin panel, the development time was spent on the user UX. Further development should be spent on a frontend to give the owner/admin greater ease in creating new products, managing orders, forums etc. 

### User Stories

![here](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/FitClubuserstories.jpg)

The **User Stories** have been detailed into a pdf [here](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/FitClub_User_Stories.pdf). The stories have been broken down in to 3 types of user, anonymous, registered & owner/admin. The status of development has also been flagged to show what items have been fully implemented, partially implemented or for future development. 

The testing will cover these user stories and their proof of implementation.

### Wireframes

The UX design and site concept **wireframes** are included here in [this](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/FitClub_Wireframing.pdf) pdf. 

### Database Schema

The database schema that is implemented is detailed here on [this](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/FitClub_DB_Schema.pdf) pdf. 

## Features

### Existing Features
The sites existing features are broken down by app. 

**Home App**

- Dynamic Information - Landing page shows potential customers the sales information and USP of the busniess by simpy viewing the home page.

- Promotional Video - Hero image contains model with motivational video of person working out, opened by clicking the button. 

- Dashboard Display - A logged in user will see the latest relevant information to them by returning to the main page *needs further development, see features left to implement*

**Products App**

- Products Link - Allows any user to see all products by having them click on the products nav link 

- Products details -  Allows users to see more information on the individual item by clicking on the item image from the all products display

- Add to Cart - Allows a user to add the item to the cart by clicking the relevant button

- Add Review - Allows a registerd user with a verified purchase to leave a review on the individual product detail page

- Filtering Products - Allows any user to filter all products for price Hi/Lo, Lo/Hi by using the dropdown menu button. 

**Bag App**

- View Bag Items/Costs - Allows any user to veiw the contents of the bag by clicking the bag icon permanently top fixed nav bar

- Bag total value - Allows any users to see the running total of the bag in the nav bar, updating automatically

- Delete Items - Allows any user to delete items from the bag contents by clicking the trash icon from the bag page

**Checkout**

- View bag items - Allows any user to see the contents of the bag they wish to purchase by clicking through the bag's checkout button. 

- Shipping/Payment details - Allows user to enter shipping/payment inforamtion in the checkout screen by using the form 

- Stripe Payments - Allows user to pay with visa or mastercard by filling out the form and submitting. 

- Order Success - User will see a success message with all order details by successfully completing the checkout process

**Profile**

- View Profile Data - Allowes a registered & logged in user to see their address and order history by logging in and going to my account via the link on the nav bar

- Update address data - Allows a registered and logged in user to update thier address details by editing the form in the my profile page and submitting via the button

- View order history - Allows a registered and logged in user to see there order history displayed in a table by going to their profile page via the link

- View individual order history - Allows user to click the individual order and view in the same page as the original order success page by 

**Forum**

- Forums post messages - Allows users to create topics and post messages for other users to see and comment on by logging in and linking to the forum pages. Then using the relevant buttons to create a new topic or post a reply

- Edit/delete post - Allows the user to edit / delete their posts on a particular topic by clicking the edit/delete button on the relevant post

### Features Left to Implement

Additional features to be implemented in the future:

**Tracker**

- Tracking App - Will identify the users purchased plan and display daily content on the dashbord (training or meal plans data)
- Weigh In capture - Will capture users weigh in data and display graphically as a graph on the users dashboard

**Admin**

- All in one Admin App - Admin app to compile sales metrics, users, and product management

- Customised Http response errors - added Customised Http pages

**Products** 

- Search/Filtering - Create a search bar and greater filtering options

**Forum** 

- More Forum Layers - Develop a more detailed forum system. Added more layers and implement an updated time/date as well as how many edits etc

## Technologies Used

The following technologies were used;

- [HTML5](https://en.wikipedia.org/wiki/HTML5) 
    - Markup language for displaying content on all web browsers 
- [CSS3](https://en.wikipedia.org/wiki/CSS) 
    - Styling language to manipulate the webpage display
- [Bootstrap4](https://getbootstrap.com/) 
    - This project uses **Bootstrap 4** to create responsive web & mobile layouts with integrated javascript
- [JQuery](https://jquery.com)
    - The project uses **JQuery** and **JQUERYUI** to simplify DOM manipulation and for its use of interface effects and widgets.
- [Python](https://www.python.org/) 
    - This project uses **Python** for the backend programming.
- [Python Django](https://www.djangoproject.com/)
    - This project uses **Python Django** framework, whose web framework helps with rapid development and clean, pragmatic design.

## Testing

The testing of this site is documented [here](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/Testing.md) in seperate markdown file.

The projects code was run through individual validators. The detailed breakdown can be found [here](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/FitClub_Validators_Summary.pdf) with written explanations on any warnings or errors.

The use of flake8 IDE plugin was run and errors corrected. The following [output](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/flake8output.txt) where the remaining flags that were not corrected due to them being self created files such as db migrations or advice flags on django model attribute. 

Two IDEs were used for the coding of this project due to the poor internet connectivity mid project. GitPod was the primary IDE and IntelliJ was used to code offline. You will notice commits detailing the move between IDEs. 

## Deployment

This specific steps to deployment and versions there of are deatiled in [this](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/Deployment.md) seperate document 


## Credits

### Content

- The text for products was copied from variou sources and is documented here in [this](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/Content.md)

- The layout for the user stories document was taken from this source [User Stories tracking template idea](https://www.techno-pm.com/2016/09/product-backlog-excel-template.html), although template was not copied just inspired by.


### Media

- [Font Awesome](https://fontawesome.com/) was used for all icons on the site unless otherwise stated in the per page attributions.

- [Unsplash](https://unsplash.com/) was used for to obtain the photo images the site. Image by image referenceing is detailed on the seperate media.md file below

- Fonts taken from [Google Fonts](https://fonts.google.com)

The media references by page are detailed on a seperate markdown [here](https://github.com/StevePilcher/FitClub-MS4/blob/master/media/files/Media.md)


### Acknowledgements

- **No** Mentoring was used in the development of this project. It was written alone. 

- Additional Django learning from Nick Walter's Django 3 - Full Stack Websites with Python Web Development course on [Udemy](https://www.udemy.com/course/django-3-make-websites-with-python-tutorial-beginner-learn-bootstrap/)

- The product, bag, checkout and profile apps were heavily influenced by the [Code Institutes](https://codeinstitute.net/) Boutique Ado tutorials, in places like for like, especially with the Stripe payments system. I found this difficult to make work without the tutorials/source code.

- The landing page effect fading sectiosn whilst scrolling was taken from [Super Hi](https://www.superhi.com/library/posts/how-to-add-web-design-elements-that-fade-in-and-out-on-scroll)

- The Forum was influenced by tutorials by [Data FLair's](https://data-flair.training/blogs/discussion-forum-python-django/) creating a discussion forum with Python Django

- I received inspiration for this project from [Sphinx Digitals](https://www.spinxdigital.com/blog/top-10-website-designs-2020/) top 10 website designs 2020, also [awwwards](https://www.awwwards.com/) 
