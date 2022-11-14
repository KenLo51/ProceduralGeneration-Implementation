# Python-ProceduralGeneration-Implementation

# 1. L System
## 各符號定義
| 符號 | 說明 |
| :-: | :- |
| F | 向前移動並繪製線段 |
| f | 向前移動且不繪製線段 |
| + | 左轉ø度 |
| - | 右轉ø度 |
| | | 迴轉(180度) |
| [ | 將目前位置與方向存入堆疊 |
| ] | 從堆疊中取出位置與方向 |
| # | 增加未來將繪製線段粗細 |
| ! | 漸少未來將繪製線段粗細 |

## 運行結果
| 1.                                                                   | 2.                                                                     | 3.Quadratic Gosper     |
| :-----                                                               | :-----                                                                 | :----- |
|<img src="https://i.imgur.com/741k9KB.gif" width="300" height="300" />| <img src="https://i.imgur.com/R3Geuaw.gif" width="300" height="300" /> | <img src="https://i.imgur.com/mrg5yzQ.gif" width="300" height="300" /> |
| Axiom : F+F+F+F                                                      | Axiom : X                                                              | Axiom : -YF |
| ø = 90                                                               | ø = 20                                                                 | ø = 90 |
| F --> F+F-F-FF+F+F-F                                                 | F --> FF                                                               | X --> XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF- |
| --                                                                   | X --> F[+X]F[-X]+X                                                     | Y --> +FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY |
## 參考資料
> [Paul Bourke. L-System User Notes](http://paulbourke.net/fractals/lsys/)  
> [實作 L-system](https://openhome.cc/Gossip/P5JS/Lsystem.html)
> 
# 2. Fractals
