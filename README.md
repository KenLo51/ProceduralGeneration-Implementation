# Python-ProceduralGeneration-Implementation

# 1. L System
## 1.1. 各符號定義
| 符號 | 說明 |
| :-: | :- |
| F | 向前移動並繪製線段 |
| f | 向前移動且不繪製線段 |
| + | 左轉ø度 |
| - | 右轉ø度 |
| \| | 迴轉(180度) |
| [ | 將目前位置與方向存入堆疊 |
| ] | 從堆疊中取出位置與方向 |
| # | 增加未來將繪製線段粗細 |
| ! | 漸少未來將繪製線段粗細 |

## 1.2. 運行結果
| 1.                                                                   | 2.                                                                     | 3.Quadratic Gosper     |
| :-----                                                               | :-----                                                                 | :----- |
|<img src="https://i.imgur.com/741k9KB.gif" width="300" height="300" />| <img src="https://i.imgur.com/R3Geuaw.gif" width="300" height="300" /> | <img src="https://i.imgur.com/mrg5yzQ.gif" width="300" height="300" /> |
| Axiom : F+F+F+F                                                      | Axiom : X                                                              | Axiom : -YF |
| ø = 90                                                               | ø = 20                                                                 | ø = 90 |
| F --> F+F-F-FF+F+F-F                                                 | F --> FF                                                               | X --> XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF- |
| --                                                                   | X --> F[+X]F[-X]+X                                                     | Y --> +FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY |
## 1.3. 參考資料
> [1] [Paul Bourke. L-System User Notes](http://paulbourke.net/fractals/lsys/)  
> [2] [實作 L-system](https://openhome.cc/Gossip/P5JS/Lsystem.html)  

# 2. Wave Function Collapse  
## 2.2. 運行結果  
patterns :  
![](https://i.imgur.com/3Vbmikm.png)  
progress result :  
[<img src="https://i.imgur.com/ANwduBv.gif" width="300" height="300"/>](https://imgur.com/Y6ITcXB)  

## 2.3. 參考資料  
> [1] [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)  
> [2] [Roguelike/RPG pack](https://www.kenney.nl/assets/roguelike-rpg-pack)   
> [3] [Martin Donald. Superpositions, Sudoku, the Wave Function Collapse algorithm.](https://www.youtube.com/watch?v=2SuvO4Gi7uY&ab_channel=MartinDonald)  

# 3. Fractals  
