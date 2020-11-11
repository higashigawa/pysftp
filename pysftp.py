# -*- encoding: utf-8 -*-

import os
import paramiko


"""
hostname = '__sshサーバー名__'
port = '__使用ポート__' 
username = '__sshユーザー名__'
password = '__パスワード__'
local_path = '__ローカルパス__'
local_file = '__ローカルファイル名__'
target_path = '__ターゲットパス__'
"""


def get_data(hostname, port, username, password, local_path, local_file, target_path,):

    # 初期化
    client = None
    sftp_connection = None

    try:
        # サーバーに接続
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        sftp_connection = client.open_sftp()
        sftp_connection.chdir(target_path)
        
        # カレントディレクトリのファイル一覧を取得
        file_list = sftp_connection.listdir()
        for target_file in file_list:
            print(target_file)

            # ファイル名設定
            localfile = local_path + local_file
            remotefile = target_path + target_file
    
            # ファイルを取得
            sftp_connection.get(remotefile, localfile)
    
            # ファイルを消去
            sftp_connection.remove(remotefile)
    
    except:
        raise
    
    finally:
        # 終了処理
        if client:
            client.close()
        if sftp_connection:
            sftp_connection.close()


def main():
    get_data(hostname, port, username, password, local_path, local_file, target_path,):


if name == '__main__':
    main()            
