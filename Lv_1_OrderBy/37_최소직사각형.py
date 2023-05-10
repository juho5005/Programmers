def solution(sizes):
    widths = []
    heights = []

    for size in sizes :
        # 가로 : size[0]
        # 세로 : size[1]
        if size[0] > size[1] :
            widths.append(size[0])
            heights.append(size[1])
        else :
            widths.append(size[1])
            heights.append(size[0])

    return max(widths) * max(heights)