for token in range(1,11):
    print(f"serving chai to token: {token}")


def multiplication_table(number: int) -> list[str]:
    ans = []#creating a empty list
    for i in range(1,11):
        ans.append(f"{number} x {i} = {number*i}")#inserting at end
    return ans

ans = multiplication_table(5)
print(ans)


