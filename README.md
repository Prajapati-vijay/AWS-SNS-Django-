# AWS SNS Project 

# Setting up the AWS SNS :

1. First got to AWS 
2. After go IAM user 
3. You will see a warning by AWS that your account is sandbox mode.
4. To move out from the sandbox mode we have to send the request to AWS team by filling their request form.
5. Give your complete details in the form.
6. AWS team will approve the account in 24hrs .
7. Now go to IAM user dashboard .
8. click on the users
9. Create new user and give the following permissons:-
a. AdministratorAccess
b. AmazonSESFullAccess
c.IAMUserChangePasword
d. AmazonSNSFullAccess
10. Now get the credentials .
11. The credentials will be displayed only once so copy it .
12. Now to SNS dashboard
13. Under mobile section go to text messaging
14. Then under Text messaging preferences click on edit
15. Edit your prefrence
16. Now we are done with the AWS

# Setting up the Django project:

1. Create a virtual environment 
```
py -m venv env
```
2. Install django in virtual environment after activating it 
3. Start new project
4. Add the following in settings.py file
```
AWS_ACCESS_KEY_ID='# Access key'
AWS_SECRET_ACCESS_KEY ='# Secret acess key'
AWS_SES_REGION_NAME='#Region'
AWS_SES_REGION_ENDPOINT='# Endpoint'
```

5. Install the library for working with AWS
```
pip install boto3

```

6. Now configure the AWS before starting the project
```
aws configure

```
7. Enter all the credentials you have
8. Now you are all set to run the project 
9. ``` python manage.py runserver```