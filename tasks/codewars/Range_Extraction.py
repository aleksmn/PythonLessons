# def solution(args):
#     diffs = [0]
#     ranges = ''

#     for i in range(len(args) -1):
#         diffs.append(args[i + 1] - args[i])
#     print(diffs)
#     print(args)
#     for i in range(len(diffs)):
#         if diffs[i] != 1:
#             ranges+= str(args[i]) + ', '

#     return ranges


def solution(args):

    ranges = ''

    for i in range(len(args)):

        if i == 0: 
            ranges += str(args[i]) + ", "
        elif i == len(args) - 1:
            ranges += str(args[i])
        elif args[i+1] - args[i] != 1 or args[i] - args[i-1] != 1:
            ranges += str(args[i]) + " "



    return ranges




print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
# '-6,-3-1,3-5,7-11,14,15,17-20'