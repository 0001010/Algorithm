"""
이 문제의 핵심은 끝까지 마을을 돌면서 가장 많은 거리비용이 드는 곳을 제외하면 된다.
마지막에서 처음으로는 돌아가지 않으니..

여러가지 풀이 방법이 있지만
input을 받은다음 정렬을 해주고 가장 큰 값을 제외시켜 합을 해주면 답이 된다.

"""
input_num = int(input())

inputs = list(map(int, input().split()))

inputs.sort()
print(sum(inputs[:-1]))
