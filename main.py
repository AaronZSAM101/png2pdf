import os
from PIL import Image
import fitz  # PyMuPDF

def pngs_to_pdf(folder_path, output_pdf_path):
    # 获取文件夹中所有的PNG文件
    png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
    
    # 按文件名排序
    png_files.sort()
    
    # 创建一个PDF文档
    pdf_document = fitz.open()
    
    for png_file in png_files:
        # 打开每一个PNG文件
        img_path = os.path.join(folder_path, png_file)
        img = Image.open(img_path).convert('RGB')
        
        # 保存临时PDF文件
        temp_pdf_path = img_path.replace('.png', '.pdf')
        img.save(temp_pdf_path, 'PDF', resolution=100.0)
        
        # 将临时PDF文件加载到文档中
        temp_pdf_document = fitz.open(temp_pdf_path)
        pdf_document.insert_pdf(temp_pdf_document)
        temp_pdf_document.close()  # 确保在删除之前关闭临时PDF文件
        
        # 删除临时PDF文件
        os.remove(temp_pdf_path)
    
    # 保存合并后的PDF文件
    pdf_document.save(output_pdf_path)
    pdf_document.close()
    
    print(f"所有PNG文件已合并为: {output_pdf_path}")

# 指定文件夹路径和输出PDF文件路径
folder_path = r'C:\Users\Capta\Desktop\png2pdf\关于调整及新辟北京进近管制扇区的批复'
output_pdf_path = r'C:\Users\Capta\Desktop\png2pdf\关于调整及新辟北京进近管制扇区的批复.pdf'

# 调用函数进行合并
pngs_to_pdf(folder_path, output_pdf_path)