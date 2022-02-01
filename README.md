# Auto-book COVID Test Appointment

Due to the ongoing COVID pandemic, the situation is quite dire in Germany. With daily cases having reached a record 200,000 cases day, most retail stores, bars, restaurants and gyms have implemented a 2G + rule. This means you have to either be fully vaccinated or recovered from COVID, AND, have a 24 hour negative rapid test result (the tests are free, no room for capitalism here :D).

As a person who is actively trying to lose the pandemic weight he gained, just eating while working from home, I want to go to the gym everyday. This means of course, that I have to get tested. Booking an appointment became quite monotonous. Open the website everytime, fill out the same form everytime yada yada. Sure, you have the option to save your data so next time it is just two clicks. But, as a programmer, I wanted to be even lazier. So, I decided to completely automate the booking process.

This was done via Chromedriver, Selenium, and a little bit of basic html and python knowledge.

## Chromedriver
Chromedriver is an open source tool which basically allows you to test webapps across many browsers (Chrome, Firefox, etc.). You can find out more, and download the tool here: https://chromedriver.chromium.org/ 

When downloading, make sure you download it for the correct version of the chrome browser.

## Selenium
Selenium is the secret sauce for browser automation. Using it, you can basically write code which will help you automatically navigate pages, pass user inputs and also interact (clicks) with the browser. 

## Contents of the project

The covid.py script contains the code I used for total booking automation, and the config.ini file contains all the parameters that I will pass to my script. This provides more flexibility, as I can just change the values in the config file, instead of writing hard values into the code.

## Remarks

Everytime I create a new python project, I like to create a new virtual environment using Anaconda. This helps keep package dependencies in check.

