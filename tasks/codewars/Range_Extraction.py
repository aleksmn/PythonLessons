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


# def solution(args):
#     ranges = str(args[0])
#     streak = 0
#     for i in range(len(args)-1):
#         if args[i+1] - args[i] != 1:
#             ranges += f",{args[i+1]}"
#             streak = 0
#         else:
#             streak += 1
#             print(streak)

#     return ranges


def solution(args):

    ranges = []
    for i in range(0, len(args)-1):
        if args[i+1] - args[i] != 1:
            ranges.append(args[i])
            ranges.append(',')
            ranges.append(args[i+1])

    ranges.append(args[i+1])
    result = ''
    print(ranges)
    
    ranges = [x for x in ranges if ]

    print(ranges)
    for i in range(len(ranges)-1):
        result += str(ranges[i])

        if ranges[i] != ',' and ranges[i+1] != ',':
            if  ranges[i+1] - ranges[i] != 1:
                result += '-'
            else:
                result += ','

    result += str(ranges[-1])


    return result



# print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
# '-6,-3-1,3-5,7-11,14,15,17-20'

print(solution([-3,-2,-1,2,10,15,16,18,19,20]))