# %% import libraries
import typing
import random
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import json

# %% parameters
boardSize = (100, 100)

# %% define functions
def progressBar(name, value, endvalue, comment="", bar_length = 50, newLine=True):
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent*bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))
    print(f"\r{name} : [{arrow + spaces}]{round(percent*100):4}%  {comment}", end='')
    if (value == endvalue) and newLine:     
        print("\n", end='')

tex_all_ori = cv2.imread("Texture/roguelikeSheet_transparent.png")
tex_all = cv2.cvtColor(tex_all_ori, cv2.COLOR_BGR2RGB)
def getTexture(index : typing.Set) -> np.ndarray:
    row, col = index
    row = row * 17
    col = col * 17
    return tex_all[row:row+16, col:col+16]

def showBoard(board:np.ndarray, blockData):
    imgPlt = np.zeros(shape=(board.shape[0]*16, board.shape[1]*16, 3), dtype=np.uint8)
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            blockName = board[row, col]["currBlock"]
            if blockName is None:
                continue
            textureIdx = blocks[blockName]["texture"]
            textureIdx = random.choice(textureIdx)
            textureIdx = (textureIdx["row"], textureIdx["column"])
            imgPlt[row*16:row*16+16, col*16:col*16+16] = getTexture(textureIdx)
    plt.imshow(imgPlt)
    plt.show()

def saveBoardImg(path:typing.AnyStr, board:np.ndarray, blockData):
    imgPlt = np.zeros(shape=(board.shape[0]*16, board.shape[1]*16, 3), dtype=np.uint8)
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            blockName = board[row, col]["currBlock"]
            if blockName is None:
                continue
            textureIdx = blocks[blockName]["texture"]
            textureIdx = random.choice(textureIdx)
            textureIdx = (textureIdx["row"], textureIdx["column"])
            imgPlt[row*16:row*16+16, col*16:col*16+16] = getTexture(textureIdx)
    imgPlt = cv2.cvtColor(imgPlt, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, imgPlt)

def getAllEdgeDict(allBlocks) -> typing.Set:
    edgeType = dict()
    blockType = dict()
    blockCnt, edgeCnt = 1, 1
    
    for blockName, blockData in allBlocks.items():
        blockType[blockName] = blockCnt
        blockCnt = blockCnt + 1
        for blockEdge in blockData["edgeType"]:
            if edgeType.get(blockEdge, None) is None:
                edgeType[blockEdge] = edgeCnt
                edgeCnt = edgeCnt + 1
    return blockType, edgeType

def updateBoard(pos:typing.Set, boardPossable:np.ndarray, boardresult:np.ndarray):
    pass

if __name__ == "__main__":
# %% readd block config
    blocks = None
    with open("Texture/table.json", mode="r") as blockConfigFile:
        blocks = json.load(blockConfigFile)
    
    blockTypes, edgeTypes = getAllEdgeDict(blocks)

# %% init board
    board = np.empty(shape=boardSize, dtype=object)

    allPossableEdge = [t[0] for t in edgeTypes.items()]
    allPossableBlock = [t[0] for t in blockTypes.items()]
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            newElement = {
                "currBlock" : None,
                "possableBlock" : allPossableBlock,
                "edge" : []
            }
            board[row, col] = newElement

# %% randomly put block
    # randomly pick position
    randPos = (random.randint(0,boardSize[0]-1), random.randint(0,boardSize[1]-1))

    setPos = randPos

    # randomly pick a block
    possableBlocks = []
    for b in list(blockTypes.items()):
        b = b[0]
        possableBlocks.extend([b]*blocks[b]["weight"])
    newBlock = random.choice(possableBlocks)

    settingupTimes = 0
    while(True):
        # set board
        board[setPos] = {
                    "currBlock" : newBlock,
                    "possableBlock" : [],
                    "edge" : blocks[newBlock]["edgeType"]
                }
        settingupTimes = settingupTimes + 1
        progressBar("Calculating", settingupTimes, board.size)
        # if(settingupTimes%20 == 0):
        #     showBoard(board, blocks)
        saveBoardImg(os.path.join("resultImg", f"{settingupTimes:06d}.png"), board, blocks)
        if(settingupTimes >= board.size):
            break


        # pop neighbor possable block
        for edgeIdx, posOffset in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
            posOffset = (setPos[0] + posOffset[0], setPos[1] + posOffset[1])
            if posOffset[0]<0 or posOffset[1]<0 or posOffset[0]>=boardSize[0] or posOffset[1]>=boardSize[1]:
                continue
            currEdge = board[setPos]["edge"][edgeIdx]

            neighborEdgeIdx = (edgeIdx + 2)%4
            newPossableBlock = []
            for possableBlock in board[posOffset]["possableBlock"]:
                possableBlockName = possableBlock
                possableBlock = blocks[possableBlock]
                neighborEdge = possableBlock["edgeType"][neighborEdgeIdx]
                if(neighborEdge=="grass" and currEdge=="grass") or \
                    (neighborEdge=="sea" and currEdge=="sea") or \
                    (neighborEdge=="coastal_R" and currEdge=="coastal_L") or \
                    (neighborEdge=="coastal_L" and currEdge=="coastal_R"):
                    newPossableBlock.append(possableBlockName)
            board[posOffset]["possableBlock"] = newPossableBlock

        #print(board)

        # choice new block
        minPossiblePos = []
        PossibleNum = np.array([[len(block["possableBlock"]) for block in row] for row in board], dtype=np.uint32)
        PossibleNum[PossibleNum==0] = 9999

        minIdx = np.argmin(PossibleNum)
        minVal = PossibleNum.flatten()[minIdx]
        if((PossibleNum==minVal).sum() == 1):
            setPos = (minIdx//boardSize[0], minIdx%boardSize[0])
            possableBlocks = []
            for b in board[setPos]['possableBlock']:
                possableBlocks.extend([b]*blocks[b]["weight"])
            newBlock = random.choice(possableBlocks)
        else:
            posY, posX = np.where(PossibleNum==minVal)
            randIdx = random.randint(0, posY.size-1)
            setPos = ( posY[randIdx], posX[randIdx] )
            possableBlocks = []
            for b in board[setPos]['possableBlock']:
                possableBlocks.extend([b]*blocks[b]["weight"])
            newBlock = random.choice(possableBlocks)

showBoard(board, blocks)