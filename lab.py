# program to accept a sentence from the user and display the longest word of the sentence along with its length 
 sentence = input('Enter a sentence:') 
 longest = max(sentence.split(),key=len) 
 print("longset word is :", longest) 
 print('and its length is :', len(longest))
