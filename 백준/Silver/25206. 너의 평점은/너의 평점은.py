# 등급에 따른 과목평점
rating = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0 ,'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

cnt = 0             # 인정되는 과목의 수
grade_total = 0     # 학점의 총 합
total = 0           # 전공과목별 (학점 x 과목평점) 합

for _ in range(20):
    subject, grade, rate = input().split()
    grade = float(grade)

    if rate in rating:
        cnt += 1
        grade_total += grade
        total += grade * rating[rate]

print(total / grade_total)