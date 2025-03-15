# pyseleniyouchat
pyseleniyouchat is a slow and simple way to access you.com's youchat llm from python using selenium!

i was happy with https://github.com/Ruu3f/freeGPT but it didn't support context (think of it as new 'session' each time), and i wanted to try out selenium, so i made this.


my code accesses you.com and enters and reads text to and from different parts of the webpage (you.com) that i point to in my code by their xml path, which i determined by `inspect`ing the page.


you'll need to download [TO YOUR PATH] a specific browser driver (and change `browser=webdriver.Firefox()` in my code) depending on the browser you want selenium to control:

- for firefox, https://github.com/mozilla/geckodriver/releases
- for safari, https://webkit.org/blog/6900/webdriver-support-in-safari-10/
- for edge, https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- for chrome, https://sites.google.com/chromium.org/driver/


when you run the python script, it:
- launches your chosen browser in headless mode
- waits for it to load
- sends '::: ' in the output window for you to enter your prompt
- prints the answer once procured and prompts for your next answer
- loops till you kill the script.


the code waits for a loading sign to appear and vanish before continuing. it's unreliable as short replies often skip the sign entirely. for longer answers, it works fine.


note: i'm not going to update this, and the you.com website layout will definitely change later on. i'll accept fixes, but don't expect more from me.
