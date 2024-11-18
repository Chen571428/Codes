#!/bin/bash

# 递归解压所有zip文件
function unzip_recursive() {
    find . -type f -name "*.zip" | while read -r zip_file; do
        echo "解压 $zip_file"
        unzip -o "$zip_file" -d "${zip_file%.zip}"
        # 删除原始的zip文件
        rm -f "$zip_file"
        # 递归处理解压后的目录
        unzip_recursive "${zip_file%.zip}"
    done
}

# 开始递归解压
unzip_recursive