import pyxel

# 【Python】 第2章で学んだクラスの定義
class Game:
    def __init__(self):
        # self.x, self.y がこのゲーム(オブジェクト)の状態
        self.x = 70
        self.y = 50

    # 【Python】 selfを持つメソッド
    def update(self):
        # 【Pyxel】 キー入力判定
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 1

    def draw(self):
        # 【Pyxel】 描画処理
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 10, 10, 7)

# 【Python】 Gameクラスのインスタンス（オブジェクト）を作成
game = Game()

# 【Pyxel】 Pyxelの初期化
pyxel.init(160, 120)

# 【Pyxel/Python】 gameオブジェクトのメソッドをPyxelに渡してループ開始
pyxel.run(game.update, game.draw)
