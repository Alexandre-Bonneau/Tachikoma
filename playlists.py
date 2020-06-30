import xml.etree.ElementTree as ET
class playlist(object):

    def __init__(self, xml ='playlists.xml' ):
        self.xml = xml
        self.tree = ET.parse(xml)
        self.root = self.tree.getroot()
        self.plist = self.root.findall('playlist')
        self.plist_name = [k1.get('pname') for k1 in self.plist]
        self.plist_name.sort()

    def get_playlist(self,str):
        for i in self.plist:
            if i.get('pname') == str:
                return i
        return None

    def get_song_name(self,playlist):
        return [i.get('name') for i in playlist.findall('song')]

    def get_song_addr(self,playlist):
        return [i.get('address') for i in playlist.findall('song')]

    def add_song(self,playlist,songname,songaddr):
        p = self.get_playlist(playlist)
        if p == None:
            return "No such playlist"
        if not (songname in self.get_song_name(p)):
            new=ET.SubElement(p,'song')
            new.set('address',songaddr)
            new.set('name',songname)
            # p.append(new)
            self.tree.write(self.xml)
            self.__init__(self.xml)
            return None
        else:
            return "There is already such song name"
    def add_playlist(self,pname):
        if not (pname in self.plist_name):
            new=ET.SubElement(self.root,'playlist')
            new.attrib = {'pname' : pname}
            self.root.append(new)
            self.tree.write(self.xml)
            self.__init__(self.xml)
            return None
        else:
            return "There is already such playlist"

#a = playlist()
#a.add_playlist("test3")
#a.add_song("test3","test","eeokeko")
#"print(a.get_playlist("test1").attrib)
