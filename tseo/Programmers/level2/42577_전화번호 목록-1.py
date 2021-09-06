def solution(phone_book):
    phone_book.sort()  # 일단 사전 순으로 정렬해준다

    for i in range(len(phone_book) - 1):  # 사전순으로 정렬했으니 바로 뒤에것만 체크하면 된다
        if phone_book[i] == phone_book[i + 1][: len(phone_book[i])]:
            return False

    return True


phone_book_1 = ["119", "97674223", "1195524421"]
phone_book_2 = ["123", "456", "789"]
phone_book_3 = ["12", "123", "1235", "567", "88"]

print(solution(phone_book_1))
print(solution(phone_book_2))
print(solution(phone_book_3))
