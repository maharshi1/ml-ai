Make a Django project with the following tasks:
1. Create 2 Apps in the Django project with names ‘Motor’ & ‘Accounts’.
2. Create a Home Page with url ‘home/‘ in the Motor App. Use the Class Based View for the
same to render a form with the following field-names:
1. Vehicle Number (like MH03CB8906) - Text Box with validation for the same using
Regex (think of a regex for the MH03CB8906 and consider that the vehicle number
format will always be like this)
2. Do you have a Policy with choice YES, NO.
3. Create a Login Page with url ‘/accounts/login’ to login the user based on Phone Number
and Password in the Accounts App.
4. Finally, when the user tries to access the ‘home/‘ url, it should check whether the user is
logged in or not. If not, redirect to the login page. After authentication, it should redirect to
the previous url. The redirection after login should not be hard-coded.
