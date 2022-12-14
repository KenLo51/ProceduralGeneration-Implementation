# ProceduralGeneration-Implementation
  
# 1. L System
以固定公理(Axiom)繪製圖形，並限制遞迴深度執行其餘規則。

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
  
<img src="https://i.imgur.com/Vplz1ah.png" width="300" height="156" />
3D L-System

## 1.3. 參考資料
> [1] [Paul Bourke. L-System User Notes](http://paulbourke.net/fractals/lsys/)  
> [2] [實作 L-system](https://openhome.cc/Gossip/P5JS/Lsystem.html)  

# 2. Wave Function Collapse 
初始於任一位置隨機選取一可用pattern。  
接著在每次放置新pattern後，依據此pattern可接受邊界更新剩餘尚未決定pattern位置的可能pattern集合。  
每次更新後若有任一位置的可能pattern集合為空則須回復動作，並將先前決定的一pattern踢出其位置中的集合。  

## 2.1. 運行結果  
patterns :  
![](https://i.imgur.com/3Vbmikm.png)  
progress result :  
[<img src="https://i.imgur.com/ANwduBv.gif" width="300" height="300"/>](https://imgur.com/Y6ITcXB)  

## 2.2. 參考資料  
> [1] [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)  
> [2] [Roguelike/RPG pack](https://www.kenney.nl/assets/roguelike-rpg-pack)   
> [3] [Martin Donald. Superpositions, Sudoku, the Wave Function Collapse algorithm.](https://youtu.be/2SuvO4Gi7uY)  

# 3. Fractals  
# 4. Perlin Noise  
使亂數平滑，當x代入亂數函數時應與x-1、x+1相關。  
使用6t<sup>5</sup>-15t<sup>4</sup>+10<sup>3</sup>計算內插，其中因微分後於兩端(t=0 or 1)為0使其變化連續。  
  
計算1維Perlin Noise如下:  
w = 6t<sup>5</sup>-15t<sup>4</sup>+10<sup>3</sup>  
Noise(x) = (t)\*(1-w)\*y<sub>0</sub> + (1-t)\*(w)\*y<sub>1</sub>  
<img src="https://i.imgur.com/b8C8au4.png"/>  

## 4.1. 運行結果  
| 1. 1D Perlin Noise with 1 and 2 octaves | 2. 2D Perlin Noise | 3. 3D Perlin Noise |
| :- | :- | :- |
| <img src="https://i.imgur.com/VD1WELA.png" width="320" height="240" /> | <img src="https://i.imgur.com/8xB6bh6.png" width="320" height="240" /> | <img src="https://i.imgur.com/RGsVfSM.gif" width="320" height="240" /> |  

## 4.2. 參考資料  
> [1] [I.5: Perlin Noise - The Nature of Code](https://youtu.be/8ZEMLCnn8v0)  
> [2] [柏林噪聲(Perlin Noise): (科普)創造亂中有序大自然的魔法](https://youtu.be/NqqIT_-xJls)  
> [3] [Perlin Noise: A Procedural Generation Algorithm](https://rtouti.github.io/graphics/perlin-noise-algorithm)  
> [4] [Perlin噪聲](https://zh.m.wikipedia.org/zh-tw/Perlin%E5%99%AA%E5%A3%B0)
  
# 5. Worley Noise
於空間中隨機放置數個點，每點數值依據其與最近隨機放置點的距離決定。  
## 5.1. 運行結果  
<img src="https://i.imgur.com/w0p9PDX.png" width="320" height="240" />  
Worley Noise with 10 random points  

## 5.2. 應用  
### 5.2.1 Volumetric Cloud
使用Worley Noise與Perlin Noise製作隨機分布體積雲。  
<img src="https://i.imgur.com/kwRM7Wa.png" width="400" height="233" /> <img src="https://i.imgur.com/ScDVJBv.png" width="400" height="233" />  
## 5.3. 參考資料  
> [1] [Coding Adventure: Clouds](https://youtu.be/4QOcCGI6xOU)  
