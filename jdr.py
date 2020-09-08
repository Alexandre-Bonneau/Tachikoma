import xml.etree.ElementTree as ET

import random
# def new_dic(str,dex,con,intel,vol,cha):
#     dic = {}
#     dic["for"]=str
#     dic["con"]=con
#     dic["int"]=intel
#     dic["vol"]=vol
#     dic["cha"]=cha
#     dic["dex"]=dex
#     return dic
#
# def dod():
#     dic = {}
#     dic[227088616575205376] = new_dic(4,8,6,10,6,10) #alex
#     dic[482938921416654849] = new_dic(4,8,6,10,6,10) #alex_smurf
#     dic[182932585477963777] = new_dic(6,10,8,10,6,4) #julien
#     dic[203621493773434890] =new_dic(10,10,8,6,6,4)  #leyla
#     dic[244204902316769281] = new_dic(8,10,6,8,8,4) #paulin
#     dic[42] = new_dic(4,8,4,12,4,10) #pf
#
#     return dic

class data_stat(object):

    def __init__(self, xml ='jdr_stat.xml' ):
        self.xml = xml
        self.tree = ET.parse(xml)
        self.root = self.tree.getroot()
        self.fdp_list = self.root.findall('fdp')
        self.stat_dic = self.init_dic()

        # self.names_list = [k1.get('pname') for k1 in self.fdp_list]
        # self.names_list.sort()
    def init_dic(self):
        dic={}
        dic["for"]="force"
        dic["con"]="constitution"
        dic["int"]="intelligence"
        dic["vol"]="volonte"
        dic["cha"]="charisme"
        dic["dex"]="dexterite"
        return dic
    def get_fdp(self,str, type = "id"):
        if type == "id":
            for i in self.fdp_list:
                if eval(str) in eval(i.get('idlist')):
                    return i
        if type == "name":
            for i in self.fdp_list:
                if str.lower() == i.get('name'):
                    return i
        if type == "pname":
            for i in self.fdp_list:
                if str.lower() == i.get('pname'):
                    return i
        return None

    def get_stat(self,fdp,stat):
        return fdp.find('stat').get(stat)

    def roll(self,str_,id):
        str_list=[i for i in str_.split(' ') if len(i)>0]
        ret = []
        fdp = self.get_fdp(str(id))
        for i in str_list:
            val = self.get_stat(fdp,i)
            ret.append("le Jet de " + self.stat_dic[i]+"("+val+") de "+fdp.get('pname')+" est :")
            rd =random.randint(1,eval(val))
            ret.append(str(rd))
        return ret
#
# a=data_stat()
# b=a.roll("for int","42")
# print(b)


    #
    # def get_song_name(self,playlist):
    #     return [i.get('name') for i in playlist.findall('song')]
    #
    # def get_song_addr(self,playlist):
    #     return [i.get('address') for i in playlist.findall('song')]
    #
    # def add_song(self,playlist,songname,songaddr):
    #     p = self.get_playlist(playlist)
    #     if p == None:
    #         return "No such playlist"
    #     if not (songname in self.get_song_name(p)):
    #         new=ET.SubElement(p,'song')
    #         new.set('address',songaddr)
    #         new.set('name',songname)
    #         # p.append(new)
    #         self.tree.write(self.xml)
    #         self.__init__(self.xml)
    #         return None
    #     else:
    #         return "There is already such song name"
    # def add_playlist(self,pname):
    #     if not (pname in self.plist_name):
    #         new=ET.SubElement(self.root,'playlist')
    #         new.attrib = {'pname' : pname}
    #         self.root.append(new)
    #         self.tree.write(self.xml)
    #         self.__init__(self.xml)
    #         return None
    #     else:
    #         return "There is already such playlist"
