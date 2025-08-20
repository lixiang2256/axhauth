#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的SQL Server连接测试脚本
使用纯Python实现，不依赖复杂的C扩展
"""

import socket
import struct
import hashlib
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def test_connection(server, port, database, username, password):
    """
    测试SQL Server连接
    """
    print(f"测试连接到: {server}:{port}")
    print(f"数据库: {database}")
    print(f"用户名: {username}")
    
    try:
        # 尝试TCP连接
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((server, port))
        sock.close()
        
        if result == 0:
            print("✓ TCP连接成功")
            return True
        else:
            print("✗ TCP连接失败")
            return False
            
    except Exception as e:
        print(f"✗ 连接测试失败: {e}")
        return False

def main():
    """主函数"""
    print("SQL Server连接测试工具")
    print("=" * 50)
    
    # 数据库配置
    config = {
        'server': 'axhauth.soulapp.cn',
        'database': 'ab_Axh',
        'username': 'userdev',
        'password': '4zLqgfw7TrthXZnZCRNUfgl6g0659ELo',
        'port': 1433
    }
    
    # 测试连接
    success = test_connection(
        config['server'], 
        config['port'], 
        config['database'], 
        config['username'], 
        config['password']
    )
    
    if success:
        print("\n基本网络连接正常，可以尝试其他解决方案")
    else:
        print("\n网络连接失败，请检查:")
        print("1. 服务器地址是否正确")
        print("2. 端口是否开放")
        print("3. 网络连接是否正常")
        print("4. 防火墙设置")

if __name__ == "__main__":
    main() 