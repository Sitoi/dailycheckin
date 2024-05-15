from dailycheckin import CheckIn
import os
import json


class TestNotice(CheckIn):
    name = "通知测试"

    def __init__(self, check_item):
        self.check_item = check_item

    def main(self):
        return f"测试内容{self.check_item}"


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("TestNotice", [])[0]
    print(TestNotice(check_item=_check_item).main())
