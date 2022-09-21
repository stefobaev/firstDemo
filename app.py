from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media2.giphy.com/media/12BYUePgtn7sis/200w.webp?cid=ecf05e474ensr8gxejm52coatbwyp3c1alkdwfv3i2lovxe8&rid=200w.webp&ct=g",
    "https://media4.giphy.com/media/MdA16VIoXKKxNE8Stk/200w.webp?cid=ecf05e474ensr8gxejm52coatbwyp3c1alkdwfv3i2lovxe8&rid=200w.webp&ct=g",
    "https://media4.giphy.com/media/11ZSwQNWba4YF2/giphy.webp?cid=ecf05e474ensr8gxejm52coatbwyp3c1alkdwfv3i2lovxe8&rid=giphy.webp&ct=g",
    "https://media0.giphy.com/media/bPCwGUF2sKjyE/200.webp?cid=ecf05e47i8incow9d6dch1a7pnnw06w208g79h8qoy4bavom&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/D0EjguuQzYr9m/200w.webp?cid=ecf05e47r36jkok066qq79sxlmk2i7tcaxpog0fa1jq2sngw&rid=200w.webp&ct=g",
    "https://media0.giphy.com/media/YQitE4YNQNahy/200w.webp?cid=ecf05e47qrxawngsq825qmftsuj1fuhav9duolodr0emu8v2&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/DHBGehJ3FSZEygszX3/200w.webp?cid=ecf05e47bi4v04bnmn2sy2ar12dn3fqxs1aio7bjf0k3q3yp&rid=200w.webp&ct=g",
    "https://media4.giphy.com/media/MdA16VIoXKKxNE8Stk/200w.webp?cid=ecf05e47km1b9ply8g1vhpinmgc8jc270hj1zaiwaacwavsc&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/kGFqR72PTCTujo6uKE/200.webp?cid=ecf05e47gltoexyydpugg63ry5leky62i1y69yhlbm2aog1s&rid=200.webp&ct=g"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
