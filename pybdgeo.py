# coding=utf-8
import hashlib
import json
import urllib
from urllib import quote

import requests


class BaiduGEO(object):
    def __init__(self, ak, sk):
        self.ak = ak
        self.private_sk = sk

    def _get_sn(self, queryStr):
        """
        以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
        对queryStr进行转码，safe内的保留字符不转换
        在最后直接追加上yoursk
        md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
        最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0

        :param queryStr: /geocoder/v2/?address=xxx&output=json&ak=l6jsgxmG2EKIG6Om4kih7Tu9VjLTUIWB
        :return:
        """
        encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
        rawStr = encodedStr + self.private_sk
        return hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()

    def get_longitude_latitude(self, address):
        """
        在线文档：http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding

        :param address: 地址如：深圳弘法寺
        :return:
        """

        queryStr = '/geocoder/v2/?address=%s&output=json&ak=%s' % (address, self.ak)
        print queryStr

        sn = self._get_sn(queryStr)
        quote_address = quote(address)  # 由于本文城市变量为中文，为防止乱码，先用quote进行编码
        url = 'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s&sn=%s' % (quote_address, ak, sn)

        r = requests.get(url)
        ret = json.loads(r.content)  # 对json数据进行解析
        return ret

    def get_address(self, longitude, latitude):
        """
        在线文档：http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding

        http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=39.934,116.329&output=json&pois=1&ak=您的ak //GET请求
        :param longitude: 经度如：114.18798340633165
        :param latitude: 维度如：22.583631511145345
        :return:
        """

        queryStr = '/geocoder/v2/?location=%s,%s&output=json&ak=%s' % (latitude, longitude, self.ak)
        sn = self._get_sn(queryStr)
        url = 'http://api.map.baidu.com%s&sn=%s' % (queryStr, sn)
        r = requests.get(url)
        ret = json.loads(r.content)  # 对json数据进行解析
        return ret


if __name__ == '__main__':
    ak = 'l6jsgxmG2EKIG6Om4kih7Tu9VjLTUIWB'
    sk = '5C06x25Tm9etBO2qX76FgmjS6ZERqlpz'
    bdgeo = BaiduGEO(ak, sk)

    # test for get_longitude_latitude
    address = '深圳弘法寺'
    res = bdgeo.get_longitude_latitude(address)
    print res

    # test for get_address
    longitude = 114.1879
    latitude = 22.5836
    res2 = bdgeo.get_address(longitude, latitude)
    print res2
