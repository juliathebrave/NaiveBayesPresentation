#This is a file that provides answers and hints to some question in WiDS_NaiveBayes.ipynb
from __future__ import division

hints = {}
hints[0] = 'What is 42?'
hints[1] = 'How many cookies are there in Bowl #1? How many cookies are there\nin total?'
hints[1.5] = '\nYou want to do this:\nno_of_cookies_in_bowl_1 / total_no_of_cookies_in_both_bowls\n'
hints[2] = 'How many cookies are there in Bowl #1? Of those, how many are \noatmeal?'
hints[2.5] = '\nYou want to do this:\nno_of_oatmeal_cookies_in_bowl_1 / no_of_cookies_in_bowl_1\n'
hints[3] = "You've calculated P(Bowl #1) and P(oatmeal| Bowl #1) already. \nYou need to calculate P(Bowl #2) and P(oatmeal|Bowl #2) now and\nsubstitute all of these values into the formula above."
hints[3.5] = "\nDon't worry if you get stuck. If you'd like an easier approach,\nthan using the Total Law of Probability, do this:\nno_of_oatmeal_cookies_in_both_bowls / total_no_of_cookies_in_both_bowls\n"
hints[4] = "Instead of copy/pasting you could use: \nprint(ans.answer(1)*ans.answer(2)/ans.answer(3))\n"
hints[11] = "The variable no_of_training_spams is already assigned.\nThe number of training spams containing the word 'hodor' is:\nwinter_dict['hodor'][0]"
hints[11.5] ="\nUse:\nno_of_training_spams_containing_hodor = winter_dict['hodor'][0]\n"

hints[12] = "The variable no_of_training_hams is already assigned.\nThe number of training hams containing the word 'hodor' is:\nwinter_dict['hodor'][1]"
hints[12.5] ="\nUse:\nno_of_training_hams_containing_hodor = winter_dict['hodor'][1]\n"


answers = {}
answers[0] = 42
answers[1] = 0.5
answers[2] = 0.75
answers[3] = 0.625
answers[4] = 0.6
answers[9] = "George R. R. Martin wrote these sentences to begin the book \n'A Game of Thrones - A Song of Ice and Fire'"
answers[10] = "There are 5 words in our vocabulary, which are exactly the \nkeys of the dictionary:" + " 'hodor', 'winter', 'witch', 'red', 'dragon'. "
answers[11] = 0.25
answers[12] = 400/425

answers[14] = 'We classify it as spam because we estimated that the \nprobability it is spam (97%) is greater than 50%.'
answers[15] = "Our classifier is absolutely certain this message isn't spam.\nThis is suspicious!"
answers[16] = "In our training set, the word 'dragon' only appeared in \nmessages marked as 'not spam.' Our model thinks that P(S|dragon) = 0.\nSince we are multiplying probabilities together in our calculation, this 0 \nannihilated all the other probabilities."
answers[17] = "With an estimated probability of about 85% (which is greater than 50%)\nthe message is classified as 'spam.'' \nThis is a very different answer than classifying the same message as \n'not spam' with absolute certainty!"

def answer(number):
	return answers.get(number, 'Sorry, ' + str(number) + ' is an invalid question number.')

def hint(number):
	return hints.get(number, 'Sorry, there are no hints available for ' + str(number) + '.')
