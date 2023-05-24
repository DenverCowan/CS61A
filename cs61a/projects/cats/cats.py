"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    '''my original solution. it works fine but the below solution is more concise and makes use of list comprehensions.
    select_paragraphs = []
    for i in range(len(paragraphs)):
        if select(paragraphs[i]):
            select_paragraphs += [paragraphs[i]]
    if k >= len(select_paragraphs):
        return ''
    else:
        return select_paragraphs[k]'''
    selected_paragraphs = [i for i in paragraphs if select(i)]
    return '' if k >= len(selected_paragraphs) else selected_paragraphs[k] # this is a conditional expression, and news to me.
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def select(p):
        paragraph = remove_punctuation(p).lower().split()
        for t in topic:
            for p in paragraph:
                if t == p:
                    return True
        return False
    return select
'''Below is my original solution. the one used is a bit more "pythonic"
#removes punctuation, puts it in lower case, and turns it into a list of words. 
        paragraph = remove_punctuation(p).lower().split()
        for i in range(len(topic)):
            for j in range(len(paragraph)):
                if topic[i] == paragraph[j]:
                    return True
        return False
    return select'''
     # END PROBLEM 2


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    correct = 0
    total_length = len(typed_words)
    ''' since in the else case we change the length of typed_words to avoid an index out of range error we need to store the length
        of typed_words so our average in the end will come out correctly. '''
    if typed_words == [] and source_words == []:
        return 100.0
    elif typed_words == [] and source_words != []:
        return 0.0
    elif typed_words != [] and source_words == []:
        return 0.0
    else:
        if len(typed_words) > len(source_words):
            typed_words = typed_words[:len(source_words)]  # this will prevent an index out of range ERROR
        for i in range(len(typed_words)):
            if typed_words[i] == source_words[i]:
                correct += 1
        return correct / total_length * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    '''My original solution. It works and is more readable but probably takes up more memory for variable storage.
    words = len(typed) / 5
    words_per_min = (words/ elapsed) * 60
    return words_per_min'''
    return ((len(typed) / 5) / elapsed) * 60
    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words -> takes in 3 args (w1,w2,limit)
        limit: a number. if lowest_diff > limit return typed word

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    '''my original solution, with help from github. I had the logic right but not that difference needed to be = to limit in the last
        step as opposed to strictly less than. the uncommented solution below is more elegant in my opinion due to its use of 
        the min function and key.
    if typed_word in word_list:
        return typed_word
    else:
        k, difference = 0, 99999
        for i in range(len(word_list)):
            new_diff = diff_function(typed_word, word_list[i], limit)
            if new_diff < difference:
                difference = new_diff
                k = i
        if difference <= limit:
            return word_list[k]
        else:
            return typed_word
            '''
    if typed_word in word_list:
        return typed_word
    else:
        closest_word = min(word_list, key= lambda word: diff_function(typed_word, word, limit))
        if diff_function(typed_word, closest_word, limit) <= limit:
            return closest_word
        return typed_word


    # END PROBLEM 5


def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    '''
    the hardest part of this is how the limit needs to adjust if the letters don't match up, as well as using built in
    string splicing functionality because I kept wanting to hard code variable like in an iteration. but the solution
    below is elegant and follows the same logic I was using. :)
    '''
    if typed == "" or source == "" or limit < 0:
        return abs(len(typed) - len(source)) if abs(len(typed) - len(source)) <= limit else limit + 1
    elif typed[:1] == source[:1]:
        return feline_fixes(typed[1:], source[1:], limit)
    else:
        return 1 + feline_fixes(typed[1:], source[1:], limit - 1)

    # END PROBLEM 6


def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.
    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    '''
    This problem is a massive recursive tree problem, the (cat,scat) example alone takes around 1000 steps in the python
    tutor. So, it's essentially impossible to trace. I tried to solve this differently, I don't think I quite have my
    mind wrapped around inductive reasoning well enough to make the leap to this solution yet.
    '''
    #base case 1: empty string, or we surpassed the limit
    if start == "" or goal == "" or limit < 0:
        # BEGIN
        return abs(len(start) - len(goal)) if abs(len(start) - len(goal)) <= limit else limit + 1 # Fill in the condition
        # END
    elif start[0] == goal[0]: # limit stays the same because there was no change in the letters.
        return minimum_mewtations(start[1:], goal[1:], limit)
    else: # these all get a "1 + " because the count as 1 change
        add = 1 + minimum_mewtations(start, goal[1:], limit - 1)
        remove = 1 + minimum_mewtations(start[1:], goal, limit - 1)
        substitute = 1 + minimum_mewtations(start[1:], goal[1:], limit - 1)
        # BEGIN
        return min(add, remove, substitute)
        # END


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    '''My original solution below works and I am proud of it, but I did find a more concise solution which I left as the
        implemented solution. the only real difference is that given we know typed is always less than prompt we can 
        shorten our code with a for loop that way we are avoiding index out of range errors that I had to use the 
        typed_length variable to fix in my solution.'''
    correct = 0
    for k in range(len(typed)):
        if typed[k] == prompt[k]:
            correct += 1
        else:
            break
    progress = correct / len(prompt)
    upload({'id':user_id, 'progress': progress})
    return progress
    '''    
    correct = 0
    k = 0
    typed_length = len(typed) - 1
    while k <= typed_length and typed[k] == prompt[k]:
        correct += 1
        k += 1
    progress = correct / len(prompt)
    upload({'id': user_id, 'progress': progress})
    return progress
    '''
    # END PROBLEM 8


def time_per_word(words, times_per_player):
    """Given timing data, return a match dictionary, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> match["words"]
    ['collar', 'plush', 'blush', 'repute']
    >>> match["times"]
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    '''I did not get this one right away, I had the logic correct and tried to make it work a few different ways to no
        avail. I did not know about the append function for lists.'''
    new_times = []
    for t in times_per_player:
        new_times.append([t[i] - t[i - 1] for i in range(1, len(t))])
    return match(words, new_times)
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match dictionary as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(get_all_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_all_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    final_list = [[] for p in player_indices]
    for i in word_indices:
        times = [time(match, j, i) for j in player_indices]
        final_list[times.index(min(times))].append(get_word(match, i))
    return final_list

    # END PROBLEM 10


def match(words, times):
    """A dictionary containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(match["words"]), "word_index out of range of words"
    return match["words"][word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(match["words"]), "word_index out of range of words"
    assert player_num < len(match["times"]), "player_num out of range of players"
    return match["times"][player_num][word_index]


def get_all_words(match):
    """A selector function for all the words in the match"""
    return match["words"]


def get_all_times(match):
    """A selector function for all typing times for all players"""
    return match["times"]


def match_string(match):
    """A helper function that takes in a match dictionary and returns a string representation of it"""
    return f"match({match['words']}, {match['times']})"


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
