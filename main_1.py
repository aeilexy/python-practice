from munch import Munch
#A1 다음 동영상들의 제목과 조회수를 모두 출력하세요.
videos = [
    {"title": "동문 주변 맛집", "views": 2025106018, "likes": 4300, "saved": True},
    {"title": "응정 2학년의 하루 VLOG", "views": 54000, "likes": 1800, "saved": False},
    {"title": "GLC 동아리 홍보", "views": 210000, "likes": 9200, "saved": True},
    {"title": "응정 개강총회 3월 18일 18시 양푼이 주막", "views": 330000, "likes": 90000, "saved": False},
    {"title": "진로특강 3월 24일 11:30 이윤재관 801호", "views": 870000, "likes": 31300, "saved": True},
]

# C1
videos_dict = {video["title"]: {"views": video["views"], "likes": video["likes"], "saved": video["saved"]} for video in videos}



if __name__ == "__main__":
    print("YOUTUBe analyzer")

# D1
    for video in videos:
        title = video["title"]
        rest = {k: v for k, v in video.items() if k != "title"}
        rest = Munch({K: v for K, v in video.items() if K != "title"})
    videos_dict[title] = rest
    videos = videos_dict

#A2
    # for video in videos:
    #     if video["views"] >= 100000:
    #         print(video["title"])
#A3
    # for video in videos:
    #     like_ratio = video["likes"] / video["views"] *100
    #     print(f"video{video['title']}의 좋아요 비율: {like_ratio:.2f}%")    

#C2
    for title, info in videos_dict.items():
        if info["views"] >= 100000:
            print(title)
#C3
    for title, info in videos_dict.items():
        like_ratio = info["likes"] / info["views"] * 100
        print(f"video {title}의 좋아요 비율: {like_ratio:.2f}%")
    

# A4
    # saved_videos = []
    # for video in videos:
    #     if video["saved"]:
    #         saved_videos.append(video["title"])
    # print(saved_videos)
# B1
    # saved_videos = [video["title"] for video in videos if video["saved"]]
    # print(saved_videos)
# C4
    save_videos = []
    for title, info in videos_dict.items():
        if info["saved"]:
            save_videos.append(title)
    print(save_videos)


# A5
    # sum_views = 0
    # for video in videos:
    #     sum_views += video["views"]
    # print(f"총 조회수: {sum_views}")
# # B2
#     sum_views = sum(video["views"] for video in videos)
#     print(f"총 조회수: {sum_views}")
# C5
    sum_views = 0
    for info in videos_dict.values():
        sum_views += info["views"]
    print(f"총 조회수: {sum_views}")


# A6
    # saved_videos = []
    # for video in videos:
    #     saved_videos.append(video["views"])
    # print(f"조회수가 가장 높은 영상의 조회수: {max(saved_videos)}")
# B3
    # max_views = max(video[views] for video in videos)
    # print(f"조회수가 가장 높은 영상의 조회수: {max_views}")
# C6
    max_views = 0
    for info in videos_dict.values():
        if info["views"] > max_views:
            max_views = info["views"]
    print(f"조회수가 가장 높은 영상의 조회수: {max_views}")

        






















