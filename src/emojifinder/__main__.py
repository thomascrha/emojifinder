"""Search for emojis on emojifinder.com"""
from typing import List
import http.client
import json
import argparse
from dataclasses import dataclass


@dataclass
class Emoji:
    code: str
    name: str
    fitz_modified: int
    gender_modified: int
    profession: int
    default_emoji_style: str
    score: str
    cnt: int
    version: str
    display_code: str
    display_mode: str
    rank: int



class EmojiFinder:
    def __init__(self, male: bool = False, female = False):
        self.connection = http.client.HTTPSConnection("emojifinder.com")
        self.gender = "false"

        if male:
            self.gneder = "m"

        if female:
            self.gender = "f"

        self.headers = {
            "cookie": f"fitz=false; gender={self.gender}",
            "User-Agent": "", # i get a 500 if i dont set this
        }

    def search(self, terms: List[str]) -> List[Emoji]:
        self.connection.request("GET", f"/*/ajax.php?action=search&query={'+'.join(terms)}", headers=self.headers)
        response = self.connection.getresponse()
        data = json.loads(response.read().decode("utf-8"))

        emojis = []
        for emoji in data["results"]:
            emojis.append(Emoji(**{k.lower(): v for k, v in emoji.items()}))

        return emojis


def main(args):
    finder = EmojiFinder()
    emojis = finder.search(args.terms)
    print(emojis)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="+", help="Search terms")

    parser.add_argument("--male", "-m", action="store_true", help="Set the emojis sex as Male")
    parser.add_argument("--female", "-f", action="store_true", help="Set the emojis sex as Female")

    parser.add_argument("--dark", action="store_true", help="Set the emojis skin tone as Dark")
    parser.add_argument("--medium-dark", action="store_true", help="Set the emojis skin tone as Medium Dark")
    parser.add_argument("--medium", action="store_true", help="Set the emojis skin tone as Medium")
    parser.add_argument("--medium-light", action="store_true", help="Set the emojis skin tone as Medium Light")
    parser.add_argument("--light", action="store_true", help="Set the emojis skin tone as Light")
    parser.add_argument("--no-skin-tone", action="store_true", help="Set the emojis skin tone as None")

    args = parser.parse_args()
    main(args)

