def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


phone_book_1 = ["119", "97674223", "1195524421"]
phone_book_2 = ["123", "456", "789"]
phone_book_3 = ["12", "123", "1235", "567", "88"]

print(solution(phone_book_1))
print(solution(phone_book_2))
print(solution(phone_book_3))

p = list(zip(phone_book_1, phone_book_3))
print(p)
