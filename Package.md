## 打包方式

### 所需工具

- Node.js: [Installation](https://nodejs.org/zh-tw/download/)
  - 測試是否安裝成功: 在 cmd 下 `node -v` 看是否有出現版本
- yarn: [Installation](https://yarnpkg.com/latest.msi)
  - 測試是否安裝成功: 在 cmd 下 `yarn --version` 看是否有出現版本
- Python: [Installation](https://www.python.org/downloads/)
- WiX: [Installation](https://github.com/wixtoolset/wix3/releases/tag/wix3112rtm)
  - 安裝後請將 Program Files 下的 `Wix Toolset\bin` 加入環境變數的 Path 中 (打包會需要用到 bin 資料夾內的`candle.exe`及`light.exe`)

### 打包步驟

- 若有編輯.py 檔
  - 先將根目錄的`main_py.spec`，`src\python\__pycache__\*`，`build\main_py\*`，`dist\*`這四個刪除
  - 下 `pyinstaller -F .\src\python\main_py.py`將 python 打包成`.exe`檔
- `yarn install`安裝 nodeJS 所需的 package
- `yarn run make`會打包所有 code，最後`.exe`路徑會放在`out\make\wix\x64`內
