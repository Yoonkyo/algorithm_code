def solution(count):
    for counting in range(count):
        sentence = input()
        result = "No"
        new_sentence = "a"+sentence
        if new_sentence != new_sentence[::-1]:
            print("YES")
            print(new_sentence)
            continue
        new_sentence_1 = sentence+"a"
        if new_sentence_1 != new_sentence_1[::-1]:
            print("YES")
            print(new_sentence_1)
            continue
        for i in range(len(sentence)-1):
            new_sentence_2 = sentence[i]+ "a"+ sentence[i+1:]
            if new_sentence_2 != new_sentence_2[::-1]:
                result = "YES"
                break
        print(result)
        if result == "YES":
            print(new_sentence_2)
a = int(input())
solution(a)