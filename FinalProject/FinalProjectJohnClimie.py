dataList = []

def readTxt():
    txtFile = open('data.txt', 'r')
    for count in range(507):
        print(txtFile.readline())

        txtFile.close()

def main():
    readTxt()

if __name__ == "__main__":
    main()