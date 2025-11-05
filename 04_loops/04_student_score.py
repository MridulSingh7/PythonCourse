names = ["Hitesh", "Meera", "Ali", "Sam"]
scores = [80,93,90,95]

def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
    ans = [] #empty list as of now
    for name,marks in zip(names,scores):
        temp = name+" : "+str(marks)
        ans.append(temp)
    return ans

scorecard = generate_score_report(names,scores)
print(scorecard)

for item in scorecard:
    print(item)
    