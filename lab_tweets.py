#!/usr/bin/python3

'''
# Lab: Analyzing Trump Tweets

In this lab, you will analyze all tweets sent by president Trump from 2009-2018.
You will get practice
1. loading datasets stored in JSON files, and
2. creating plots in python.
This lab will also get you started on your Project 2.

The data we will analyze is used to create the following two websites:
1. [An analysis of which types of tweets Trump is likely to send himself, versus which his staffers send.](http://varianceexplained.org/r/trump-tweets/)
2. [A search engine for all of Trump's tweets.](https://www.thetrumparchive.com/)

> **Note:**
> I am using Markdown formatting within this python docstring.
> This is a *very* common practice.
> Markdown (unlike HTML) is designed to be human readable in it's "uncompiled" form.

## Part 0: Setup Project

You will have to upload files to github to submit this lab.
Complete the following steps to setup your project.

1. Create a new github repo through the github interface called `lab-markdown`.

2. Use github desktop to clone that project onto your computer.

3. Copy this `lab_tweets.py` file into your project folder.

## Part 1: Download the Data

The github repo <https://github.com/bpb27/trump_tweet_data_archive> contains an archive of tweets sent by Donald Trump.

1. Download the files `master_*.json.zip`, where * is a year.
    There should be 10 total files (2009-2018).

    > **Note:**
    > This particular archive stops in 2018 because the maintainer moved their codebase to <https://github.com/bpb27/tta-elastic>.
    > The newer archive has data that goes through the current year (and includes messages sent on Truth Social),
    > but it's a bit more complicated to access the data,
    > so we will use this older archive for this assignment.

2. Unzip these files into the project folder you created in Part 0 above.
    You should get a bunch of files that look like `master_*.json`.

## Part 2: Data Analysis

1. Modify this python file so that it:

    1. Opens each json file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.

    2. Prints the total number of tweets.

    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.
       It's important to remember that each of these words can appear with many different capitalizations, 
       and your program should count the word no matter how it is capitalized.  
       For example, `OBAMA`, `obama`, and `ObAmA` all need to count as an occurrence of the word `Obama`.

    4. Prints out a count of each of these words.

        > **Hint:**
        > My program gives the following output:
        > ```
        > len(tweets)= 36307
        > counts= {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}
        > ```
        > You'll know your program is correct if you get the same numbers.

2. Select at least 3 more interesting words/phrases to count in trump's tweets,
    and modify your program to display those words.

3. Calculate the percentage of tweets that contain each word.  (Both your new words and Trump's original tweets.)

4. Display the results nicely in a markdown table.

    The display must have all words right justified and the percents printed with two 
    significant figures (on both sides of the decimal) as shown in the example output below.

    ```
    | phrase            | percent of tweets |
    | ----------------- | ----------------- |
    |              daca | 00.17             |
    |         fake news | 00.92             |
    |  mainstream media | 00.06             |
    |            mexico | 00.55             |
    |             obama | 07.47             |
    |            russia | 01.13             |
    |             trump | 38.35             |
    |              wall | 00.91             |
    ```

    > HINT:
    > There are many ways to achieve this effect in python,
    > but I recommend using python's f-string syntax.

5. Plot the results in a bar graph.

## Submission

Create a properly formatted markdown file `README.md` that contains:
1. the markdown table created by your program
2. the image created by your program
3. a short description (1 sentence is fine) for your table/image above

Ensure that you have uploaded to your github repo:
1. your modified python file
2. your python image

Upload your github url to sakai.

## Extra Credit

There are two extra credit opportunities for this lab, worth one point each.

1. If you use the latest version of the data (instead of the files in the github repo) you will get +1 point.
    You can find instructions for accessing the data at <https://www.thetrumparchive.com/faq> under the question "Can I have the data?"

2. If you make a plot of other interesting information in this dataset (that doesn't use the 'text' key).
    For example, you could plot: what time of day does Trump tweet most often? or what state does Trump tweet from most often?
'''

import json
import pprint
import matplotlib.pyplot as plt

files = {
    'tweets_01-08-2021.json',
}

data = []

for file in files:
    with open (file, encoding = 'utf8') as fin:
        text = fin.read()
        data += json.loads(text) 

print (f'len(data)={len(data)}') # print the total number of tweets

obama_counts = 0
trump_counts = 0
mexico_counts = 0
russia_counts = 0
fake_news_counts = 0
elon_counts = 0
rich_counts = 0
god_counts = 0
retweet_counts = 0

for i, tweet in enumerate(data):
    if 'text' in tweet:

        if 'obama' in tweet['text'].lower():
            obama_counts += 1

        if 'trump' in tweet['text'].lower():
            trump_counts += 1
    # to check we can use:
    # if 'trump' in tweet['text'].lower ():
    
        if 'mexico' in tweet['text'].lower():
            mexico_counts += 1
    
        if 'russia' in tweet['text'].lower():
            russia_counts += 1

        if 'fake news' in tweet['text'].lower():
            fake_news_counts += 1

        if 'elon' in tweet['text'].lower():
            elon_counts += 1

        if 'rich' in tweet['text'].lower():
            rich_counts += 1

        if 'god' in tweet['text'].lower():
            god_counts += 1

    if int(tweet['retweets']) >= 500:
        retweet_counts += 1

print(f'obama_counts = {obama_counts}. Percentage: {100 * obama_counts/len(data):05.2f}%')
print(f'trump_counts = {trump_counts}. Percentage: {100 * trump_counts/len(data):05.2f}%')
print(f'mexico_counts = {mexico_counts}. Percentage: {100 * mexico_counts/len(data):05.2f}%')
print(f'russia_counts = {russia_counts}. Percentage: {100 * russia_counts/len(data):05.2f}%')
print(f'fake_news_counts = {fake_news_counts}. Percentage: {100 * fake_news_counts/len(data):05.2f}%')
print(f'elon_counts = {elon_counts}. Percentage: {100 * elon_counts/len(data):05.2f}%')
print(f'rich_counts = {rich_counts}. Percentage: {100 * rich_counts/len(data):05.2f}%')
print(f'god_counts = {god_counts}. Percentage: {100 * god_counts/len(data):05.2f}%')

print(f'retweet_counts = {retweet_counts}. Percentage: {100 * retweet_counts/len(data):05.2f}%')

print("| {:>18} | {:>17} |".format("phrase", "percent of tweets"))
print("| ------------------ | ----------------- |")

print(f"| {'obama'.rjust(18)} | {100 * obama_counts / len(data):05.2f}             |")
print(f"| {'trump'.rjust(18)} | {100 * trump_counts / len(data):05.2f}             |")
print(f"| {'mexico'.rjust(18)} | {100 * mexico_counts / len(data):05.2f}             |")
print(f"| {'russia'.rjust(18)} | {100 * russia_counts / len(data):05.2f}             |")
print(f"| {'fake news'.rjust(18)} | {100 * fake_news_counts / len(data):05.2f}             |")
print(f"| {'elon'.rjust(18)} | {100 * elon_counts / len(data):05.2f}             |")
print(f"| {'rich'.rjust(18)} | {100 * rich_counts / len(data):05.2f}             |")
print(f"| {'god'.rjust(18)} | {100 * god_counts / len(data):05.2f}             |")


labels = ['obama','trump','mexico','russia','fake news', 'elon', 'rich', 'god']
counts = [obama_counts, trump_counts, mexico_counts, russia_counts, fake_news_counts, elon_counts, rich_counts, god_counts]
percentages = [100 * c / len(data) for c in counts]

plt.figure(figsize=(10,6))
plt.bar(labels,percentages)

plt.ylabel("Percentage of Tweets")
plt.title("Percentage of Tweets Containing Each Phrase")
plt.xticks(rotation = 20)

for i, val in enumerate(percentages):
    plt.text(i, val + 0.2, f"{val:0.2f}%", ha='center', fontsize=9)

# Save the figure
plt.tight_layout()
plt.savefig("trump_tweet_percentages.png")
plt.show()

with open ("README.md", "w", encoding = "utf-8") as f:
    f.write ('# Trump Tweet Keyword Analysis \n\n')
    f.write ("This project analyzes President Trump's tweet from 2009-2021")
    
    f.write("## 📊 Keyword Frequency Table\n\n")
    f.write("| phrase            | percent of tweets |\n")
    f.write("| ----------------- | ----------------- |\n")

    for word in sorted(word_counts.keys()):
        percent = 100 * word_counts[word] / len(data)
        f.write(f"| {word.rjust(18)} | {percent:05.2f}             |\n")

    f.write("\n## 📈 Bar Chart\n\n")
    f.write("![Tweet Keyword Bar Chart](trump_tweet_percentages.png)\n\n")
    f.write("This chart shows how often Trump used each phrase in his tweets from 2009–2021.\n")