# 五子棋应用自动化测试项目

## 项目简介
这是一个使用uiautomator2库实现的五子棋应用自动化测试项目，用于自动连接设备、启动应用、等待特定界面出现并执行点击操作。

## 目录结构
```
UI/
├── src/             # 源代码目录
│   ├── tests/       # 测试脚本
│   ├── config/      # 配置文件（如坐标参数等）
│   ├── resources/   # 资源文件
│   │   └── screenshots/ # 截图资源
│   └── utils/       # 工具函数
├── venv/            # Python虚拟环境
└── README.md        # 项目说明文件
```

## 环境准备
1. 确保已创建Python虚拟环境：`venv`
2. 安装必要的依赖：`uiautomator2`

## 运行测试
在项目根目录下执行以下命令运行测试：
```bash
python3.12 -m src.tests.app_launch_test
```

## 文件说明
- **src/tests/app_launch_test.py**: 应用启动测试主脚本
- **src/config/coordinates.py**: 存放界面元素坐标参数
- **src/resources/screenshots/**: 存放测试过程中使用的截图资源

## 注意事项
1. 确保测试设备已连接并开启USB调试模式
2. 测试前请确保`uiautomator2`库已正确安装
3. 运行测试时需要使用模块方式运行，以便正确解析相对导入路径