from nlp import SnowNLP


def main():
    sentence = input("請輸入句子:")
    nlpObj = SnowNLP(sentence)
    keyword = nlpObj.keywords(4)
    print(keyword)

if __name__ == '__main__':
    main()
