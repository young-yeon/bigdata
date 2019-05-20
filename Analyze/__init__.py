from Analyze.get_news import *
from Analyze.analyze import *
from Analyze.knusl import KnuSL
from Analyze.make_wordcloud import Wordcloud
from Analyze.make_graph import *
import json
from datetime import date

def main():
    n = int(input("검색 정보 크기 입력\n>>> "))
    get_comments = Get_comments(n)
    run = get_comments.main()

    if run:
        datas = get_comments.datas
        presidents = get_comments.presidents
        del get_comments

        print("\n================================================")

        results = []
        cnt = 0
        for data in datas:
            print("\n%s 에 관한 뉴스 정보 분석" %presidents[cnt])
            cnt += 1
            results.append([])
            for text in data:
                analyze = Analyze(text)
                results[-1] += analyze.parse_phrase_to_morphemes()
            
            print("/" * 30)
        
        # 현재 단어를 뽑아내기 까지 끝냄,
        # 필요시 analyze.noun_extractor() 이용

        print("\n================================================")
        print("\n워드클라우드 생성")

        cnt = 0
        wc = Wordcloud()
        for words in results:
            wc.make_cloud(words, presidents[cnt])
            cnt += 1
        
        print("\n================================================")


        polarity = {}
        cnt = 0
        knusl = KnuSL()

        polarities = []
        for words in results:
            print("\n\n%s 에 관한 뉴스의 감성 분석" %presidents[cnt])
            polarity[presidents[cnt]] = { \
                "plus" : {"value" :0, "count" : 0}, \
                "minus" : {"value" :0, "count" : 0}, \
                "unknown" : {"value" :0, "count" : 0} }

            num = 0
            tmp = 0
            length = len(words)
            for word in words:
                _, p = knusl.data_list(word)
                if p > 0:
                    polarity[presidents[cnt]]["plus"]["value"] += p
                    polarity[presidents[cnt]]["plus"]["count"] += 1
                elif p < 0:
                    polarity[presidents[cnt]]["minus"]["value"] += p
                    polarity[presidents[cnt]]["minus"]["count"] += 1
                else:
                    polarity[presidents[cnt]]["unknown"]["count"] += 1

                now = int((num / length) * 100)
                if tmp * 10 < now:
                    print("///", end = "")
                    tmp += 1
                num += 1

            plus = polarity[presidents[cnt]]["plus"]["value"]
            minus = polarity[presidents[cnt]]["minus"]["value"]
            size = polarity[presidents[cnt]]["plus"]["count"] + \
                polarity[presidents[cnt]]["minus"]["count"]
            try:
                polarity[presidents[cnt]]["result"] = float("%.2f" %((plus + minus) / size))
                polarities.append(float("%.2f" %((plus + minus) / size)))
            except ZeroDivisionError:
                polarity[presidents[cnt]]["result"] = 0
                polarities.append(0)
            cnt += 1

        print()
        print("\n================================================\n")
        print("결과를 출력합니다 (dict)\n")
        print(polarity)
        print(polarities)
        print("\n================================================\n")
        print("결과를 저장합니다.")

        make_graph_presidents(presidents, polarities, "감성점수", "역대 대통령에 대한 뉴스 제목 감성점수")
        make_graph_economy(presidents, polarities)
        
        today = date.today()
        polarity["작성일"] = today.isoformat()

        with open('results\\result.json', 'w', encoding="utf-8") as make_file:
            json.dump(polarity, make_file, ensure_ascii=False, indent="\t")

        print("\n================================================\n")
        print("동작이 완료되었습니다.")
    
    else:
        print("에러가 발생했습니다.")
