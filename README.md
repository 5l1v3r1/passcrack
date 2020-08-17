# Passcrack

Passcrack is a simple tool used to generate wordlists from a person's Facebook likes, biographical information and Kali Linux's `rockyou.txt`.

## How it works

- You will be prompted to enter basic details about the person, such as their name, hobbies and nationality.
- You then enter the person's Facebook profile URL, which the program uses to extract some of their likes.
- The program then uses this information to generate related information, such as the person's Greek and Chinese Zodiac sign, the day of the week they were born and their current age.
- These words are then used to generate different spelling variants- all upper case, all lower case, reversed and **leetspeak**.
- The program combines all the above information into a list of words. You then have the option of creating two different wordlists- one which only uses the information you entered about the person (~ 5 million) and one which also uses the rockyou.txt passwords ( ~ 50 million), which can take signifcantly longer to compute. The word list you choose is printed out to a text file in the same directory, and each password is checked against `password.zip`, a zip file you can encrypt with a password.
- The wordlists are created using permutations of length 1, 2 and 3, along with cartesian products.


## Requirements

- requests
- beautifulsoup4

## Usage

1. Download `rockyou.txt` <a href="https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt">here</a>. This text file contains over 14 million compromised passwords from the site RockYou, and is over 100 MB, so I can't upload it here. Place this file in the passcrack directory.

2. Encrypt the file `password.txt` in a zip file using the command `zip -e password.zip password.txt` once you are inside the passcrack directory. `password.txt` serves no other purpose other than giving you a file which we can encrypt in a zip file using a password of your choice.
