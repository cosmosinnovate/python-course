Data Structures

### List (done)

### Tuples (done)

### Dictionaries
Associative keys and values

```py
# Pythonic way of doing it
empty_dict = {}
# less pythonic
empty_dict2 = dict()
grades = {
    "Joel": 90, 
    "Noel": 90
}

joel_grades = grades["Joel]
```

If you try to access key that does not exist, you will get KeyError

```py
# Pythonic way of doing it
empty_dict = {}
# less pythonic
empty_dict2 = dict()
grades = {
    "Joel": 90, 
    "Noel": 90
}

try: 
    kape_grades = grades["Kape]
except KeyError:
    print("Key not found") 

```

Dictionary has get methods that return default values instead of raising 

Owner staring at me. (C28574L Ford)

joels_grade = grades.get("Joel", 0) # equals 80
kates_grade = grades.get("Kate", 0) # equals 0
no_ones_grade = grades.get("No One") # default default is None


You assign key-value pairs using the same square brackets:
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)
# replaces the old value
# adds a third entry
# equals 3

We will frequently use dictionaries as a simple way to represent structured data:

   tweet = {
       "user" : "joelgrus",
       "text" : "Data Science is Awesome",
       "retweet_count" : 100,
       "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

Besides looking for specific keys we can look at all of them:

tweet_keys   = tweet.keys()
tweet_values = tweet.values()
tweet_items  = tweet.items()

"user" in tweet_keys "user" in tweet
# list of keys
# list of values
# list of (key, value) tuples
# True, but uses a slow list in
# more Pythonic, uses faster dict in


defaultdict
Imagine that you’re trying to count the words in a document. An obvious approach is to create a dictionary in which the keys are words and the values are counts. As you check each word, you can increment its count if it’s already in the dictionary and add it to the dictionary if it’s not:


word_counts = {}
for word in document:
if word in word_counts: word_counts[word] += 1
else:
word_counts[word] = 1

defaultdict like a regular expression except that if there is no key, it will add a value using zero-based function you provided when created. 

from collections import defaultdict
word_counts = defaultdict(int) # int() produces 0 for word in document:
       word_counts[word] += 1

Counter
A Counter turns a sequence of values into a defaultdict(int)-like object mapping keys to counts. We will primarily use it to create histograms:
from collections import Counter
c = Counter([0, 1, 2, 0]) # c is (basically) { 0 : 2, 1 : 1, 2 : 1 }
This gives us a very simple way to solve our word_counts problem: word_counts = Counter(document)
A Counter instance has a most_common method that is frequently useful:
   # print the 10 most common words and their counts
for word, count in word_counts.most_common(10): print word, count

Sets
Another data structure is set, which represents a collection of distinct elements:
s = set() s.add(1) s.add(2) s.add(2)
x = len(s) y=2ins z=3ins
#sisnow{1} #sisnow{1,2} #sisstill{1,2} # equals 2
# equals True
# equals False

Strings
Collections


Advanced. Sorting. 

Sorting
Every Python list has a sort method that sorts it in place. If you don’t want to mess up your list, you can use the sorted function, which returns a new list:

x = [4,1,2,3]
y = sorted(x) # is [1,2,3,4], x is unchanged x.sort() # now x is [1,2,3,4]

By default, sort (and sorted) sort a list from smallest to largest based on naively comparing the elements to one another.
If you want elements sorted from largest to smallest, you can specify a reverse=True parameter. And instead of comparing the elements themselves, you can compare the results of a function that you specify with key:
# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key=abs, reverse=True) # is [-4,3,-2,1]
   # sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
key=lambda (word, count): count,
               reverse=True)

