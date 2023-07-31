import argparse
from Modules.ExcelEdit import ExcelEdit
from Modules.ImageGeneratorLocal import Generator
import datetime
import os


def GetCurrentTime():
    dt_now = datetime.datetime.now()
    return dt_now.strftime('%Y%m%d-%H-%M-%S')


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        '--image_path',
        help='画像のフォルダのルート 例: data/',
        default='data/')
    parser.add_argument(
        '--excel_path',
        help='エクセルファイルのパス 例: data/items.xlsm',
        default='data/items.xlsm')
    parser.add_argument('--enable_watermark',
                       help='透かしを入れるか否か',
                       default=False,
                       type=bool)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    excel_operator = ExcelEdit()
    source_folder_list, items_row_data = excel_operator.LoadExcel(args.excel_path)
    folder_name = GetCurrentTime()
    os.makedirs(f"./output/{folder_name}", exist_ok=True)
    
    generator = Generator()
    generator.ImageGeneratorWithList(args.image_path, items_row_data, source_folder_list, folder_name, args.enable_watermark)


if __name__ == "__main__":
    main()
