system_answer = int(input())
student_answer = int(input())

if system_answer == student_answer or (system_answer != 1 and student_answer != 1):
    print("YES")
else:
    print("NO")
