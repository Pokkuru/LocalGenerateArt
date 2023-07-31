# LocalGenerateNFT Project

ローカルで動作する Excel ファイルとアイテム（画像ファイル）群を読み込んで、  
構成通りのアイテムを一括作成するプロジェクト。

## 環境

- OS
  - Windows11 22H2
  - macOS Monterey 12.6
- Docker Desktop
  - Version 4.14.1

## 使用方法

### 環境構築

#### Docker desktop をインストールする

[Docker desktopダウンロードページ](https://www.docker.com/products/docker-desktop/ "Docker desktop ダウンロードページ")

#### コンテナをビルドして立ち上げる

コンテナというプログラムの実施環境を準備する。  
以下の作業は、WindowsならPowerShell、Macならターミナルでコマンドを打って実施する。  

```bash
cd <プロジェクトルートのパス>
# コンテナのビルド（2～3分程度かかる）
docker-compose build
# コンテナの立ち上げ
docker-compose up -d
```

### データ設置

事前に`./data/`に元の画像フォルダ、アイテムの設定が書いてある Excel ファイルを置いておく  
LocalGenerateNFT  
&emsp;└─data  
&emsp;&emsp;&emsp; ├─cnt01  
&emsp;&emsp;&emsp; ├─cnt02  
&emsp;&emsp;&emsp; ├─cnt03  
&emsp;&emsp;&emsp; ├─cnt04  
&emsp;&emsp;&emsp; ├─cnt05  
&emsp;&emsp;&emsp; └─items.xlsm

### 実行

```bash
# 透かしがない画像が生成されるデフォルト構成の実行コマンド
docker exec -it art-generator_local_app python LocalGenerateNFT/app.py
```

プロジェクトルートの`output`にタイムスタンプがフォルダ名になった出力がされる。  
中身に生成された画像ファイルがある。

#### コマンドオプション

| オプション                              | 説明                   | デフォルト値    |
| --------------------------------------- | ---------------------- | --------------- |
| --image_path \<IMAGE_PATH\>             | 画像のフォルダのルート | data/           |
| --excel_path \<EXCEL_PATH\>             | エクセルファイルのパス | data/items.xlsm |
| --enable_watermark \<ENABLE_WATERMARK\> | 透かしを入れるか否か   | False           |

例 1: 以下のコマンドでは透かしが入った画像が生成される

```bash
docker exec -it art-generator_local_app python LocalGenerateNFT/app.py --enable_watermark True
```

例 2: 以下のコマンドでは透かしがない画像が生成される

```bash
docker exec -it art-generator_local_app python LocalGenerateNFT/app.py --enable_watermark False
```

## 注意事項  

ベータ版のため動作不良を起こす可能性あり、  
不具合は状況やデータを添付してお問い合わせください。
