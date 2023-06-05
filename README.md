# Email API
This is just a basic API I've made to send emails to any user, there might be some inconsistencies but it should work well.
I've used Django Rest Framework to acheive this

PS - The get request does not work, still trying to fix that


## Combine your mail ID
To send the mail successfully, you'll have to combine your mail ID so that the program knows who the sender is.

I've used Gmail because it was quite easy to do it with it
To enable your gmail to send mails as well, enable 2-step verification and create an app password
You can name the app anything you want (I named it Django, helps to remember) 

Now in the settings.py, on line 129 - add your email ID and on line 130 - change the email host password to whatever you got from the app password
Keep in mind both of them should be contained within the  " " 


## Using the API:
PS - This is how I did the testing in Postman, I'm not very sure if it will work as intended by directly clicking in the link given in the terminal 

1) Enter the link with the port number that you use in the code

![image](https://github.com/AzureSky007/email-api/assets/112969052/5a8e4f57-b8b6-4ded-8146-467f05446b21)

2) You'll be asked to enter a number, enter any you see fit

(http://127.0.0.1:8000/email-api/12345678) 

![image](https://github.com/AzureSky007/email-api/assets/112969052/7db7ed19-9579-41e4-a3a0-6c63d76f5dda)

3) Next, enter any greeting. Since it's not based on ML, I'd suggest entering a basic greeting like Hello or Hi

(http://127.0.0.1:8000/email-api/12345678/Hello) 

![image](https://github.com/AzureSky007/email-api/assets/112969052/904ee0c3-e32d-4418-a8eb-e7eb8f29c0c4)

4) You'll be asked for your email, which you will put in place in of the greeting. For now, I've only integrated the gmail id's, so enter any mail ID ending with '@gmail.com' 

(http://127.0.0.1:8000/email-api/12345678/youremail@gmail.com)

![image](https://github.com/AzureSky007/email-api/assets/112969052/f6928aea-3f61-4357-a41c-1961648994c8)

5) Now you enter your name by replacing the mail ID text 

(http://127.0.0.1:8000/email-api/12345678/yourname)

![image](https://github.com/AzureSky007/email-api/assets/112969052/de74ea0e-20ef-4bf8-ac9e-c7e2a1ad063a)

6) Finally, enter your city instead of the name and hit enter

(http://127.0.0.1:8000/email-api/12345678/yourcity)

![image](https://github.com/AzureSky007/email-api/assets/112969052/aba3c0de-2410-4e23-bfca-08215a36f5ff)

You should get a mail on the email ID you've entered with your details.



