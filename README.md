## select-watershed-qgis-plugin


`select-watershed-qgis-plugin` 為基於 Python 開發的 QGIS 3 插件。  
`select-watershed-qgis-plugin` is a Python plugin for QGIS 3 that can select upstream watershed from your specific point.  
![image](https://github.com/cvb14795/select-watershed-qgis-plugin/blob/master/img/Result.png)  

## 功能  
* 使用者可指定河道圖層，即可自由點選圖層上的任意座標，再指定集水區圖層，程式將會選擇出該點上游集水區範圍。
* 提供可將選擇的圖徵輸出為.shp檔案，且將輸出之圖層自動加入至QGIS軟體內之功能。
* 本QGIS插件經由該軟體介接 GDAL/OGR（地理空間數據庫）API，以提供計算集水區範圍並選取之功能。

## 介面概覽 
![image](https://github.com/cvb14795/select-watershed-qgis-plugin/blob/master/img/PluginUI.png)

## 需求軟體
* QGIS ver.3.4 以上或更新版本  
QGIS version 3.4 or later  

## 如何使用
1. 至上方連結 **Code > Download ZIP** 下載本插件之ZIP檔，或[點擊此處][]以下載  
2. 在QGIS 3中，上方工具列選擇 **外掛程式(Plugins) > Manage and Install Plugins... > Install from ZIP**，選擇剛剛下載的ZIP檔案位置  


## 注意事項
* 本插件 **並沒有** 發佈在QGIS插件庫，因此無法由QGIS插件庫搜尋，只能從 **Install from ZIP** 方式安裝。  
* 若安裝後在 **已安裝** 清單中找不到該插件，請將 **外掛程式 > 設定 > 顯示實驗性質的外掛程式** 打勾。  

 [點擊此處]: https://github.com/cvb14795/select-watershed-qgis-plugin/archive/master.zip "DownloadZIP"
