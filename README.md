# News webscraper
This is a basic web scraper made in the Web Scraping Fundaments course of Platzi. It extract news from the newsite La Republica.
In order to use it you have to install python3 and pip in your computer and execute the following command lines.
```
git clone https://github.com/AngelFA04/basic_webscraper.git
cd basic_webscraper
#Windows
pip install virtualenv 
python -m venv venv
venv\Scripts\activate

#Linux
pip install virtualenv 
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

```
Now you can run the command to extract the news

```
python scraper.py
```
The news files are going to be saves in a new directory named `Notices`
