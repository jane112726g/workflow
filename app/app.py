def dedupe(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def calculate_sum(lst):
    return sum(lst)
if __name__ == "__main__":
    test_list = [1, 2, 2, 3, 4, 4, 4]
    print("去重结果：", dedupe(test_list))
    print("总和结果：", calculate_sum(test_list))
