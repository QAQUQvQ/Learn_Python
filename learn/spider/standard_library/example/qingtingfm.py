# https://www.52pojie.cn/thread-974724-1-1.html
# http://www.jikexiazai.cn/qtfm.html

import requests
import json

vvid = "161294"


# 获取该页视频列表
def GetPageJson(vid):
    apiurl = "https://i.qingting.fm/wapi/channels/" + vid + "/programs/page/1/pagesize/50"
    # 总页码
    pnum = 1
    r = requests.get(apiurl)
    rejson = r.json()
    # 视频总个数
    pagecount = rejson["total"]

    # 获取总页数
    if (pagecount % 50 == 0):
        pnum = pagecount // 50
    else:
        pnum = pagecount // 50 + 1
    # 下载不排序，为了排序
    v_i = 1
    for n in range(1, pnum):
        gurl = "https://i.qingting.fm/wapi/channels/" + vid + "/programs/page/" + str(n) + "/pagesize/50"
        gjson = requests.get(gurl).json()
        for d in gjson["data"]:
            # 循环获取名称 ,收听地址
            vname = d["name"]
            vpath = d["file_path"]
            print(vname + "--" + vpath)
            # 下载文件
            furl = "https://od.qingting.fm/" + vpath
            fname = str(v_i).zfill(3) + vname + ".m4a"
            fdown = requests.get(furl)
            with open(fname, "wb") as code:
                code.write(fdown.content)
            v_i = v_i + 1;


# 主函数入口
if __name__ == '__main__':
    GetPageJson(vvid)