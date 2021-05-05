def solution(n):
    for i in range(n):
        string = input()
        print(string, "-", "Balanced"
      if isBalanced(string) else "Unbalanced")

def isBalanced(final_str):
    type_brackets = ['()']
    while any(x in final_str for x in type_brackets):
        for br in type_brackets:
            final_str = final_str.replace(br, '')
    return not final_str


string = "{[]{()}}"


 
a = int(input())
solution(a)