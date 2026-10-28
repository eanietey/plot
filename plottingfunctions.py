import matplotlib.pyplot as plt

def plot_hist(data):

    plt.hist(data, bins=7)

    plt.ylabel('Count')
    plt.title('Frequency of letters')

    plt.show()


def plot_bar(word):

    d = dict()
    for char in word:
        d[char] = d.get(char,0) + 1  #the zero is what is returned if char is not in d
        print(d)

    plt.bar(list(d.keys()), d.values())
    plt.ylabel('Counts')
    plt.title('Frequency of letters') 
    plt.show()

def counting():
    fname = input("Enter file name: ")
    
    if len(fname) < 1:
        fname = "mbox-short-1.txt"
        
    d = dict()
    fh = open(fname)
    count=0
    count1=0
    count2=0

    for line in fh:
        #words = line.split()
        
        if len(words) == 0:
            continue
        first_word = words[0]
            
        if first_word == 'From:':
            d['From:']  = d.get('From:', 0) + 1
            count+=1
        elif first_word == 'From':
            d['From']  = d.get('From', 0) + 1
            count1+=1
        else:
            d['other'] = d.get('other', 0) + 1
            count2+=1

    for key, val in d.items():
        print(key, val)


        
