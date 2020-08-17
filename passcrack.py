import datetime
import math
import itertools
from collections import Counter
import requests
from bs4 import BeautifulSoup
import zipfile
#################################################################################
#################################################################################
                                #PHASE 1#
#################################################################################
#################################################################################
                    #DEFINING TEXT PROCESSING FUNCTIONS#

# We will first define functions which will be used to extract various words and dates from our user input and format it in ways which
# can commonly occur in passwords

# While the functions below are single methods, they are defined as functions for the sake of uniformity and readability


print("""
========================================
WELCOME TO THE PASSCRACk PROGRAM
========================================

version 0.0.1

""")

print("""
Please wait one moment while program initialises...
""")



def captitalize(word):
    return word.title()

def upper_case(word):
    return word.upper()

def lower_case(word):
    return word.lower()


# Used for handling any words entered which contain a space. Spaces seem to be very infrequent in passwords, although sometimes are accepted as valid characters
# For our purposes we shall ignore creating any passwords with spaces
def permutation_handler(word):
    output = []
    space_breakup = word.split(' ')
    output.append('_'.join(space_breakup))
    output.append('-'.join(space_breakup))
    output.append(''.join(space_breakup))
    for word in space_breakup:
        output.append(space_breakup)
    return output


def leet_transforms(word):
    output = []
    i=0
    for char in word:
        if char in ('a', 'A'):
            char = '4'
        elif char in ('i', 'I'):
            char = '1'
        elif char in ('e', 'E'):
            char = '3'
        elif char in ('s', 'S'):
            char = '5'
        elif char in ('b', 'B'):
            char = '8'
        elif char in ('o', 'O'):
            char = '0'
        word = word[:i] + char + word[i + 1:]
        i += 1
        if word not in output:
             output.append(word)
    return output


def reversal(word):
    reversed_word = word[::-1]
    return reversed_word


def get_birth_year(dob):
    # dob must be a string in UK format: %d/%m/%Y eg.12/03/1981
    date_obj = datetime.datetime.strptime(dob, '%d/%m/%Y')
    return date_obj.year

def get_birth_day(dob):
    # dob must be a string in UK format: %d/%m/%Y eg.12/03/1981
    date_obj = datetime.datetime.strptime(dob, '%d/%m/%Y')
    weekday = date_obj.date().weekday()
    result_dict = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    return result_dict[weekday]

def get_chinese_zodiac(dob):
    # dob must be a string in UK format: %d/%m/%Y eg.12/03/1981

    date_obj = datetime.datetime.strptime(dob, '%d/%m/%Y')
    birthyear = date_obj.year
    if ((birthyear - 2008) % 12) == 0:
        chinese_zodiac = "rat"
    elif ((birthyear - 2009) % 12) == 0:
        chinese_zodiac = "ox"
    elif ((birthyear - 2010) % 12) == 0:
        chinese_zodiac = "tiger"
    elif ((birthyear - 2011) % 12) == 0:
        chinese_zodiac = "rabbit"
    elif ((birthyear - 2012) % 12) == 0:
        chinese_zodiac = "dragon"
    elif ((birthyear - 2013) % 12) == 0:
        chinese_zodiac = "snake"
    elif ((birthyear - 2014) % 12) == 0:
        chinese_zodiac = "horse"
    elif ((birthyear - 2015) % 12) == 0:
        chinese_zodiac = "goat"
    elif ((birthyear - 2016) % 12) == 0:
        chinese_zodiac = "monkey"
    elif ((birthyear - 2017) % 12) == 0:
        chinese_zodiac = "rooster"
    elif ((birthyear - 2018) % 12) == 0:
        chinese_zodiac = "dog"
    else:
        chinese_zodiac = "pig"

    return chinese_zodiac

def get_greek_zodiac(dob):
    # dob must be a string in UK format: %d/%m/%Y eg.12/03/1981
    date_obj = datetime.datetime.strptime(dob, '%d/%m/%Y')
    birthmonth = date_obj.month
    birth_day = date_obj.day

    # Corresponding dates for January
    if birthmonth == 1:
        if birth_day <= 19:
            greek_zodiac = 'capricorn'
        else:
            greek_zodiac = 'aquarius'

	# Corresponding dates for February
    elif birthmonth == 2:
        if birth_day <= 18:
            greek_zodiac = 'aquarius'
        else:
            greek_zodiac = 'pisces'

	# Corresponding dates for March
    elif birthmonth == 3:
        if birth_day <= 20:
            greek_zodiac = 'pisces'
        else:
            greek_zodiac = 'aries'

	# Corresponding dates for April
    elif birthmonth == 4:
        if birth_day <= 19:
            greek_zodiac = 'aries'
        else:
            greek_zodiac = 'taurus'

	# Corresponding dates for May
    elif birthmonth == 5:
        if birth_day <= 20:
            greek_zodiac = 'taurus'
        else:
            greek_zodiac = 'gemini'

	# Corresponding dates for June
    elif birthmonth == 6:
        if birth_day <= 20:
            greek_zodiac = 'gemini'
        else:
            greek_zodiac = 'cancer'

	# Corresponding dates for July
    elif birthmonth == 7:
        if birth_day <= 22:
            greek_zodiac = 'cancer'
        else:
            greek_zodiac = 'leo'

	# Corresponding dates for August
    elif birthmonth == 8:
        if birth_day <= 22:
            greek_zodiac = 'leo'
        else:
            greek_zodiac = 'virgo'

	# Corresponding dates for September
    elif birthmonth == 9:
        if birth_day <= 22:
            greek_zodiac = 'virgo'
        else:
            greek_zodiac = 'libra'

	# Corresponding dates for October
    elif birthmonth == 10:
        if birth_day <= 22:
            greek_zodiac = 'libra'
        else:
            greek_zodiac = 'scorpio'

	# Corresponding dates for November
    elif birthmonth == 11:
        if birth_day <= 21:
            greek_zodiac = 'scorpio'
        else:
            greek_zodiac = 'sagittarius'

	# Corresponding dates for December
    else:
        if birth_day <= 21:
            greek_zodiac = 'sagittarius'
        else:
            greek_zodiac = 'capricorn'
    return greek_zodiac

def calculate_current_age(dob):
    # dob must be a string in UK format: %d/%m/%Y eg.12/03/1981
    date_obj = datetime.datetime.strptime(dob, '%d/%m/%Y')
    age_in_days = (datetime.datetime.today() - date_obj).days
    age = math.floor(age_in_days / 365)
    return age

def calculate_past_decade_ages(dob):
    # dob must be a string in UK format: %d/%m/%Y eg.12/03/1981
    current_age = calculate_current_age(dob)
    age_10_years_ago = current_age - 10
    if age_10_years_ago < 0:
        age_10_years_ago = 0
    return range(age_10_years_ago, current_age)

def calculate_past_decade(dob):
    current_year = datetime.datetime.today().year
    decade_ago = current_year - 10
    return range(decade_ago, current_year)


def date_to_string(date):
    return str(date)



def americanize_date_format(dob):
    # dob must be a string in UK format: %d/%m/%Y eg.12/03/1981
    date_obj = datetime.datetime.strptime(dob, '%d/%m/%Y')
    american_format_date = date_obj.strftime('%m/%d/%Y')
    return american_format_date


def gender_synonym_generator(gender):
    if gender.lower() in ['m', 'male']:
        m_synonyms = ['man','bro','dude','sir','gent','mr','mister','guy','boy','boi']
        return m_synonyms
    elif gender.lower() in ['f', 'female']:
        f_synonyms = ['woman','girl','gal','chick','lady','mrs','ms','miss','misses','grrl','gurl','madame']
        return f_synonyms
    else:
        raise ValueError("Gender input must be either 'male' or 'female'")




#################################################################################
#################################################################################
                                #PHASE 2#
#################################################################################
#################################################################################
                    #IMPORTING HACKED PASSWORD LIST#


# Now we import rockyou.txt, a hacked list of passwords from the company RockYou, resulting from a data breack in 2009

passwords = []

with open('rockyou.txt', encoding = 'latin-1') as open_file:
    for password in open_file:
        passwords.append(password)



#################################################################################
#################################################################################
                                #PHASE 3#
#################################################################################
#################################################################################
                    #GETTING TEXT INFORMATION FROM USER#

print("""
You will now be asked questions about your subject.
This biographical information will then be used to generate wordlist.
The lists are generated using all permutations of inputted numbers and words.

This cracker also utilises the infamous RockYou password leak from 2009, from which more permutations will be created.
 """)

input('Press Enter to begin...')

first_name = input('Please enter your subjects first name: ')
print('\n')
second_name = input('Please enter your subjects surname: ')
print('\n')
print('Please note, if you do not have a certain piece of information on the subject, simply hit Enter to proceed to the next question.')
print('\n')
middle_name = input('''If your subject has a middle name(s), please enter them here (if more than one simply seperate by a space): ''')
print('\n')
maiden_name = input('''If you know your subject's maiden name, please enter it here: ''')
print('\n')
birth_date_string = input('''Please enter the subjects date of birth. This should be ideally in UK format: DD/MM/YYYY.
However, if you only have the year of birth, just enter that (ie. YYYY).
Also, if you are unsure even of the subjects year of birth, then enter the earliest year you think the subject could have been born, since this program includes years and ages
for the past decade, since people often use the current year / age for their password and retain it into the future: ''')
print('\n')
# We make the assumption that the birth date is on the 1st of the Jan for the sake of later calculations
if len(birth_date_string) == 4:
    birth_date_string = '01/01/' + birth_date_string

nickname = input('If you are aware of a nickname of the subject, please enter it here: ')
print('\n')

gender = input("Please enter the subject's gender: ")
print('\n')
nationality = input("Please enter the subject's nationality: ")
print('\n')
hometown = input("Please enter the subject's hometown: ")
print('\n')
hobbies = input("Please enter any of the subject's hobbies you are aware of (just seperate each hobby with a space): ")
print('\n')
facebookurl = input("Please enter the subject's facebook profile URL (ensure there is no trailing slash): ")
print("\n")
try:
    likesurl = facebookurl + '/likes_all'
    request = requests.get(likesurl)
    print('Now program will scrape likes from Facebook profile...')
    soup = BeautifulSoup(request.text, features='lxml')
    likeslist = soup.find_all(class_='uiCollapsedList uiCollapsedListHidden uiCollapsedListNoSeparate pagesListData')[0].find_all('a')
    likes = []
    for like in likeslist:
        likes.append(like.text)
    print('\n')
    print('Likes extracted.')
    likes = likes[:-1]
except requests.exceptions.MissingSchema:
    print('No valid URL provided. Facebook likes will not be included in this wordlist...')

print('\n')
print('...')


#################################################################################
#################################################################################
                                #PHASE 4#
#################################################################################
#################################################################################
                    #PROCESSING USER INPUT AND CREATING WORDLIST#

initial_word_list = [first_name, second_name, maiden_name, birth_date_string.replace('/',''), nickname, gender, nationality, hometown] + middle_name.split() + hobbies.split()

birth_year = str(get_birth_year(birth_date_string))
birth_year_short = birth_year[2:]
birth_day = str(get_birth_day(birth_date_string))
chinese_zodiac = get_chinese_zodiac(birth_date_string)
greek_zodiac = get_greek_zodiac(birth_date_string)
current_age = str(calculate_current_age(birth_date_string))
american_birth_date_string = americanize_date_format(birth_date_string).replace('/','')
initials = first_name[0] + second_name[0]

processed_strings = [birth_year, birth_year_short, birth_day, chinese_zodiac, greek_zodiac, current_age, american_birth_date_string, initials]



past_decade_ages = [str(age) for age in calculate_past_decade_ages(birth_date_string)]
past_decade = [str(year) for year in calculate_past_decade(birth_date_string)]
past_decade_short = [year[2:] for year in past_decade]
gender_synonyms = gender_synonym_generator(gender)

processed_lists = [past_decade_ages, past_decade, past_decade_short, gender_synonyms]

for string in processed_strings:
    initial_word_list.append(string)


for entry in processed_lists:
    initial_word_list = initial_word_list + entry


# Now we create the various transformations of our wordlist, such as reversals and leetspeak

capital_list = [captitalize(word) for word in initial_word_list]
upper_list = [upper_case(word) for word in initial_word_list]
lower_list = [lower_case(word) for word in initial_word_list]
leet_list = []
for word in initial_word_list:
    leet_list += leet_transforms(word)
reversal_list = [reversal(word) for word in initial_word_list]

initial_word_list = initial_word_list + capital_list + upper_list + lower_list + leet_list + reversal_list



initial_word_list = set(initial_word_list)

# Now, we finally get to creating the permutations

print("Biographical data entry for subject complete. Now, permutations for this data will be generated...")
print('\n')
print('...')

permutations_length_1 = itertools.permutations(initial_word_list, 1)
permutations_length_2 = itertools.permutations(initial_word_list, 2)
permutations_length_3 = itertools.permutations(initial_word_list, 3)
try:
    permutations_likes = itertools.product(initial_word_list, likes)
    permuatation_likes_reverse = itertools.product(likes, initial_word_list)
except:
    pass

permutations = []

for x in permutations_length_1:
    permutations.append(x)

for x in permutations_length_2:
    permutations.append(x)

for x in permutations_length_3:
    permutations.append(x)

try:
    for x in permutations_likes:
        permutations.append(x)

    for x in permuatation_likes_reverse:
        permutations.append(x)
except:
    pass


format_string = 'There have been {} words generated in the word list from biographical data. Would you like to continue to generate more words from the hacked passwords? This will generate roughly 50 million more words. If no, the program will stop here and print out the current wordlist. (y/n): '.format(str(len(permutations)))
answer = input(format_string)

if answer.lower() == 'y':
    pass
else:
    li =[]
    print('Word list will be printed to wordlist.txt, and then each password will be checked against the encrypted password.zip')
    my_list = []
    for line in permutations:
        word = ''.join(list(line))
        my_list.append(word)
    f = open('wordlist.txt','w')
    for word in my_list:
        f.write(word+'\n')
    f.close()

    print('All passwords printed to wordlist.txt')
    print('\n')
    i = 0
    print('Password checking beginning...')
    for password in my_list:
        i += 1
        if i % 100000 == 0:
            print("{} / {} passwords checked.".format(i,len(my_list)))
        try:
            z = zipfile.ZipFile('password.zip')
            z.extract('password.txt', pwd = password.encode())
            print('PASSWORD CRACKED.')
            print('PASSWORD IS:' + password)
        except:
            pass
    print('Thank you for using this program!')
    exit()

# We now use this password list to generate some common words which will feed into our wordlist. We will remove any digits from
# the passwords, since these tend to be quite individual to the user. These words will be combined with our biographical information
# and used to make more permutations


print("\n")
print('Generating words from RockYou passwords...')
passwordchars = []
for x in passwords:
    charlist = [n for n in x if n.isalpha()]
    charstring = "".join(charlist)
    if charstring != "":
        passwordchars.append(charstring)

print('\n')
print('Done')
print('\n')

##################################################################################
# Notice that we have only selected a small number of the biographic information.
# This is to save causing a memory overload. most_important_bio_words can be altered
# to suit your RAM. IF PROGRAM CRASHES HERE REDUCE SIZE OF THIS LIST
#################################################################################

most_important_bio_words = [first_name, second_name, birth_year, birth_year_short]
print('''Program will now generate cartesian product of the following strings:''')
print('\n')
for imp in most_important_bio_words:
    print(imp + '\n')

print('With the text from 14,341,564 RockYou passwords')
print('\n')
print('This may take some time!')

permutations_length_1_rockyou = set(passwordchars).union(initial_word_list)
permutations_length_2_rockyou = itertools.product(most_important_bio_words,passwordchars)

permutations_rockyou = []
for x in permutations_length_1_rockyou:
    permutations_rockyou.append(x)
for x in permutations_length_2_rockyou:
    permutations_rockyou.append(x)


my_list2 = []
for line in permutations_rockyou:
    word = ''.join(list(line))
    my_list2.append(word)

my_list = []
for line in permutations:
    word = ''.join(list(line))
    my_list.append(word)


g = open('wordlist.txt','w')

final_list = my_list + my_list2
format_string = 'This has generated {} additional words for our wordlist'.format(str(len(my_list2)))
format_string2 = 'So in total that is {} words'.format(str(len(final_list)))
format_string3 = 'All words generated so far will now be printed to wordlist.txt, and then each password will be checked against the encrypted password.zip.'

print(format_string)
print(format_string2)
print(format_string3)

for x in final_list:
    g.write(x+'\n')

g.close()
print('All passwords printed to wordlist.txt')
print('Password checking beginning...')
i = 0
for password in final_list:
    i += 1
    if i % 100000 == 0:
        print("{} / {} passwords checked.".format(i,len(my_list)))
    try:
        z = zipfile.ZipFile('password.zip')
        z.extract('password.txt', pwd = password.encode())
        print('PASSWORD CRACKED.')
        print('PASSWORD IS:' + password)
    except:
        pass


print('Thank you for using this program!')
exit()
