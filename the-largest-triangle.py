def largestTriangleArea(points):
    result = 0.0
    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for k in range(j + 1, len(points)):
                result = max(result,
                             0.5 * abs(points[i][0] * points[j][1] +
                                       points[j][0] * points[k][1] +
                                       points[k][0] * points[i][1] -
                                       points[j][0] * points[i][1] -
                                       points[k][0] * points[j][1] -
                                       points[i][0] * points[k][1]))
    return result


def main():


if __name__ == '__main__':
    main()