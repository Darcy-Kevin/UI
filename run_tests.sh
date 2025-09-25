#!/bin/bash

# 清理旧的Allure结果和报告
echo "清理旧的Allure测试结果和报告..."
if [ -d "allure-results" ]; then
  rm -rf allure-results/*
  echo "  已清理allure-results目录"
fi
if [ -d "allure-report" ]; then
  rm -rf allure-report/*
  echo "  已清理allure-report目录"
fi

# 激活虚拟环境
echo "
激活Python虚拟环境..."
source venv/bin/activate

# 检查是否有连接的Android设备
echo -e "\n检查连接的Android设备..."
adb devices
if [ $? -ne 0 ]; then
  echo "警告: 未找到adb命令。请确保已安装Android Platform Tools。"
  echo "可以使用 'brew install android-platform-tools' 安装。"
fi

# 运行测试脚本
echo -e "\n运行Gobang应用测试（使用pytest和Allure）..."
venv/bin/pytest src/tests/app_launch_test.py --alluredir=allure-results

# 显示测试结果信息
echo -e "\n测试完成。测试结果保存在allure-results目录中。"

# 检查allure命令是否可用并自动打开报告
if command -v allure &> /dev/null; then
  echo "
Allure命令可用，自动打开测试报告..."
  echo "注意：如果浏览器没有自动打开，请手动使用以下命令查看详细的测试报告："
  echo "  allure serve allure-results"
  # 启动allure服务查看报告
  allure serve allure-results &
else
  echo "注意: 未找到allure命令。要查看详细报告，请先安装allure："
  echo "  brew install allure"
  echo "安装完成后，使用 'allure serve allure-results' 查看报告。"
fi

# 提示用户查看现有的报告
if [ -d "allure-report" ]; then
  echo -e "\n您也可以直接打开allure-report/index.html文件查看之前生成的报告。"
fi