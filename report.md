# Homework 1 Report

## Basics
What is your Middlebury email?
* wellingwood@middlebury.edu

External resources used on this assignment:
* The Python `re` documentation
* Stack Overflow (for regex troubleshooting)
* Lecture notes from class

Classmates you talked to about this assignment:
* Aidan McMillan

How many hours did you spend on this assignment?
* Around 3-4 hours

How many hours did you spend outside of class on CS 457 this week, _excluding this assignment_?
* About 3 hours


## Report

### Regex Description
_Clearly describe how you make use of each of the required regular expression features in your make_message function._

#### Regular expression groups
I used `re.search(r"my name is (\w+)", text)` to capture the user's name and store it for future responses. This lets Gnorman personalize replies instead of treating every message as unrelated.

#### Character classes
I used `r"\b(hello|hi|greetings|hey)\b"` to recognize different greetings. The `\b` ensures that it only triggers on whole words, so "high" wouldn't be mistaken for "hi."

#### Quantifiers
I used `r"(\d+) (mushrooms|flowers|snails)"` with `+` to capture any number of items mentioned in a sentence. This allows Gnorman to respond dynamically to different numbers without hardcoding every possibility.

### Analysis
_Describe at least one interaction with your bot that worked well, and at least one interaction with your bot that worked poorly (or not as one might expect)._

#### An interaction that went well
##### Transcript
```
you: hello
you: my name is Finn
bot: Ah-ha! A pleasure to meet ye, Finn! What brings ye to me garden?
you: I found 5 mushrooms!
bot: Oh ho! 5 mushrooms, ye say? A fine collection indeed! But can ye find one more hidden under the toadstool?
```

##### What happened and why? What was good?
This worked pretty well because the regex correctly picked up the user's name and the number of mushrooms mentioned. The chatbot responded in character, keeping the whimsical tone and making the interaction feel dynamic.

#### An interaction that went poorly
##### Transcript
```
you: I saw 12 big mushrooms
bot: Oh ho! That be a curious thing to say! But tell me, have ye ever spoken to a talking mushroom?
```

##### What happened and why? What was bad?
The bot failed to recognize the number because the phrase "12 big mushrooms" didn't match `r"(\d+) (mushrooms|flowers|snails)"`. The regex only captures numbers immediately followed by the target words, so adjectives like "big" break it. A fix could involve a more flexible pattern like `r"(\d+)\s+\w*\s*(mushrooms|flowers|snails)"`.

### Another Chatbot
_Interact with one of your classmate's chatbots, and answer the following questions._

#### What was the chatbot called?
* ECHObot

##### Transcript
```
you: what is your name?
bot: what is your name?
you: i asked first
bot: i asked first
you: no i asked first
bot: no i asked first
you: you are just copying me
bot: you are just copying me
```

#### Did they implement any features that you would have liked to implement in your chatbot if you had extra time?
* They had a feature it just spat out what you enteres before. I think storing previous responses like this would be cool

#### Which features of regular expressions might they have used to achieve that functionality (regular expression groups, character classes, quantifiers, anchors, etc.)?
* They probably used variables to extract and store user input and just output again unchanged.
