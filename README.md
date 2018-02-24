# pygeography
提供计算地理距离、经纬度转换等功能的python工具包   
pydistance = calculate distance between two point...   
pybdgeo = trans between address and longitude&latitude base on lbsyun.baidu.com...   

# env
```
python==2.7+
```

# usage for pydistance
```
# coding=utf-8

import pydistance

long1 = 22.0
lat1 = 131.2

long2 = 24.0
lat2 = 110.2

dis1 = pydistance.get_distance_haversine(long1, lat1, long2, lat2)
dis2 = pydistance.get_distance_wgs84(long1, lat1, long2, lat2)

print "haversine = %s(m)" % dis1
print "WGS-84 = %s(m)" % dis2

```
result:
```
haversine = 2337555.38881(m)
WGS-84 = 2340173.99386(m)
```

# usage for pybdgeo
```
from pywhere.pybdgeo import BaiduGEO

"""
申请ak和sk网址：http://lbsyun.baidu.com/apiconsole/key/update?app-id=10601098
当然你也可是使用博主的，不过每天大概是6k次上限。
自己申请很快的，五分钟...

Apply baidu ak and sk URL: http://lbsyun.baidu.com/apiconsole/key/update?App-id=10601098
Of course, you can use bloggers', but the daily limit is about 6k times.
Apply for it quickly, five minutes ...
"""
ak = 'l6jsgxmG2EKIG6Om4kih7Tu9VjLTUIWB'
sk = '5C06x25Tm9etBO2qX76FgmjS6ZERqlpz'

bdgeo = BaiduGEO(ak, sk)

print("==========test for get_longitude_latitude==========")
address = '深圳弘法寺'
res = bdgeo.get_longitude_latitude(address)
pprint.pprint(res)

print("==========test for get_address==========")
longitude = 114.1879
latitude = 22.5836
res2 = bdgeo.get_address(longitude, latitude)
pprint.pprint(res2)

```
result:
```
==========test for get_longitude_latitude==========
{
    "status": 0,
    "result": {
        "location": {
            "lng": 114.18798340633165,
            "lat": 22.583631511145345
        },
        "precise": 0,
        "confidence": 25,
        "level": "旅游景点"
    }
}
==========test for get_address==========
{
    "status": 0,
    "result": {
        "location": {
            "lng": 114.18789999999998,
            "lat": 22.583600000474092
        },
        "formatted_address": "广东省深圳市罗湖区苏铁四路",
        "business": "莲塘",
        "addressComponent": {
            "country": "中国",
            "country_code": 0,
            "country_code_iso": "CHN",
            "country_code_iso2": "CN",
            "prov": "深圳市",
            "city_level": 2,
            "district": "罗湖区",
            "town": "",
            "adcode": "440303",
            "street": "苏铁四路",
            "street_number": "",
            "direction": "",
            "distance": ""
        },
        "pois": [],
        "roads": [],
        "poiRegions": [
            {
                "direction_desc": "内",
                "name": "深圳仙湖植物园",
                "tag": "旅游景点"
            }
        ],
        "sematic_descript": "深圳仙湖植物园内,弘法寺附近31米",
        "cityCode": 340
    }
}

```
