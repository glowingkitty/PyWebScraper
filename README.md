![PyWebScraper](https://raw.githubusercontent.com/marcoEDU/PyWebScraper/master/images/headerimage.jpg "PyWebScraper")

A web scraper that combines both Beautiful Soup (bs4) and Selenium.

Want to support the development and stay updated?

<a href="https://www.patreon.com/bePatron?u=24983231"><img alt="Become a Patreon" src="https://raw.githubusercontent.com/marcoEDU/PyWebScraper/master/images/patreon_button.svg"></a> <a href="https://liberapay.com/marcoEDU/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a>



## Installation

```
pip install PyWebScraper
```

## Usage

```
from PyWebScraper import Scraper
```

Scraper() will load bs4 or selenium (defined with the input 'scraper_type') to then load a website (defined by the input 'url') and save it under Scraper().page.

Optional inputs for Scraper():
```
url = str (will be opened in scraper and page saved in Scraper().page)
scraper_type = 'bs4' or 'selenium'
scroll_down = boolean (scrolls down in selenium first before saving page)
user_agent = 'desktop' or 'mobile'
auto_close_selenium = boolean (if False, you can further interact with the selenium browser via Scraper().selenium)
selenium_remote_webdriver = str (IP for a remote webdriver for selenium, see https://www.selenium.dev/docs/site/en/remote_webdriver/remote_webdriver_client/)
```
