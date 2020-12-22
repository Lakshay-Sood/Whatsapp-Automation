from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Function definitions:


def print_rules():
    print('\n++++ Rules for my Whatsapp ++++')
    print('Enter \'1\', \'n\' or \'new chat\'  to chat with a new person/group.')
    print('Enter \'2\', \'s\' or \'single msg\' to send single msg to selected person/group.')
    print('Enter \'3\', \'c\' or \'continuous msg\' to send continuous msg to selected person/group.')
    print('Enter \'4\', \'p\' or \'ping ping\' to send the same msg multiple times to selected person/group.')
    print('Enter \'5\', \'h\' or \'help\' to print rules again.')
    print('Enter \'0\', \'e\' or \'exit\' to exit whatsapp.\n')


def open_chat(person_name):
    search_box.send_keys(person_name, Keys.ENTER)
    text_box = browser.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    return text_box


def send_msg_single(msg_txt):
    if msg_txt == 'exit':
        return
    text_box.send_keys(str(msg_txt), Keys.ENTER)


def send_msg_continuous():
    while True:
        msg = input('You: ')
        if msg == 'exit':
            return
        text_box.send_keys(str(msg), Keys.ENTER)


def ping_ping(msg, n):
    i = 1
    while i <= int(n):
        send_msg_single(msg)
        text_box.send_keys(Keys.ENTER)
        i = i+1


# Driver Code
browser = webdriver.Edge('D:\\Downloads HDD\\#Setups\\msedgedriver')
browser.get('https://web.whatsapp.com/')

print('\n****************************\n   WELCOME TO MY WHATSAPP\n****************************')
print_rules()
input('Press any key after the QR code scan')

search_box = browser.find_element_by_xpath(
    '//*[@id="side"]/div[1]/div/label/div/div[2]')
text_box = None

choice = '1'  # default to open new chat
while choice != '0' and choice != 'exit' and choice != 'e':
    choice = input('What do you want to do? : ')
    if (choice == '1' or choice == 'n' or choice == 'new chat'):
        person_name = input("Enter name of person/group to begin chat with: ")
        text_box = open_chat(person_name)
    elif (choice == '2' or choice == 's' or choice == 'single msg'):
        msg = input("Enter the msg to be sent: ")
        send_msg_single(msg)
    elif (choice == '3' or choice == 'c' or choice == 'continuous msg'):
        print("Enter \'exit\' to return to main menu.")
        send_msg_continuous()
    elif (choice == '5' or choice == 'h' or choice == 'help'):
        print_rules()
    elif (choice == '4' or choice == 'p' or choice == 'ping ping'):
        msg = input("Enter the msg to be sent: ")
        n = input("Enter number of times: ")
        ping_ping(msg, n)

browser.close()

# https://pypi.org/project/selenium/
# //*[@id="side"]/div[1]/div/label/div/div[2]       //search_box
# //*[@id="main"]/footer/div[1]/div[2]/div/div[2]   //text_box

# browser.find_element_by_tag_name()
