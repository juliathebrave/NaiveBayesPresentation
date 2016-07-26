#This is a file that provides answers and hints to some question in WiDS_NaiveBayes.ipynb
from __future__ import division

hints = {}
hints[0] = 'What is 42?'
hints[1] = 'How many cookies are there in Bowl #1? How many cookies are there in total?'
hints[2] = 'How many cookies are there in Bowl #1? Of those, how many are oatmeal?'
hints[3] = "You've calculated P(Bowl #1) and P(oatmeal| Bowl #1) already. You need to calculate P(Bowl #2) and P(oatmeal|Bowl #2) now and substitute all of these values into the formula."
hints[4] = "Substitute the probabilities you already calculated into Bayes' Theorem."
hints[11] = "How many total spam messages are there? Of those, how many contain the word 'hodor'?" 
hints[12] = "How many total non-spam messages are there? Of those, how many contain the word 'hodor'?"
hints[13.7] = "Reread the answer for 13.5 -- summing to 1 is an important property that we don't have anymore if we don't divide by the denomiator."
hints[17.1] = "Try: \n winter_word_probabilities_2 = word_probabilities(winter_dict, 400, 425)\n spam_probability_prototype(winter_word_probabilities_2, 'witch red winter dragon')"
hints[17] = "This will be similar to what we did previously. First, use this new function word_probabilities to calculate\n conditional probabilities. Then use spam_probability_prototype to calculate the estimated probability\n the message is spam."

answers = {}
answers[0] = 42
answers[1] = 0.5
answers[2] = 0.75
answers[3] = 0.625
answers[4] = 0.6
answers[9] = "George R. R. Martin wrote these sentences to begin the book 'A Game of Thrones - A Song of Ice and Fire'"
answers[10] = "There are 5 words in our vocabulary, which are exactly the keys of the dictionary:" + " 'hodor', 'winter', 'witch', 'red', 'dragon'. "
answers[11] = 0.25
answers[12] = 400/425
answers[13] = 'We classify it as not spam because we estimated that the probability of this message being spam as less than 8%.'
answers[13.5] = "In the general Naive Bayes, we want to pick the hypothesis that results in the highest probability. (That's what argmax does.) Since we only have two hypotheses, 'The message is spam.' and 'The message is not spam.', their probabilities must sum to 1. Whichever one has a probability greater than 0.5 will naturally have a probability greater than the other one. This means we only need to calculate one of the two probabilities. You could investigate this yourself by changing the return statement of the function spam_probability_prototype to:\n return message_prob_if_spam / (message_prob_if_spam + message_prob_if_not_spam), message_prob_if_not_spam / (message_prob_if_spam + message_prob_if_not_spam) \n "
answers[13.7] = "No. If we don't divide by the denominator, we would have to calculate P(Spam|message) and P(not Spam|message), and check to see which one is bigger. " 
answers[14] = 'We classify it as spam because we estimated that the probability it is spam is greater than 97%.'
answers[15] = "Our classifier is absolutely certain this message isn't spam."
answers[16] = "In our training set, the word 'dragon' only appeared in messages marked as 'not spam.' \nOur model thinks that P(S|dragon) = 0. Since we are multiplying probabilities together in our calculation, this 0 \nannihilated all the other probabilities."
answers[17] = "With an estimated probability of about 66%, the message is classified as spam."

def answer(number):
	return answers.get(number, 'Sorry, ' + str(number) + ' is an invalid question number.')

def hint(number):
	return hints.get(number, 'Sorry, there are no hints available for ' + str(number) + '.')
