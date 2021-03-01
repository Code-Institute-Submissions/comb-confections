<img src="media/cc-logo.jpg">


# USER EXPERIENCE

## User Stories

### User

#### Business Goals

- Connect the business to social media to feed in a larger audience
- Outperform competitors by providing excellent services, products and support.
- Update the products with new and exciting recipes.
- Earn a profit by allowing anyone to purchase products

#### Common User Stories

i. I want to easily navigate the site so that I can find what I'm looking for.

ii. I want to be able to contact the company if I'm experiencing an issue.

iii. I want the website to be readable on all screen sizes.

#### As a first time visitor

i. Understand what the website provides and whether I want to invest my
time.

ii. View and compare the memberships so that I can decide is any suits me
before I subscribe.

iii. Understand the benefits of becoming a member.

iv. Easily find how to register/ subscribe to the site without it being too
difficult to find.

v. Be able to quickly register and start using the site so that I can have my
account and receive the benefits.

#### As a casual/ regular shopper I want to

i. Navigate to the product page to find what I want easily.

ii. Filter products by category to find products faster.

iii. Sort by price/ name to find products faster.

iv. See the price before I add it to my bag.

v. Have a quick way of adding to the bag without having to go through extra steps.

vi. Be able to see more details about the product before I submit to buying.

vii. Search for an item anywhere on the site.

viii. Select and edit the quantity of how many of the product I want to buy.

ix. See my shopping cart before checkout so I can process any changes.

x. See all charges before purchase so that I can review my orders and if it is
suitable for my price range.

xi. Add my details without too many steps, so I don’t get discouraged with a
lengthy checkout system.

xii. Secure my payment information so that I feel safe with using my card
details.

xiii. See an order confirmation and receive an email so I have proof of
purchase.

#### As a member
i. Register an account easily.

ii. Log in and out quickly and easily.

iii. See my personal details so I can manage them at any time.

iv. See my membership details and what my benefits include.

v. Change the membership when I want so I have more control over my
expenditure.

vi. Cancel my paid membership without any hassle.

vii. See my order history so I can have the confirmation details in one place.

viii. Receive benefits as a member.

ix. See the estimated delivery date for my order.

#### As an Admin I want to

i. Be able to add an item so I can update the products on the site.

ii. Be able to edit and remove items so that I can customise items on the site
and offer new deals/ products to the consumers.

iii. Add/ Edit new memberships so that I can customize prices and benefits.

iv. Have oversight of user data so that I can help with any issues/ queries.

# SCOPE

- Comb Confections is an e-commerce site.
- User
    - It allows users to Register/ Login to an account.
    - Authorise payments for membership as well as single products.
    - Shows categorised Products and Product Page.
    - Has a Profile Page for members.
    - allows users to buy products and checkout securely.
- Admin
    - Edit and add new products with prices and descriptions.
    - Modify and delete profile accounts.
    - Check to make sure payments have gone through.

# Structure

- Navigation - Top Level
- Body - Main Page Elements
- Footer

## Sign Up (Registration) and Login
I have used a 3rd Party package called Allauth to take care of the logic. 
The users are asked to fill in the Registration with fields ‘Email’, ‘Username’, and password, 
this is done twice to make sure they are both the same.

Sign Up and Login. The form has two fields, ‘email’ and ‘Password’.
Full Page background with a center-block design.

## Navigation
### Navbar

    - Left - Comb Confections logo
    - Center - Page Niavigation and Search bar.
    - Right - Checkout bag and Profile.

## Home Page
I chose to have a bee-themed site to go with the Honeycomb business.
So a bee background, with the main colours resembling that of a beehive.
I had a WELCOME opening. Then a link to look at the treats we had to offer.
We also had a JOIN THE HIVE section where a user could then purchase a membership.

## Treats Page
- You can select All Treats, or pick a particular category on the navbar.
- Use the Search bar if you're looking for anything particular.
- Select the category at the top of the page.
- The cards have a black background with white text.
- Sort the products into Alphabetical, Category, Rating and Price!
- Every item has a card with it's details on, including an image, price, rating and the name of the product!
- Clicking on the image will take you to the Details Treat page.
- *Admin* - Edit or delete product.

## Detailed Treats Page
- Navbar just above.
- Black background, white text.
- Image to the left of the page.
- On the right side you have the name of the product.
- The Price of the item.
- Brief description of the product.
- Category of the Product.
- Rating of the Product.
- Quantity bar of how many the user would like to purchase.
- Keep Shopping button to take you back to Treats Page.
- Add to Bag, to add it to the bag.
- *Admin* - Edit|Delete treat button.

## Bag

- Displays products info of what is in your bag.
- Displays image of product.
- Displays Price and Quantity of your products.
- Option to update/Delete items.
- Subtotal of that products overall price.
- Bag Total
- Delivery Price - If under the threshold.
- Grand Total Price of all the products in the bag.
- Message to let you know if the user is under/over free delivery threshold.
- Secure Checkout Button - Checkout Page.
- Keep Shopping button.

## Checkout Page.

- Order Summary. With Price, Sub Total, Grand Total.
- Details Forms.
- Name, Address, Contact Number. Option to save details to profile.
- Card Details to purchase items.
- Adjust Treats Bag.
- Complete Order.
- Final Price to declare what will be charged to your card.

## Profile

- Stores Users Delivery Details.
- Stores Order History.
- Show's what Membership the user has.


## Features Left to Implement

- Fixing the Membership option.
- Review System.


# Technologies Used
## Languages Used

- HTML5
- CSS3
- JavaScript
- Python 3.8

## Frameworks, Libraries and Programs Used.

- Front End
    - Bootstrap - Used for the responsive layout, as well as Navbar, Header, Forms and Item Cards.
    - Font Awesome - Adding the Icons throughout the pages.
    - Google Fonts - Imported the 'Playfair Display' Font.
    - jQuery - Used in JavaScript logic.
- Back End 
- Django - Main Framework to build the project
- Stripe - Used to make the single and subscription (if it worked) plans.
- Psycopg2 - *****
- Django Crispy Forms - Used to display Forms
- Gunicorn - Deployment tool.
- Boto3 - ******
- Pillow - Image processing tool in Python.
- Whitenoise - aids static file management.
- pip3 - install packages into python.
- SQlite3 - used as a database in development.
- PostgreSQL - used as a database in deployment.
- AWS S3 - USed to store images and static files on the deployed site.
- General
    - Git - Allows tracking of any changes in the code.
    - Github - Used to host the project files.
    - Heroku - A Cloud platform used to deploy the web application.
    - PicResize - edit and resize images.
    - Balsamiq - Used for Wireframes.

# Testing

# Deployment

# Credits

## Code

- The project’s code was developed by following the Code Institute video lessons and based on the understanding of the course material, 
The code has been customized and enhanced to fit with the purpose of the project. In some places the logic is used and in others the code.
- Idea for the Membership page is thank to this Git Repository https://github.com/LigaMoon/Prickly

## Content and media

All images and content are owned by Miles Billington from Comb Confections who allowed me to use his work
to produce this project.

## Acknowledgements

I would like to say thanks to these people who have helped and guided me through this final project and throughout the course.

- Adegbenga Adeye my tutor. He has supported me all this year and pushed me constantly. Thank you!.
- Miles, Fraser, Lydia, Jess, Danny, Kyle. Also My parents and my aunt... My friends and family who let me use their work, were my testers and who supported me for this journey.
- To the Tutor Scott who sat with me for 4 days trying to figure out the membership payment. (Though unfortunately didn't come to fruition).

# Final Say.

So this project has not been my favourite. Unfortunately, it wasn't the final project that I wanted to submit. I had many problems throughout the development
that caused it to not go as planned. I had the help of 8 tutors who were also stumped when trying to help me fix my goal.
Due to my new job, I had a massive time constraint, so all of the time I would have loved to make this into the best possible product,
I was unable to. I feel that this final product is a reflection of that.
I am happy with what I have achieved over the past year, helping me get into an awesome new career and bringing new skills to my life.
I know that I will continue to get better after I submit this project and this is just a small setback in a big future for myself.
This was a big challenge and just this time, I wasn't able to win. 