#!/usr/bin/env python

#this is the solution for problem #17


def num2word(n):
    to_19 = ( 'zero',  'one',   'two',  'three', 'four',   'five',   'six', 'seven', 'eight', 'nine', 'ten',   'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' )

    tens  = ( 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

    denom = ( '', 'thousand',     'million',         'billion',       'trillion',       'quadrillion', 'quintillion',  'sextillion',      'septillion',    'octillion',      'nonillion', 'decillion',    'undecillion',     'duodecillion',  'tredecillion',   'quattuordecillion', 'sexdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion' )


    if n < 20 :
        return to_19[n]
    else :
        



