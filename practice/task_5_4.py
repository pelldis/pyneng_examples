
number = int(input('Enter number: '))
word = (input('Enter word: '))


num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

num_list.reverse()
word_list.reverse()

print ('Last seen position: ', len(num_list) - 1 - num_list.index(number))
print ('Last seen word position: ', len(word_list) - 1 - word_list.index(word))
















