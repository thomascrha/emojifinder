from typing import List
import http.client

conn = http.client.HTTPSConnection("emojifinder.com")

headers = {
    "cookie": "fitz=1F3FB; gender=m",
    "User-Agent": "",
}


class EmojiFinder:

    def __init__(self):
        self.connection = http.client.HTTPSConnection("emojifinder.com")

        self.headers = {
            "cookie": "fitz=1F3FB; gender=m",
            "User-Agent": "",
        }

    def search(self, terms: List[str]) -> http.client.HTTPResponse:
        self.connection.request("GET", f"/*/ajax.php?action=search&query={'+'.join(terms)}", headers=headers)

        return self.connection.getresponse()


def main():
    finder = EmojiFinder()
    res = finder.search(["tool"])
    data = res.read()
    print(data.decode("utf-8"))


if __name__ == "__main__":
    main()

