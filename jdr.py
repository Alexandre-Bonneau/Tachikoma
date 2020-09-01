def new_dic(str,dex,con,intel,vol,cha):
    dic = {}
    dic["for"]=str
    dic["con"]=con
    dic["int"]=intel
    dic["vol"]=vol
    dic["cha"]=cha
    dic["dex"]=dex
    return dic

def dod():
    dic = {}
    dic[227088616575205376] = new_dic(4,8,6,10,6,10) #alex
    dic[1482938921416654849] = new_dic(4,8,6,10,6,10) #alex_smurf
    dic[182932585477963777] = new_dic(4,4,4,4,4,4) #julien
    dic[203621493773434890]=new_dic(4,4,4,4,4,4)  #leyla
    dic[244204902316769281] = new_dic(4,4,4,4,4,4) #paulin
    return dic
