def init(params: dict):
    return None


def run(data: dict, func=None) -> bool:
    if data["objectPath"] == "01.psd":
        return True
    return False


def teardown():
    pass
