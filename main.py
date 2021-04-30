# CS-6903-Project-2

import operator
from operator import itemgetter
import time
import threading
import sys
import itertools 

done = False 
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        sys.stdout.write('\rloading ' + c)
        time.sleep(.1)
    sys.stdout.write('\rDone!     ')   
def typer(strToPrint):
    for char in strToPrint:
        print(char, end='',flush=True)
        time.sleep(.03)        
def main():

# higher efficiency is faster
    # based on our stack-ranking from design doc
    # 1-indexed to match that list

    textbook_rsa = {
        'name': 'Textbook RSA',
        'security': 'OW',
        'hardness': 'RSA',
        'homomorphism': ['product'],
        'malleability': ['product'],
        'efficiency': 3
    }

    el_gamal = {
        'name': 'El Gamal',
        'security': 'IND-CPA',
        'hardness': 'DDH',
        'homomorphism': ['product'],
        'malleability': ['product'],
        'efficiency': 1
    }

    goldwasser_micali = {
        'name': 'Goldwasser-Micali',
        'security': 'IND-CPA',
        'hardness': 'Quadratic residuosity',
        'homomorphism': ['xor'],
        'malleability': ['complement'],
        'efficiency': 3
    }

    rabin = {
        'name': 'Rabin',
        'security': 'IND-CPA',
        'hardness': 'Factoring',
        'homomorphism': ['product', 'xor'],
        'malleability': ['product', 'complement'],
        'efficiency': 4
    }

    paillier = {
        'name': 'Paillier',
        'security': 'IND-CPA',
        'hardness': 'N residuosity',
        'homomorphism': ['sum'],
        'malleability': ['product', 'complement'],
        'efficiency': 1
    }

    benaloh = {
        'name': 'Benaloh',
        'security': 'IND-CPA',
        'hardness': 'N residuosity',
        'homomorphism': ['xor'],
        'malleability': ['complement'],
        'efficiency': 5
    }

    damgard_jurik = {
        'name': 'Damgard-Jurik',
        'security': 'IND-CPA',
        'hardness': 'N residuosity',
        'homomorphism': ['sum'],
        'malleability': ['product', 'complement'],
        'efficiency': 2
    }

    options = []
    #options = [textbook_rsa, el_gamal, goldwasser_micali, rabin, paillier, benaloh, damgard_jurik]

    q1 = '\nDo you know what you want to use this system for (i.e. what type of calculations you will perform over the encrypted data)?'
    q2 = '\nWhat do you want to use this system for?'
    q3 = '\nWhich functions do you need to calculate?'
    q4 = '\nIs encrypted information being exposed a concern for you?'
    q5 = '\nIs speed a concern for you?'

    IntroStr1 = '\n\nWelcome! This program is meant to help you figure out which partially homomorphic encryption scheme is best for your use case.'
    IntroStr2 = '\nThere will be around 4-5 multiple choice questions for you to answer. You can provide your answers by entering in numbers like 1 or 2 into the command line. \n\n'
   
    typer(IntroStr1)
    typer(IntroStr2)

    typer(q1)
    a1 = input('\nEnter one of the options below: \n\n 1 - Yes \n 2 - No \n\n')

    if a1 == '1':
        typer(q2)
        a2 = input('\nEnter one of the options below: \n\n 1 - Election/Voting \n 2 - Electronic Cash \n 3 - Calculating Averages \n 4 - Calculating Probabilities \n 5 - Checking Data Integrity \n 6 - Creating Digital Signatures \n 7 - Searching Over a Filesystem / Database \n 8 - Other \n\n')
       	if a2 == '1':
       		options.append(paillier)
       		options.append(damgard_jurik)
       	elif a2 == '2':
            options.append(paillier)
       	    options.append(damgard_jurik)
       	elif a2 == '3':
       	    options.append(paillier)
       	elif a2 == '4':
       	    options.append(textbook_rsa)
       	    options.append(el_gamal)
            options.append(rabin)
       	elif a2 == '5':
       	    options.append(goldwasser_micali)
       	    options.append(benaloh)
       	elif a2 == '6':
       	    options.append(el_gamal)
       	    options.append(rabin)
       	elif a2 == '7':
       	    typer('\nYou should consider a fully homomorphic encryption system. That should provide more flexibility in what you are able to compute over your encrypted data.\n\nTerminating program, goodbye!\n\n')
       	    exit()
       	elif a2 == '8':
       	    typer(q3)
       	    a3 = input('\nChoose the best fit of the options below: \n\n 1 - Addition, Multiplication by an integer, and/or Exponentiation by an integer \n 2 - Multiplication, Division, and/or Exponentiation \n 3 - Parity, Complement \n 4 - Linear Regression \n\n')
       	    if a3 == '1':
       	        options.append(paillier)
       	        options.append(damgard_jurik)
       	    if a3 == '2':
       	        options.append(textbook_rsa)
       	        options.append(el_gamal)
       	        options.append(rabin)
       	    if a3 == '3':
       	        options.append(goldwasser_micali)
       	        options.append(rabin)
       	        options.append(benaloh)
       	    if a3 == '4':
                options.append(paillier)
       	        options.append(damgard_jurik)
       	    else:
       	        typer('\nYour input is invalid.\n\nTerminating program, goodbye!\n\n')
                return
       	else:
       	    typer('\nYour input is invalid.\n\nTerminating program, goodbye!\n\n')
            return
        typer(q4)
        a4 = input('\nEnter one of the options below: \n\n 1 - Yes \n 2 - No \n\n')
        if a4 == '1':
            if textbook_rsa in options: options.remove(textbook_rsa)
        elif a4 == '2':
            pass
        else:
            typer('\nYour input is invalid.\n\nTerminating program, goodbye!\n\n')
            return
        typer(q5) 
        a5 = input('\nEnter one of the options below: \n\n 1 - Yes \n 2 - No \n\n')
        if a5 == '1':
            options = sorted(options, key = itemgetter('efficiency'), reverse=True)
        elif a5 == '2':
            pass
        else:
            typer('\nYour input is invalid.\n\nTerminating program, goodbye!\n\n')
            return
        final_answer = options[0]
        text = '\nWe recommend that the partially homomorphic encryption scheme you use is the {} cryptosystem.\n'
        typer(text.format(final_answer['name']))
        text2 = '\nHere\'s some more details about this scheme: \n - Its cryptographic security level is {}. \n - Its hardness assumption is the {} problem. \n - Its homomorphisms are {}, and its malleability properties are {}. \n - Its efficiency, on our scale from 1-5 (5 is most efficient), is {}. \n\n'

        typer(text2.format(final_answer['security'], final_answer['hardness'], final_answer['homomorphism'], final_answer['malleability'], final_answer['efficiency']))
        typer('\nThanks for playing! We hope this was useful. \n\nTerminating program, goodbye!\n\n')
        return
    elif a1 == '2':
        typer('\nYou should consider a fully homomorphic encryption system. That should provide more flexibility in what you are able to compute over your encrypted data.\n\nTerminating program, goodbye!\n\n')
        return
    else:
        typer('\nYour input is invalid.\n\nTerminating program, goodbye!\n\n')
        return


if __name__ == '__main__':
    main()
