#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    news = []
    for list in my_list:
        news.append(list)
    if idx < 0:
        return news
    if idx >= len(my_list):
        return news
    news[idx] = element
    return news
