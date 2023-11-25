SPEAKER_SRC = "https://peersuma-album-media.s3.amazonaws.com/58/video_low_res_e16706e902d849d4885a0cce8506be86_00041.mp4"SPEAKER_START = 2SPEAKER_LEN = 10NAME = "ALAN RUDT"NAME_START = 3TITLE_START = 400LT_START = 3LTFONT_SRC = "https://templates.shotstack.io/basic/asset/font/manrope-extrabold.ttf"a = 10b = 20if a < b:  NAME = "Pravin Raut"
data = {"b": b, "LT_START": LT_START, "SPEAKER_LEN": SPEAKER_LEN, "NAME": NAME, "SPEAKER_SRC": SPEAKER_SRC, "a": a, "NAME_START": NAME_START, "LTFONT_SRC": LTFONT_SRC, "TITLE_START": TITLE_START, "SPEAKER_START": SPEAKER_START, }

import json
print(json.dumps(data))
