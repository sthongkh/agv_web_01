import pymongo
import re


class MongoDB():

    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://planagv:27017/")
        self.mydb = self.myclient["agv"]

    def check_user(self, user, pw):
        col = self.mydb["user"]
        query = {"user_name" : "{}".format(user)}
        res = col.find_one(query)["password"]
        return (pw == res)

    def get_all_station(self, plant):
        col = self.mydb["station"]
        query = {"plant" : plant}
        res = col.find(query)
        sid = []
        sname = []
        for x in res:
            sid.append(x["station_id"])
            sname.append(x["station_name"])

        return sname

    def get_queue(self, agv_num):
        col = self.mydb["queue_agv_{}".format(agv_num)]
        query = {}
        res = col.find(query)
        data = []

        for x in res:
            data.append(x)

        return data

    def get_agv_num(self):
        res = self.mydb.list_collection_names()
        ret = []
        for i in res:
            match = re.match("queue_agv_(\d+)", i)
            if match:
                ret.append("{:02d}".format(int(match.group(1))))

        return ret

    def test(self, text):
        print(text)







