# Python-ProceduralGeneration-Implementation

# 1. L System

## 運行結果
Axiom : F+F+F+F <br>
F --> F+F-F-FF+F+F-F <br>
ø = 90 <br>

| 1.                                                                   | 2.                                                                     | 3.Quadratic Gosper     |
| :-----                                                               | :-----                                                                 | :----- |
|<img src="https://i.imgur.com/741k9KB.gif" width="300" height="300" />| <img src="https://i.imgur.com/R3Geuaw.gif" width="300" height="300" /> | <img src="https://i.imgur.com/mrg5yzQ.gif" width="300" height="300" /> |
| Axiom : F+F+F+F                                                      | Axiom : X                                                              | Axiom : -YF |
| ø = 90                                                               | ø = 20                                                                 | ø = 90 |
| F --> F+F-F-FF+F+F-F                                                 | F --> FF                                                               | X --> XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF- |
| --                                                                   | X --> F[+X]F[-X]+X                                                     | Y --> +FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY |
## 參考資料
> [Paul Bourke. L-System User Notes](http://paulbourke.net/fractals/lsys/)

# 2. Fractals
