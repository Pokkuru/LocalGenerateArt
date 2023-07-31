from PIL import Image
import os
import random
import csv
from .ExcelEdit import ExcelEdit
import glob
import os

WATERMARK_IMAGE_PATH = "./template/sample_image_01.png"
WATERMARK_IMAGE_HEIGHT = 850
WATERMARK_IMAGE_WIDTH = 850

class Generator:
    def __init__(self):
        self.watermark_image_generated = False
        self.watermark_image = Image.open(WATERMARK_IMAGE_PATH)

    def SetWatermarkImage(self, img):
        self.watermark_image = img

    def GetWatermarkImage(self):
        return(self.watermark_image)

    def MakeWatermarkImage(self, img_shape):
        parts_image = Image.open(WATERMARK_IMAGE_PATH)
        result_image = Image.new("RGBA", img_shape, (255, 255, 255, 0))
        currentX = 0
        currentY = 0
        if(img_shape[0] < WATERMARK_IMAGE_WIDTH or img_shape[1] < WATERMARK_IMAGE_HEIGHT):
            if(img_shape[0] < img_shape[1]):
                parts_image = parts_image.resize((img_shape[0], img_shape[0]))
            else:
                parts_image = parts_image.resize((img_shape[1], img_shape[1]))
        while currentY < img_shape[1]:
            while currentX < img_shape[0]:
                result_image.paste(parts_image, (currentX, currentY))
                currentX += WATERMARK_IMAGE_WIDTH
            currentY += WATERMARK_IMAGE_HEIGHT
        return result_image

    def OverlapWatermarkImage(self, baseImage):
        if self.watermark_image_generated is False:
            self.SetWatermarkImage(
                self.MakeWatermarkImage(
                    baseImage.size))
            self.watermark_image_generated = True
        resultImage = Image.alpha_composite(
            baseImage, self.GetWatermarkImage())
        return(resultImage)

    def ImageGeneratorWithList(
            self,
            file_prefix,
            img_objs,
            src_folders,
            dest_folder_name,
            enable_watermark):
        mex_items = len(img_objs)
        source_files = {}

        for folder_name in src_folders:
            source_files[folder_name] = {}
            files = glob.glob(f"./{file_prefix}{folder_name}/*")
            for file_name in files:
                stem = os.path.basename(file_name)
                source_files[folder_name][stem] = Image.open(file_name)

        # ベース空画像オブジェクトの設定
        base_image_path = f"{file_prefix}{src_folders[0]}/{img_objs[0][1]}"
        first_img = Image.open(base_image_path)
        base_image_obj = Image.new("RGBA", first_img.size, (255, 255, 255, 0))
        
        # リストの構成情報から画像生成
        image_file_name = ""
        for item_idx, item_parts in enumerate(img_objs):
            image_obj = base_image_obj.copy()
            for file_idx, item_name in enumerate(item_parts):
                if file_idx == 0:
                    # indexが0は出力ファイル名
                    image_file_name = item_name
                else:
                    # indexが1以上はlayer<index-1>のアイテムのファイル名
                    overlap_image = source_files[src_folders[file_idx - 1]][item_name]
                    image_obj = Image.alpha_composite(image_obj, overlap_image)

            # 透かし処理
            if enable_watermark:
                image_obj = self.OverlapWatermarkImage(image_obj)

            # 保存処理
            image_obj.save(f"./output/{dest_folder_name}/{image_file_name}")
        return()
