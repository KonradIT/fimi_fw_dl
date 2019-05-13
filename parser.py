import requests
import json
from pprint import pprint


class FimiFW():
    def __init__(self):
        self.uri = "https://fimiapp-server-frankfurt.mi-ae.com.de/v3/firmware/getFirmwareDetail"
        self.request = json.loads(requests.get(self.uri).text)

    def parseAll(self):
        firmwareCatalog = []
        for firmware in self.request["data"]:

            firmwareCatalog.append({
                "system":
                firmware.get("sysNameI18N").get("en_US"),
                "url":
                firmware.get("fileUrl"),
                "key":
                firmware.get("fileEncode"),
                "model":
                firmware.get("model")
            })
        return firmwareCatalog

    def get(self, system):
        for item in self.parseAll():
            if item["system"] == system:
                return item
