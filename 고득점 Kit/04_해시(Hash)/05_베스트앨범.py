def solution(genres, plays):
    dic = {}

    genres_plays = []

    ans = []

    # 고유 번호
    idx = 0

    for g, p in zip(genres, plays) :
        genres_plays.append((g, p, idx))
        idx += 1

    # 장르 별 노래 재생 횟수를 구함
    for g, p, _ in genres_plays :
        if g not in dic :
            dic[g] = p
        else :
            dic[g] += p

    # 노래가 재생된 횟수가 많은 수를 기준으로 정렬
    sorted_dic = sorted(dic.items(), key=lambda data:data[1], reverse=True)

    for g, _ in sorted_dic :

        compare_lst = []
        
        for genre_name, p, idx in genres_plays :
            if g == genre_name :
                compare_lst.append((p, idx))

        # 플레이 수(내림차순), 인덱스(오름차순)
        compare_lst.sort(key=lambda data:(-data[0], data[1]))
        
        cnt = 0
        two_album = 2

        for c,idx in compare_lst :
            cnt += 1
            ans.append(idx)

            if cnt == two_album :
                break 
        
    return ans