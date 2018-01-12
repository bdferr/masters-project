#I did not end up using this file, as I ran the tagger in a Linux VirtualBox
#and not in Python, but this may give an idea of what the tagger does.
from __future__ import print_function
import nltk
import re
import os
from math import log
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.tag.api import TaggerI
from operator import itemgetter
firsthalfdir = 'C:/users/brendan/documents/library and inormation science/masters_project/germanc-corpus/first_half_col/more_processed'
firsthalf = next(os.walk(firsthalfdir))[2]
secondhalfdir = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/second_half_col/more_processed'
secondhalf = next(os.walk(secondhalfdir))[2]

###This is copied from www.nltk.org/_modules/nltk/tag/tnt.html:
class TnT(TaggerI):
    '''
    TnT - Statistical POS tagger

    IMPORTANT NOTES:

    * DOES NOT AUTOMATICALLY DEAL WITH UNSEEN WORDS

      - It is possible to provide an untrained POS tagger to
        create tags for unknown words, see __init__ function

    * SHOULD BE USED WITH SENTENCE-DELIMITED INPUT

      - Due to the nature of this tagger, it works best when
        trained over sentence delimited input.
      - However it still produces good results if the training
        data and testing data are separated on all punctuation eg: [,.?!]
      - Input for training is expected to be a list of sentences
        where each sentence is a list of (word, tag) tuples
      - Input for tag function is a single sentence
        Input for tagdata function is a list of sentences
        Output is of a similar form

    * Function provided to process text that is unsegmented

      - Please see basic_sent_chop()


    TnT uses a second order Markov model to produce tags for
    a sequence of input, specifically:

      argmax [Proj(P(t_i|t_i-1,t_i-2)P(w_i|t_i))] P(t_T+1 | t_T)

    IE: the maximum projection of a set of probabilities

    The set of possible tags for a given word is derived
    from the training data. It is the set of all tags
    that exact word has been assigned.

    To speed up and get more precision, we can use log addition
    to instead multiplication, specifically:

      argmax [Sigma(log(P(t_i|t_i-1,t_i-2))+log(P(w_i|t_i)))] +
             log(P(t_T+1|t_T))

    The probability of a tag for a given word is the linear
    interpolation of 3 markov models; a zero-order, first-order,
    and a second order model.

      P(t_i| t_i-1, t_i-2) = l1*P(t_i) + l2*P(t_i| t_i-1) +
                             l3*P(t_i| t_i-1, t_i-2)

    A beam search is used to limit the memory usage of the algorithm.
    The degree of the beam can be changed using N in the initialization.
    N represents the maximum number of possible solutions to maintain
    while tagging.

    It is possible to differentiate the tags which are assigned to
    capitalized words. However this does not result in a significant
    gain in the accuracy of the results.
    '''

    def __init__(self, unk=None, Trained=False, N=1000, C=False):
        '''
        Construct a TnT statistical tagger. Tagger must be trained
        before being used to tag input.

        :param unk: instance of a POS tagger, conforms to TaggerI
        :type  unk:(TaggerI)
        :param Trained: Indication that the POS tagger is trained or not
        :type  Trained: boolean
        :param N: Beam search degree (see above)
        :type  N:(int)
        :param C: Capitalization flag
        :type  C: boolean

        Initializer, creates frequency distributions to be used
        for tagging

        _lx values represent the portion of the tri/bi/uni taggers
        to be used to calculate the probability

        N value is the number of possible solutions to maintain
        while tagging. A good value for this is 1000

        C is a boolean value which specifies to use or
        not use the Capitalization of the word as additional
        information for tagging.
        NOTE: using capitalization may not increase the accuracy
        of the tagger
        '''

        self._uni  = FreqDist()
        self._bi   = ConditionalFreqDist()
        self._tri  = ConditionalFreqDist()
        self._wd   = ConditionalFreqDist()
        self._eos  = ConditionalFreqDist()
        self._l1   = 0.0
        self._l2   = 0.0
        self._l3   = 0.0
        self._N    = N
        self._C    = C
        self._T    = Trained

        self._unk = unk

        # statistical tools (ignore or delete me)
        self.unknown = 0
        self.known = 0

    def train(self, data):
        '''
        Uses a set of tagged data to train the tagger.
        If an unknown word tagger is specified,
        it is trained on the same data.

        :param data: List of lists of (word, tag) tuples
        :type data: tuple(str)
        '''

        # Ensure that local C flag is initialized before use
        C = False

        if self._unk is not None and self._T == False:
            self._unk.train(data)

        for sent in data:
            history = [('BOS',False), ('BOS',False)]
            for w, t in sent:

                # if capitalization is requested,
                # and the word begins with a capital
                # set local flag C to True
                if self._C and w[0].isupper(): C=True

                self._wd[w][t] += 1
                self._uni[(t,C)] += 1
                self._bi[history[1]][(t,C)] += 1
                self._tri[tuple(history)][(t,C)] += 1

                history.append((t,C))
                history.pop(0)

                # set local flag C to false for the next word
                C = False

            self._eos[t]['EOS'] += 1

		# compute lambda values from the trained frequency distributions
        self._compute_lambda()

        #(debugging -- ignore or delete me)
        #print "lambdas"
        #print i, self._l1, i, self._l2, i, self._l3


    def _compute_lambda(self):
        '''
        creates lambda values based upon training data

        NOTE: no need to explicitly reference C,
        it is contained within the tag variable :: tag == (tag,C)

        for each tag trigram (t1, t2, t3)
        depending on the maximum value of
        - f(t1,t2,t3)-1 / f(t1,t2)-1
        - f(t2,t3)-1 / f(t2)-1
        - f(t3)-1 / N-1

        increment l3,l2, or l1 by f(t1,t2,t3)

        ISSUES -- Resolutions:
        if 2 values are equal, increment both lambda values
        by (f(t1,t2,t3) / 2)
        '''

        # temporary lambda variables
        tl1 = 0.0
        tl2 = 0.0
        tl3 = 0.0

        # for each t1,t2 in system
        for history in self._tri.conditions():
            (h1, h2) = history

            # for each t3 given t1,t2 in system
            # (NOTE: tag actually represents (tag,C))
            # However no effect within this function
            for tag in self._tri[history].keys():

                # if there has only been 1 occurrence of this tag in the data
                # then ignore this trigram.
                if self._uni[tag] == 1:
                    continue

                # safe_div provides a safe floating point division
                # it returns -1 if the denominator is 0
                c3 = self._safe_div((self._tri[history][tag]-1), (self._tri[history].N()-1))
                c2 = self._safe_div((self._bi[h2][tag]-1), (self._bi[h2].N()-1))
                c1 = self._safe_div((self._uni[tag]-1), (self._uni.N()-1))


                # if c1 is the maximum value:
                if (c1 > c3) and (c1 > c2):
                    tl1 += self._tri[history][tag]

                # if c2 is the maximum value
                elif (c2 > c3) and (c2 > c1):
                    tl2 += self._tri[history][tag]

                # if c3 is the maximum value
                elif (c3 > c2) and (c3 > c1):
                    tl3 += self._tri[history][tag]

                # if c3, and c2 are equal and larger than c1
                elif (c3 == c2) and (c3 > c1):
                    tl2 += float(self._tri[history][tag]) /2.0
                    tl3 += float(self._tri[history][tag]) /2.0

                # if c1, and c2 are equal and larger than c3
                # this might be a dumb thing to do....(not sure yet)
                elif (c2 == c1) and (c1 > c3):
                    tl1 += float(self._tri[history][tag]) /2.0
                    tl2 += float(self._tri[history][tag]) /2.0

                # otherwise there might be a problem
                # eg: all values = 0
                else:
                    #print "Problem", c1, c2 ,c3
                    pass

        # Lambda normalisation:
        # ensures that l1+l2+l3 = 1
        self._l1 = tl1 / (tl1+tl2+tl3)
        self._l2 = tl2 / (tl1+tl2+tl3)
        self._l3 = tl3 / (tl1+tl2+tl3)

    def _safe_div(self, v1, v2):
        '''
        Safe floating point division function, does not allow division by 0
        returns -1 if the denominator is 0
        '''
        if v2 == 0:
            return -1
        else:
            return float(v1) / float(v2)

    def tagdata(self, data):
        '''
        Tags each sentence in a list of sentences

        :param data:list of list of words
        :type data: [[string,],]
        :return: list of list of (word, tag) tuples

        Invokes tag(sent) function for each sentence
        compiles the results into a list of tagged sentences
        each tagged sentence is a list of (word, tag) tuples
        '''
        res = []
        for sent in data:
            res1 = self.tag(sent)
            res.append(res1)
        return res

    def tag(self, data):
        '''
        Tags a single sentence

        :param data: list of words
        :type data: [string,]

        :return: [(word, tag),]

        Calls recursive function '_tagword'
        to produce a list of tags

        Associates the sequence of returned tags
        with the correct words in the input sequence

        returns a list of (word, tag) tuples
        '''

        current_state = [(['BOS', 'BOS'], 0.0)]

        sent = list(data)

        tags = self._tagword(sent, current_state)

        res = []
        for i in range(len(sent)):
            # unpack and discard the C flags
            (t,C) = tags[i+2]
            res.append((sent[i], t))

        return res

    def _tagword(self, sent, current_states):
        '''
        :param sent : List of words remaining in the sentence
        :type sent  : [word,]
        :param current_states : List of possible tag combinations for
                                the sentence so far, and the log probability
                                associated with each tag combination
        :type current_states  : [([tag, ], logprob), ]

        Tags the first word in the sentence and
        recursively tags the reminder of sentence

        Uses formula specified above to calculate the probability
        of a particular tag
        '''

        # if this word marks the end of the sentance,
        # return the most probable tag
        if sent == []:
            (h, logp) = current_states[0]
            return h

        # otherwise there are more words to be tagged
        word = sent[0]
        sent = sent[1:]
        new_states = []

        # if the Capitalisation is requested,
        # initalise the flag for this word
        C = False
        if self._C and word[0].isupper(): C=True

        # if word is known
        # compute the set of possible tags
        # and their associated log probabilities
        if word in self._wd.conditions():
            self.known += 1

            for (history, curr_sent_logprob) in current_states:
                logprobs = []

                for t in self._wd[word].keys():
                    p_uni = self._uni.freq((t,C))
                    p_bi = self._bi[history[-1]].freq((t,C))
                    p_tri = self._tri[tuple(history[-2:])].freq((t,C))
                    p_wd = float(self._wd[word][t])/float(self._uni[(t,C)])
                    p = self._l1 *p_uni + self._l2 *p_bi + self._l3 *p_tri
                    p2 = log(p, 2) + log(p_wd, 2)

                    logprobs.append(((t,C), p2))

                # compute the result of appending each tag to this history
                for (tag, logprob) in logprobs:
                    new_states.append((history + [tag],
                                       curr_sent_logprob + logprob))

        # otherwise a new word, set of possible tags is unknown
        else:
            self.unknown += 1

            # since a set of possible tags,
            # and the probability of each specific tag
            # can not be returned from most classifiers:
            # specify that any unknown words are tagged with certainty
            p = 1

            # if no unknown word tagger has been specified
            # then use the tag 'Unk'
            if self._unk is None:
                tag = ('Unk',C)

            # otherwise apply the unknown word tagger
            else :
                [(_w, t)] = list(self._unk.tag([word]))
                tag = (t,C)

            for (history, logprob) in current_states:
                history.append(tag)

            new_states = current_states

        # now have computed a set of possible new_states

        # sort states by log prob
        # set is now ordered greatest to least log probability
        new_states.sort(reverse=True, key=itemgetter(1))

        # del everything after N (threshold)
        # this is the beam search cut
        if len(new_states) > self._N:
            new_states = new_states[:self._N]

        # compute the tags for the rest of the sentence
        # return the best list of tags for the sentence
        return self._tagword(sent, new_states)

tagger = TnT()
'''
for file in firsthalfdir:
    if re.search("^trainfold.*$", file):
        foldnum = file[9]
        tagger.train(file)
        for file in firsthalfdir:
            test = re.search("^testfold.*$", file)
            if test:
                f = re.search(foldnum, file)
                if f:
                    result = tagger.tagdata(file)
                    print list(result)

for file in secondhalfdir:
    if re.search("^trainfold.*$", file):
        foldnum = file[9]
        tagger.train(file)
    f = re.search(foldnum, file)
    test = re.search("^testfold.*$", file)
    if f and test:
        result = tagger.tagdata(file)
'''

##nltk.download()
from nltk.corpus import brown

sents = list(brown.tagged_sents())
test = list(brown.sents())

tagger.train(sents[200:1000])

# tag some data
tagged_data = tagger.tagdata(test[100:120])

# print results
for j in range(len(tagged_data)):
    s = tagged_data[j]
    t = sents[j+100]
    for i in range(len(s)):
        print(s[i],'--', t[i])
    print()
	
	
