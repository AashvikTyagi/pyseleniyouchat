# chatter
chatter is a simple way to access you.com's youchat llm from python using selenium!


chatter supports context!

i created this when i wanted a free way to access an llm from python. i had found https://github.com/Ruu3f/freeGPT and was super happy with it but it had one problem: there was no context to the next replies. that is, every time you queried the llm in your python script, it created a new 'session', so i couldn't ask successive questions or have a conversation with the llm while keeping context from previous messages. i found you.com after reading through the abovementioned freeGPT by Ruu3f (that is, freeGPT allows you to use gpt4 through you.com) and created this to use it.


my code accesses you.com and enters and reads text to and from different parts of the webpage (you.com) that i point to in my code by their xml path, which i determined by `inspect`ing the page using firefox's dev tools.


you'll need to download [TO YOUR PATH] a specific browser driver (and change browser=webdriver.Firefox() in my code) depending on the browser you want selenium to control:

- for firefox, https://github.com/mozilla/geckodriver/releases
- for safari, https://webkit.org/blog/6900/webdriver-support-in-safari-10/
- for edge, https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- for chrome, https://sites.google.com/chromium.org/driver/


when you run the python script, it launches your chosen browser in headless mode, waits for it to load, and sends '::: ' in the terminal/output window for you to enter your prompt. it prints the answer once procured and prompts for your next answer. this loops till you kill the script.


!! the code currently waits for the answer to load by waiting for a loading sign element to appear and dissapear. this is very buggy as for short replies, it often doesn't appear, so i will be changing that soon. it does, currently, work very well for answers it takes longer to load !!


note: i'm not working on improving chatter in general very actively but i will update it if i run into da problems and find da solutions.
