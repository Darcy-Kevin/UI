# 五子棋应用UI自动化测试项目

## 项目简介
这是一个使用uiautomator2和pytest框架实现的五子棋应用UI自动化测试项目，用于自动连接设备、启动应用、处理隐私弹窗、验证登录界面元素、查找并点击特定功能按钮（如人工客服、上传日志等），并生成详细的测试报告。

## 目录结构
```
UI/
├── src/             # 源代码目录
│   ├── tests/       # 测试脚本
│   │   ├── app_launch_test.py        # 应用启动测试脚本
│   │   └── app_logininterface_test.py # 登录界面测试脚本
│   ├── config/      # 配置文件
│   │   └── coordinates.py            # 界面元素坐标参数
│   ├── resources/   # 资源文件
│   │   └── screenshots/ # 测试过程中生成的截图
│   └── utils/       # 工具函数
│       ├── screenshot_utils.py       # 截图工具
│       └── time_utils.py             # 时间工具
├── requirements.txt # 项目依赖列表
├── run_tests.sh     # 测试运行脚本
├── venv/            # Python虚拟环境
└── README.md        # 项目说明文件
```

## 环境准备
1. 确保已安装Python 3.12或更高版本
2. 创建Python虚拟环境：`python3 -m venv venv`
3. 激活虚拟环境：`source venv/bin/activate`
4. 安装必要的依赖：`pip install -r requirements.txt`
5. 确保Android设备已连接并开启USB调试模式
6. 安装Android Platform Tools（如未安装）：`brew install android-platform-tools`
7. 可选：安装Allure命令行工具（用于查看测试报告）：`brew install allure`

## 项目依赖
项目主要依赖如下：
- pytest==7.3.1 - Python测试框架
- allure-pytest==2.13.2 - 测试报告生成工具
- setuptools>=65.0.0 - Python包管理工具
- pillow>=9.0.0 - 图像处理库
- weditor==0.6.4 - UI元素查看工具
- uiautomator2 - Android UI自动化测试库

## 运行测试
### 方法一：使用脚本运行（推荐）
在项目根目录下执行以下命令运行测试：
```bash
chmod +x run_tests.sh
./run_tests.sh
```
此脚本会自动清理旧的测试结果，激活虚拟环境，检查设备连接状态，运行测试并尝试打开Allure报告。

### 方法二：手动运行测试
在激活虚拟环境后，可以使用以下命令手动运行特定测试：
```bash
# 运行所有测试
pytest src/tests/

# 运行特定测试文件
pytest src/tests/app_logininterface_test.py

# 运行测试并生成Allure报告数据
pytest src/tests/app_logininterface_test.py --alluredir=allure-results

# 查看Allure报告（需要安装allure命令行工具）
allure serve allure-results
```

## 测试功能说明
### 测试文件详解
- **src/tests/app_launch_test.py**: 应用启动测试脚本，负责验证应用能否正常启动并显示主界面。

- **src/tests/app_logininterface_test.py**: 登录界面测试脚本，包含以下主要测试用例：
  - 验证登录页面显示
  - 处理隐私弹窗
  - 查找并截图人工客服按钮（`resourceId="com.duole.wuziqihd:id/dl_sdk_acc_login_service"`）
  - 查找并截图上传日志按钮（`resourceId="com.duole.wuziqihd:id/dl_sdk_acc_login_upload_log"`）
  - 点击人工客服按钮并验证客服页面

### 工具类详解
- **src/utils/screenshot_utils.py**: 提供截图相关的工具函数，用于捕获测试过程中的界面状态。
- **src/utils/time_utils.py**: 提供时间相关的工具函数，如获取当前时间戳等。

## 测试报告说明
项目使用Allure生成详细的测试报告，报告包含以下内容：
- 测试执行状态（通过/失败）
- 测试步骤详情
- 测试过程中的截图
- 错误信息和异常堆栈（如有）

## 注意事项
1. 确保测试设备已连接并开启USB调试模式
2. 运行测试前请确保所有依赖已正确安装
3. 测试脚本使用了fixture机制管理设备连接，确保测试环境的一致性
4. 测试过程中会自动处理隐私弹窗（点击"同意"按钮）
5. 测试失败时会自动截图并保存到resources/screenshots目录
6. 如需修改测试配置，可编辑src/config/coordinates.py文件中的相关参数