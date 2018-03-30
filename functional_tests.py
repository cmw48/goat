from selenium import webdriver

browser = webdriver.Firefox()

#user navigates to homepage
browser.get('http://localhost:8000')

#page title mentions to-do list
assert 'To-Do' in browser.title, "browser.title was " + browser.title

#enter a todo item
# type a list item into a text box
# when enter is pressed, page updates 
# list item appears in a todo list
# enter another list item in text box
# page updates, and both list items are displayed
# page explains that a unique url has been created for this list
# user navigates to url
# todo list is displayed
# end

browser.quit()
