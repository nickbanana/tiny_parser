from nlp import SnowNLP


def main():
    list1 = []
    list2 = []
    dup = True
    Find = False
    path = 'userdict.txt'
    dict_file = open(path,'r')
    list1 = dict_file.readlines()
    for i in list1:
        list2.append(i.rstrip('\n'))
    sentence = input("請輸入句子:")
    nlpObj = SnowNLP(sentence)
    keywords = nlpObj.keywords(3)
    for i in keywords:
        for j in list2:
            if i == j:
                print("想知道" + i + "的內容")
                Find = True

    if Find is False:
        for i in list2:
            if i in sentence and dup is True:
                print("想知道" + i + "的內容")
                dup = False

if __name__ == '__main__':
    main()
