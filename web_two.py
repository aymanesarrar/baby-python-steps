import requests, pyperclip

# The requests module is a third party module for downloading web pages and files
# requests.get() returns a Response object
# the raise_for_status() Response method will raise an exception if the download failed
# You can save  a downloaded file to your hard drive with calls to the iter_content() method