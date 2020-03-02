""" Score points with min number of attempts to reach the target
Starting with points[0], each points[i] is an attempt irrespective of (points[i] - points[0]) != target
Problem get solved when points[i] - points[0] >= target 
Here are target and points as an example, input to the code """

target = 11
points = [5, 8, 10, 150, 180]


def minAttmpt(thresh, score):
    i = 1
    count = 1
    while i < len(points)-1:
        if points[i] - points[0] >= thresh or points[i+1] - points[0] >= thresh:
            return count + 1
        else:
            count += 1
            i += 2
    return len(points)


print(minAttmpt(target, points))
