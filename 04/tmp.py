import pyxel

def update():
    print("update")

def draw():
    print("draw")

pyxel.init(160, 120)
pyxel.run(update, draw)
