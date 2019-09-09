from tika import parser


#PDF에서 글자 추출
def PDF2String(fileName):
    rawText = parser.from_file(fileName)
    # rawList = rawText['content'].splitlines()

    return rawText

#테스트
if __name__ == '__main__':
    text = PDF2String('N4830BU.pdf')
    print(text)