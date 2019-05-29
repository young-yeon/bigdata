try:
    from bs4 import BeautifulSoup
    import requests as req
except:
    print("Please install beautifulsoup4,requests\n=> pip install beautifulsoup4,requests")
    import sys
    sys.exit()

class Get_comments:
    
    def __init__(self, count):
        self.query = "이승만,박정희,전두환,노태우,김영삼,김대중,노무현,이명박,박근혜,문재인".split(",")
        self.presidents = []
        self.datas = []
        self.count = count

        
    def main(self):
        index = 0
        for q in self.query:
            print("\n" + q + " 검색중...")
            self.presidents.append(q)
            raw_data = []
            tmp = 0
            for i in range(self.count):
                start = "&start=%d" %(i * 10 + 1)
                url = "https://search.naver.com/search.naver?query=" + q + "&where=news&ie=utf8" + start

                try:
                    html = req.get(url)
                    soup = BeautifulSoup(html.text, "lxml")
                except:
                    print("검색중 에러가 발생했습니다.\n동작을 중지합니다.")
                    return False
                
                now = int((i / self.count) * 100)
                if tmp * 10 < now:
                    print("///", end = "")
                    tmp += 1
                    
                raw_data += soup.find_all("a", {"class" : " _sp_each_title"})
                
            self.datas.append([])
            for x in raw_data:
                self.datas[index].append(x.text)
            
            print()    
            index += 1
            
        return True


    def print_results(self):        
        for i in range(len(self.presidents)):
            print("=" * 25)
            print(self.presidents[i])
            print("=" * 25)
            for com in self.datas[i]:
                print(com)
            print("=" * 25)
            print()


    def save_comments(self, fname):
        file = open(fname, 'w')
        for i in range(len(self.presidents)):
            file.write(self.presidents[i] + "\n")
            for com in self.datas[i]:
                file.write(com + "\n")
            file.write("\n")
        file.close()

        
if __name__ == '__main__':
    print("================================================")
    print("=*= 네이버 뉴스 대통령 검색 및 뉴스명 추출기 =*=")
    print("================================================")
    print("\n" + " " * 20 + "개발자 : Cachi")
    print("\n\n검색을 시도합니다.\n")
    n = int(input("몇 페이지를 검색하시겠습니까? >>> "))
    TEST = Get_comments(n)
    
    run = TEST.main()
    if run:
        print("\n\n검색이 완료되었습니다.\n")
        print("검색결과를 출력 하시겠습니까?")
        choice = input("1 : 화면 출력\n2 : 파일 출력\n3 : 둘다\n그외 : 종료\n>>> ")
        
        if choice == "1":
            TEST.print_results()
            
        elif choice == "2":
            fname = input("저장할 파일명을 입력해 주세요. >>> ")
            TEST.save_comments(fname)
            
        elif choice == "3":
            TEST.print_results()
            fname = input("저장할 파일명을 입력해 주세요. >>> ")
            TEST.save_comments(fname)

        else:
            print("프로그램이 종료됩니다.")
    else:
        print("\n\n[*] 인터넷 연결이나 url을 확인해 주세요!!!")
    print("================================================")
