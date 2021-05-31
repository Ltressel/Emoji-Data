#Problem statement:What are the most popular emojis on social media?
#We’ll analyze how frequently emojis are used across several
#different social media platforms. You can compare your emoji use
#with the vast majority of other users.

#Data taken from: EmojiXpress app: http://www.emojistats.org/, Hashtag searchs on Instagram, and Twitter: http://emojitracker.com/

#But given this variety of sources, how do we determine which emojis are truly the most popular?

#We consider the most popular emojis to be the ones most commonly used on a given platform. That’s why we took the top 10 most common emojis from EmojiXpress, Instagram, and Twitter, adding Facebook and Emojipedia to flesh things out:
#Top 10 emojis from EmojiXpress, an emoji keyboard for iOS (source: EmojiStats)
#Top 10 emojis on Instagram (source: CNBC)
#Top 10 emojis on Twitter (source: EmojiTracker)
#Top 10 emojis on Facebook (source: Emojipedia)
#Top emojis on Emojipedia (source: Emojipedia).
#Sources 1, 2, and 3 will provide us with the required statistics.
#I've arranged their data into "emoji.csv"

#Exercise 1: Get a takeaway from the data. Including normalization of data, in order
#to make a true comparison of emojis across platforms.

#In this exercise, you will use the code to:
#
#   1. Calculate mean values for all three platforms and then save
#   them in the variables emojixpress_mean, instagram_mean, and twitter_mean.
#
#   2. Calculate the usage index for each emoji:
#   the sum of normalized values for the emoji on each platform.
#   Store the usage index and add this new column of values to the table.
#
#   3. As the final step to get the answer, we're going to need to sort the table
#   in descending order by the added column and only print the first five elements.

data = [
    ['Grinning', 2.26, 1.02, 87.3],
    ['Beaming', 19.1, 1.69, 150.0],
    ['ROFL', 25.6, 0.774, 0.0],
    ['Tears of Joy', 233.0, 7.31, 2270.0],
    ['Winking', 15.2, 2.36, 264.0],
    ['Happy', 22.7, 4.26, 565.0],
    ['Heart Eyes', 64.6, 11.2, 834.0],
    ['Kissing', 87.5, 5.13, 432.0],
    ['Thinking', 6.81, 0.636, 0.0],
    ['Unamused', 6.0, 0.236, 478.0],
    ['Sunglasses', 4.72, 3.93, 198.0],
    ['Loudly Crying', 24.7, 1.35, 654.0],
    ['Kiss Mark', 21.7, 2.87, 98.7],
    ['Two Hearts', 10.0, 5.69, 445.0],
    ['Heart', 118.0, 26.0, 1080.0],
    ['Heart Suit', 3.31, 1.82, 697.0],
    ['Thumbs Up', 23.1, 3.75, 227.0],
    ['Shrugging', 1.74, 0.11, 0.0],
    ['Fire', 4.5, 2.49, 150.0],
    ['Recycle', 0.0333, 0.056, 932.0]
]

emojixpress_sum = 0
instagram_sum = 0
twitter_sum = 0
for row in data:
    emojixpress_sum += row[1]
    instagram_sum += row[2]
    twitter_sum += row[3]
    
emojixpress_mean = emojixpress_sum / len(data)
instagram_mean = instagram_sum / len(data)
twitter_mean = twitter_sum / len(data)

for i in range(len(data)):
    emojixpress_normalized = data[i][1] / emojixpress_mean
    instagram_normalized = data[i][2] / instagram_mean
    twitter_normalized = data[i][3] / twitter_mean
    index = emojixpress_normalized + instagram_normalized + twitter_normalized
    data[i].append(index)

data.sort(key=lambda row: row[1], reverse=True)

print('Emoji name       | EmojiXpress, mil.')
print('-----------------------------------')
for row in data[:5]:
    print('{: <16} | {: >16.2f}'.format(row[0], row[1]))
print()
print()

data.sort(key=lambda row: row[2], reverse=True)

print('Emoji name       | Instagram, mil.')
print('---------------------------------')
for row in data[:5]:
    print('{: <16} | {: >14.2f}'.format(row[0], row[2]))
print()
print()

data.sort(key=lambda row: row[3], reverse=True)

print('Emoji name       | Twitter, mil.')
print('-------------------------------')
for row in data[:5]:
    print('{: <16} | {: >12.2f}'.format(row[0], row[3]))
print()
print()

data.sort(key=lambda row: row[4], reverse=True)

print('Emoji name       | Usage index')
print('---------------------------------------')
for row in data[:5]:
    print('{: <16} | {: >20.2f}'.format(row[0], row[4]))
print()
print()

#What did you conclude from the table you generated?

#The most popular emojis are the ones linked to positive emotions
#— happiness and love.

#The ranking order of emojis may be different on various platforms,
#but the most popular emojis are the same all across the board.

#Individual websites have their own idiosyncrasies that generate outliers,
#as is the case of the Recycle emoji on Twitter. Artifacts can be avoided by
#collecting values from all platforms, and then normalizing them.

#To quit after running code type: exit()
