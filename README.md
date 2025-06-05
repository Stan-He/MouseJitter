# MouseJitter

一个简单的鼠标抖动程序，每120秒自动移动一次鼠标，防止系统进入休眠状态。

## 功能特点

- 显示120秒倒计时
- 自动移动鼠标
- 简洁的图形界面
- 可独立运行的exe文件

## 安装步骤

### 方法一：直接运行exe文件（推荐）

1. 在 `dist` 文件夹中找到 `MouseJitter.exe`
2. 双击运行即可
3. 如果遇到Windows安全中心拦截，可以选择"仍要运行"

### 方法二：从源码运行

1. 确保已安装Python 3.x
2. 安装必要的依赖：
   ```bash
   pip install pyinstaller
   ```
3. 运行程序：
   ```bash
   python MouseJitter.py
   ```

### 方法三：自行打包exe

1. 安装PyInstaller：
   ```bash
   pip install pyinstaller
   ```
2. 打包程序：
   ```bash
   pyinstaller --onefile --windowed MouseJitter.py
   ```
3. 在 `dist` 文件夹中找到生成的 `MouseJitter.exe`

## 使用说明

1. 运行程序后会显示一个带有倒计时的窗口
2. 倒计时从120秒开始，每秒更新一次
3. 当倒计时到0时，程序会自动移动鼠标
4. 移动鼠标后，倒计时会重新开始
5. 点击"Exit"按钮可以退出程序

## 注意事项

1. 程序需要管理员权限才能移动鼠标
2. 如果遇到权限问题，请右键exe文件，选择"以管理员身份运行"
3. 程序运行时可能会被Windows安全中心拦截，这是正常的
4. 生成的exe文件可以直接复制到其他Windows电脑上运行，不需要安装Python环境

## 系统要求

- Windows 10/11
- 不需要安装Python环境（如果使用exe文件）
- 需要管理员权限（用于移动鼠标）

## 常见问题

1. Q: 程序无法移动鼠标？
   A: 请尝试以管理员身份运行程序

2. Q: Windows安全中心拦截程序？
   A: 这是正常的，因为这是一个自制的程序。您可以选择"仍要运行"

3. Q: 如何修改倒计时时间？
   A: 需要修改源代码中的 `self.countdown = 120` 值，然后重新打包 