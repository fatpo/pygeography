# coding=utf-8
import math
from math import radians, cos, sin, asin, sqrt


def get_distance_haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    haversine算法，计算地球上两点距离...
    :param lon1: 经度1
    :param lat1: 纬度1
    :param lon2: 经度2
    :param lat2: 纬度2
    :return: 距离，单位为 米
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


def get_distance_wgs84(lon1, lat1, lon2, lat2):
    """
    根据https://github.com/googollee/eviltransform，里面的算法：WGS - 84
    :param lon1: 经度1
    :param lat1: 纬度1
    :param lon2: 经度2
    :param lat2: 纬度2
    :return: 距离，单位为 米
    """
    earthR = 6378137.0

    pi180 = math.pi / 180
    arcLatA = lat1 * pi180
    arcLatB = lat2 * pi180
    x = (math.cos(arcLatA) * math.cos(arcLatB) *
         math.cos((lon1 - lon2) * pi180))
    y = math.sin(arcLatA) * math.sin(arcLatB)
    s = x + y
    if s > 1:
        s = 1
    if s < -1:
        s = -1
    alpha = math.acos(s)
    distance = alpha * earthR
    return distance


if __name__ == '__main__':
    long1 = 22.0
    lat1 = 131.2

    long2 = 24.0
    lat2 = 110.2

    print "haversine = %s" % get_distance_haversine(long1, lat1, long2, lat2)
    print "WGS-84 = %s" % get_distance_wgs84(long1, lat1, long2, lat2)

    '''
    结果：
    haversine = 2337555.38881
    WGS-84 = 2340173.99386

    '''
