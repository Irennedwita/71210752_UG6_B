#Irenne Dwita Natalia
#71210752
#UG6

class NodeMahasiswa:
    def __init__(self,nama,ipk,n=None,p=None):
        self._element = nama
        self._ipk = ipk
        self._next = n
        self._prev = p

    def getNama(self):
        return self._element

    def getIpk(self):
            return self._ipk

    def setNama(self,nama):
        self._element = nama

    def setIpk(self,ipk):
        self._ipk = ipk

class DoubleLList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self._size

    def addElementTail(self,nama,ipk):
        new = NodeMahasiswa(nama,ipk)
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            self.tail._next = new
            new._prev = self.tail
            self.tail = new
            print("data masuk ke tail")
        self.size = self.size + 1

    def deleteLast(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            hapus = self.tail
            self.tail = self.tail._prev
            hapus._prev = None
            self.tail._next = None
            del hapus
        print("# Data", hapus,"terhapus #")
        self.size = self.size-1

    def printDescending(self):
        print("=" * 5, "Print Descending", "=" * 5)
        bantu = self.head
        while bantu != None:
            print("=" * 30)
            print("Nama\t: ", bantu.getNama())
            print("IPK\t: ", bantu.getIpk())
            bantu = bantu._next
        print()

    # def rataIpk():
DLLNC = DoubleLList()
DLLNC.addElementTail('Shalom',3.9)
DLLNC.addElementTail('Nabilla',3.8)
DLLNC.addElementTail('Kurniadi',3.7)
DLLNC.addElementTail('Harris',3.6)
DLLNC.printDescending()
DLLNC.deleteLast()
DLLNC.printDescending()     
