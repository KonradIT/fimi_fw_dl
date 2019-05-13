from parser import FimiFW
from util import download

FimiFW = FimiFW()
fwList = FimiFW.parseAll()

for index, fwItem in enumerate(fwList):
    print("%s - %s" % (" " + str(index) if len(str(index)) == 1 else index,
                       fwItem.get("system")))
firmwareToDL = int(input("Enter FW: "))
filename = fwList[firmwareToDL].get("key") + "-" + fwList[firmwareToDL].get(
    "system") + ".bin"
download(filename, fwList[firmwareToDL].get("url"))
