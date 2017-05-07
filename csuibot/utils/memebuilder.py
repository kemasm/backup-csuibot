import requests as r


class MemeBuilder:

    def __init__(self, top, bottom):
        self.webservice = "https://api.imgflip.com/caption_image?"
        self.template_id = "&template_id=14859329"
        self.username = "&username=drinkinwater1000"
        self.password = "&password=vivafasilkom"
        self.top = "&text0=" + top
        self.bottom = "&text1=" + bottom

    def build_meme(self):
        param = self.template_id + self.username + self.password + self.top + self.bottom
        res = r.post(self.webservice + param)
        return res.json()
