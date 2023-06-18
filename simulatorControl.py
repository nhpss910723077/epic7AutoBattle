import time

class SimulatorControl:
    def __init__(self, imageControl, simulator, language):
        self.imageControl = imageControl
        self.simulator = simulator
        self.language = language
        
        if language == "en":
            self.language = "en_"
        else:
            self.language = "ch_"
        
        self.imgFolder = "images/"
        
        self.start = self.imgFolder + self.language + "start.png"
        self.restart = self.imgFolder + self.language + "restart.png"
        self.end = self.imgFolder + self.language + "end.png"
        self.confirm = self.imgFolder + self.language + "confirm.png"
        self.leaf = self.imgFolder + self.language + "leaf.png"
        self.leaf_btn = self.imgFolder + self.language + "leaf_btn.png"
        self.expedition = self.imgFolder + self.language + "expedition.png"
        self.expedition_btn = self.imgFolder + self.language + "expedition_btn.png"

    # 搜尋結束戰鬥圖
    def matchEnd(self):
        match_result = self.imageControl.matchImages(self.end, 0.9)
        if(match_result != None):
            print("搜尋結束戰鬥圖成功");
            x = 300
            y = 300
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            
            # 確認是否有遠征
            checkExpeditionTime = 0
            while not self.checkExpedition():
                if checkExpeditionTime >= 5:
                    return True
                else:
                    time.sleep(3)
                    checkExpeditionTime += 1
            
            return True
        
        else:
            print("搜尋結束戰鬥圖失敗");
            return False
            
    # 確認是否有遠征 有則點選確認
    def checkExpedition(self):
        match_result = self.imageControl.matchImages(self.expedition, 0.9)
        if(match_result != None):
            print("搜尋遠征成功");
            match_result = self.imageControl.matchImages(self.expedition_btn, 0.9)
            if(match_result != None):
                print("搜尋遠征按鈕成功");
                x, y = match_result
                self.simulator.click(x, y)
                self.simulator.click(x, y)
                self.simulator.click(x, y)
                
                return True
            else:
                print("搜尋遠征按鈕失敗");
                return False
        
        else:
            print("搜尋遠征失敗");
            return False
            time.sleep(99999)
            
    # 點選確認按鈕
    def clickConfirm(self):
        # 確認是否有確認按鈕
        match_result = self.imageControl.matchImages(self.confirm, 0.9)
        if(match_result != None):
            print("搜尋確認按鈕成功");
            x, y = match_result
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            self.simulator.click(x, y)
                
            return True
            
        else:
            print("搜尋確認按鈕失敗");
            return False
            time.sleep(99999)
            
    # 點選重新開始按鈕
    def clickRestart(self):
        # 確認是否有重新開始按鈕
        match_result = self.imageControl.matchImages(self.restart, 0.9)
        if(match_result != None):
            print("搜尋重新開始按鈕成功");
            x, y = match_result
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            self.simulator.click(x, y)
                
            return True
            
        else:
            print("搜尋重新開始按鈕失敗");
            return False
            time.sleep(99999)
            
    # 點選開始按鈕
    def clickStart(self):
        # 確認是否有開始按鈕
        match_result = self.imageControl.matchImages(self.start, 0.9)
        if(match_result != None):
            print("搜尋開始按鈕成功");
            x, y = match_result
            self.simulator.click(x, y)
            self.simulator.click(x, y)
            self.simulator.click(x, y)
                
            return True
            
        else:
            print("搜尋開始按鈕失敗");
            return False
            time.sleep(99999)
            
    # 確認是否需要購買體力
    def checkLeft(self):
        checkLeftTime = 0
        while checkLeftTime <= 5:
            match_result = self.imageControl.matchImages(self.leaf, 0.9)
            if(match_result != None):
                print("搜尋葉子畫面成功");
                match_result = self.imageControl.matchImages(self.leaf_btn, 0.9)
                if(match_result != None):
                    print("搜尋購買體力按鈕成功");
                    x, y = match_result
                    self.simulator.click(x, y)
                    self.simulator.click(x, y)
                    self.simulator.click(x, y)
                    
                    return True
                else:
                    print("搜尋購買體力按鈕失敗");
                    checkLeftTime += 1
            
            else:
                print("搜尋葉子畫面失敗");
                checkLeftTime += 1

            time.sleep(3)
            
        return False