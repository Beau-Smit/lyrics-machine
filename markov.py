'''
k-th order Markov model Learning Algorithm
'''
import numpy as np

class Markov:
    '''
    This class is used for speaker identification based on written text. The 
    class will learn features about the speech patterns of two speakers. It can 
    then use those patterns to compare the likelihood of an unknown text being 
    uttered by those speakers.

    Attributes:
        text: a text to learn from and associate with the speaker
        k: the number of letters to use in each key to build our word dictionary
        text_len: characters in the text
        unique_chars: unique characters in the text
        data: dictionary containing the data for the Markov model
    '''
    def __init__(self, text, k):
        '''
        Constructor for the Markov class
        '''
        self.text = text
        self.k = k
        self.text_len = len(self.text)
        self.unique_chars = set(self.text)
        self.data = {}
        
        for idx in range(self.text_len):

            k_str = self.text[idx : (idx + self.k)]
            k_1_str = self.text[idx : (idx + self.k + 1)]

            # adjust for wrap arounds
            if len(k_str) < self.k:
                k_missing_chars = self.k - len(k_str)
                k_str += self.text[:k_missing_chars]
            if len(k_1_str) < (self.k + 1):
                k_1_missing_chars = (self.k + 1) - len(k_1_str)
                k_1_str += self.text[:k_1_missing_chars]

            if k_str not in self.data:
                self.data[k_str] = 0
            if k_1_str not in self.data:
                self.data[k_1_str] = 0

            self.data[k_str] += 1
            self.data[k_1_str] += 1
    
    def log_probability(self, new_str):
        '''
        This method takes in a new string and returns the log probability that 
        the modeled speaker uttered it.

        Input:
            new_str (str) - text of an unknown speaker
        Output:
            the log_probability that the modeled speaker uttered it
        '''
        _s = len(self.unique_chars)
        log_prob_acc = 0
        
        for idx in range(len(new_str)):

            k_str = new_str[idx : (idx + self.k)]
            k_1_str = new_str[idx : (idx + self.k + 1)]

            # adjust for wrap arounds
            if len(k_str) < self.k:
                k_missing_chars = self.k - len(k_str)
                k_str += self.text[:k_missing_chars]
            if len(k_1_str) < (self.k + 1):
                k_1_missing_chars = (self.k + 1) - len(k_1_str)
                k_1_str += self.text[:k_1_missing_chars]
            
            # how many times did k_str and k_1_str appear in self.text?
            if k_str in self.data:
                _n = self.data[k_str]
            else:
                _n = 0
            if k_1_str in self.data:
                _m = self.data[k_1_str]
            else:
                _m = 0
            
            # Laplace smoothing (add-one smoothing to be precise)
            log_prob_acc += np.log((_m + 1) / (_n + _s))
            
        return log_prob_acc / len(new_str)
