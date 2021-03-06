<img src="media/cc-logo.jpg">

# <h1 align="center">Testing - Comb Confections</h1>

<a href="https://comb-confections.herokuapp.com/">Live Website</a>

<a href="https://github.com/jakefernihough/comb-confections">Github Repository</a>

# Table of Contents

1. [Functionailty](#functionailty)
1. [Validators](#validators)
    - [HTML5](#html5)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
1. [Compatability](#compatability)
1. [User Stories](#user-stories)
1. [Bugs](#bugs)

# Functionailty

## Navbar

- The navigation bar is positioned at the top of the screen and stays visible on the top of the screen when the site is being scrolled.
- When hovering over the main nav, it has a golden background colour. The icons change in size when hovering over.
- Home, Treats and Membership page links bring the user to the relevant pages.
- Treats link opend up a drop menu to give out the specific categories.
- Search button ativates the dropdown search bar on mobile. On pc, it zooms out and changes the colour to black.
- My Hive button brings a dropdown menu for My Hive, My Membership (if subscribed) and to login/logout/register.
- Admin also have a Product Management.
- Shopping bag takes you to the bag/ checkout pages.
- On mobile and tablet views, the navbar collapses and a hamburger menu button is displayed instead.
- The logo is a clickable link, when clicked on it brings the user to the home page.

## Search bar

- Is a permanent fixture on all pages.
- When clicked on the search bar, the bar gets bigger and changes background colour.
- In mobile, it is a collapsable button that pops out at the bottom of the navbar.
- When a value is entered and 'Search' is clicked, the user is navigated to the 'Treats' page with matched results displayed.
- If no results are found that match the search, a message is displayed on the screen to let the user know.

## Registration

- When not having an account, you click on the My Hive button and select either Login/ Register.
- Fill out the Register form with certain details to create an account.
- If you already have an account, it will have a link to the login page.
- If the username already exists, it will ask you to choose a new one.
- The email address must be inputted twice for verification.
- The password must be correctly written twice.
- Press Sign Up to register an account.
- User receives an email from Comb Confections with a link to 'Confirm E-mail address'.
- When the users Register, They will be greeted with a message saying successfully register as <username>

## Sign Out/ Log in

- Sign in form allows user to sign in with their existing profile.
- The validation form will display a validation message if either password or username/e-mail are left blank.
- Form will display a validation error if username/e-mail and/or password were incorrect so malicious users don't know specifically which field was incorrect.
- When the 'Forgot Password' link is clicked, the user is navigated to a page where they are prompted to enter their e-mail address. They will then receive an e-mail with a link to reset the password. When the link is clicked, the user is navigated to the page and prompted to enter the new password twice. If this is successful, the user is navigated to a success page.
- When the 'Sign Up' link is clicked on the 'Login' page, the user is brought to the Register page.
- Log Out page has one button, which when clicked, removes the user's session and logs the user out. The user is then re-directed to the Home page.

## Home page

- Home page scrolls nicely and is responsive on all screen sizes.
- All buttons are working and bring the user to the relevant pages.
- Treats link brings you to the product page.

## Treats Page 

- When the Treats link in the navbar is clicked, a dropdown offers the user to select a category or view all items in the shop.
Either option brings the user to the same Products page with items filtered to the selected category.
- Four category buttons. All Treats, Fudge, Cakes, Sweet Treats.
- Categories are filtered via the specific category.
- Sorting filter - Name, Price, Category and Rating.
- Grid response to the page. 3 on larger, 2 on medium, one on small screens.
- Each prodicy has the Image, Title, Price and Rating.
- When the image is clicked, user is navigated to the product detail page.

## Product detail

- Back button to return to previosu page.
- Detail Page displays Image, Title, Description, Category, Rating, Quantity and Add button.
- Clicking on the +/- will change the quantity of products.
- Adding more than 20 items will bring up an error message.
- When the user has selected a valid quantity and the 'Add to Bag' button is clicked, an item is added to the Bag and
 a notification is displayed with all items in the cart and the page is refreshed.
- Admin can edit | Delete products here.

## Memberships Page *No Longer Used

- For a non-user, It will display the types of memberships with the image, title, benefits, price and 'Treat Yourself' Button.
- Authorised users have the chance to Change their membership if required. Picking between the Free and the Paid subscription.
- They will then follow the same steps as below.
  A card payment will have to be used each time they do this.
- When a user selects a membership, they will be redirected to the Membership checkout.
- The user can change their membership before committing to a subscription.
- Checkout page will show the benefits one last time.
- Payment section. Shows price. 'Treat Yourself' Button to go to the Stripe Payment Screen.
- If a valid form is entered, by using a webhook user's details are added to the Stripe system, added in the database as StripeCustomer, and new membership is added to the user's profile.
- User is then re-directed to their profile page which displays the membership summary and amount.
- If the webhook fails and the user's details are not added to the systems, the user will be re-directed to the membership page next time they sign in.
- When Cancel is clicked on, the user is re-directed to the products page.
- When Confirm is clicked, the user's membership is updated and they are re-directed to their profile where they can see their new membership summary, and a message is displayed to confirm the change.

## Bag 

- When the user clicks the 'Add Treat' the product will be added to bag with a toast to confirm that it has been added.
- the bag toast shows the image, name, price, quantity and total price. It also shows how much more needs to be spent to get free delivery.
- The bag page shows the Image, Name, Description, Product Number, Price, Quantity, Update/ Remove items and subtotal.
- Shows you the bag total, the delivery cost and the Grand Total for the bag.
- Ability to keep shopping or to continue to checkout.

## Checkout Page

- On the checkout page, the user sees Order Summary, User Details, Delivery Address and Payment Info forms.
- When filling out the details, the user has an option to save these details to their profile.
- User inputs their card details.
- User can adjust their treats back on the bag page before submitting order.
- Completing order will take the page a few moments before redirecting to an order form of what has been ordered with a toast saying "order successful" and giving an order number.
- User will get an email with their details of their order.

## User Membership Page

- Logged in user only can navigate to this page from the navbar by clicking on the 'My Membership' link or their profile page.
- User sees their selected membership details and benefits and the 'Cancel Membership' button at the bottom.

# Validators

## [HTML5](#https://validator.w3.org/)
- All pages passed. The only issues were the Doctypes being declared as well as the Python functions in the code.

## [CSS3](https://jigsaw.w3.org/css-validator/)
- All CSS files passed with no errors.

## [JSHint](https://jshint.com/)
- All JS files passed.
    - Only warning was this 'template literal syntax' is only available in ES6 (use 'esversion: 6').

## [PEP8](http://pep8online.com/)
- All Passed
- I used [flake8](https://flake8.pycqa.org/en/latest/) installed on my Gitpod as a validator throughout the project.
- A Few files that came built-in Django did not meet PEP8 requirements, However this was not written by myself, so left in to not break the database.


# Usability
- To test the ease of navigation, this website was shared with friends and family of different ages and different levels of computer/smart device knowledge. There were no issues identified regarding the simplicity of navigating the website.
- The testers also verified that all functionality aspects are working as explained above and as expected.
- Testers expressed that the design is easy to understand and navigate.

# Compatability

- After using [ami.responsive](#http://ami.responsivedesign.is/) and Chrome DevTools, the pages are responsive on all devices.
- I used a Laptop screen, an Ipad and a Xiamoi Android to test out the responsiveness through this development.


1. [User Stories](#user-stories)

#### Common User Stories

i. I want to easily navigate the site so that I can find what I'm looking for.
    
- User can easily find what they need through ease of navigation.

ii. I want the website to be readable on all screen sizes.
    
- Passed responsiveness.

#### As a first time visitor

i. Understand what the website provides and whether I want to invest my
time.

- User know's exactly what is on offer from opening up page.

ii. View and compare the memberships so that I can decide is any suits me
before I subscribe.

- No Longer an option on the site.

iii. Understand the benefits of becoming a member.

- No longer on the site.

iv. Easily find how to register/ subscribe to the site without it being too
difficult to find.

- No Longer on the site

v. Be able to quickly register and start using the site so that I can have my
account and receive the benefits.

- No longer on the site.

[Back to Menu](#table-of-contents)

#### As a casual/ regular shopper I want to

i. Navigate to the product page to find what I want easily.

- Easily navigational.

ii. Filter products by category to find products faster.

- Sorts through the products with ease

iii. Sort by price/ name to find products faster.

- Sorts through the products with ease

iv. See the price before I add it to my bag.

- Can see the prices well.

v. Have a quick way of adding to the bag without having to go through extra steps.

- Easy way to add products

vi. Be able to see more details about the product before I submit to buying.

- Back button to return to treats menu

vii. Search for an item anywhere on the site.

- Search Bar available

viii. Select and edit the quantity of how many of the product I want to buy.

- Can do that on Product Detail and Bag page.

ix. See my shopping cart before checkout so I can process any changes.

- Full order avaliable

x. See all charges before purchase so that I can review my orders and if it is
suitable for my price range.

- Order details available in Bag and checkout

xi. Add my details without too many steps, so I don’t get discouraged with a
lengthy checkout system.

- Quick and simple to use UX

xii. See an order confirmation and receive an email so I have proof of
purchase.

- A message, an email and can find your order history on the profile.

[Back to Menu](#table-of-contents)

#### As a member
i. Register an account easily.

- Easy to register

ii. Log in and out quickly and easily.

- By going onto the My Hive section.

iii. See my personal details so I can manage them at any time.

- On My Hive section

iv. See my membership details and what my benefits include.

- No longer on site

v. Change the membership when I want so I have more control over my
expenditure.

- No longer on site

vi. Cancel my paid membership without any hassle.

- No longer on site

vii. See my order history so I can have the confirmation details in one place.

- Available on Profile.

viii. Receive benefits as a member.

- No longer on site

ix. See the estimated delivery date for my order.

- No longer on site

[Back to Menu](#table-of-contents)

#### As an Admin I want to

i. Be able to add an item so I can update the products on the site.

- Can do it from treats page, product detail and through admin.

ii. Be able to edit and remove items so that I can customise items on the site
and offer new deals/ products to the consumers.

- Can do it from treats page, product detail and through admin.

iii. Add/ Edit new memberships so that I can customize prices and benefits.

- No longer on site.

iv. Have oversight of user data so that I can help with any issues/ queries.

- Access to Django Admin

[Back to Menu](#table-of-contents)

1. [Bugs](#bugs)

- When Loading Data and migrating my products to Heroku, the products did not sort into their correct categories, so had to be done manually through the Admin.

- Spinning wheel when processing a payment does not show.

- I had to delete the Membership App due to spending two weeks trying to get the ability to change memberships for a current subscriber.
Unfortunately I took too much time trying to sort it with the Tutors, so had to delete it a few days before project submission. This is why the project is very basic.

- Website does not load onto iamresponsive.

[Back to Menu](#table-of-contents)