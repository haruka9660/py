import os
import shutil

def organize_files_by_type(directory):
    for filename in os.listdir(directory):
        # 获取文件的完整路径
        file_path = os.path.join(directory, filename)

        # 如果是文件，我们才处理
        if os.path.isfile(file_path):
            # 分割文件名和扩展名
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension[1:]

            # 如果扩展名存在，则按照扩展名分类文件
            if file_extension:
                destination_folder = os.path.join(directory, file_extension)
                
                # 如果目标文件夹不存在，则创建该文件夹
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                # 将文件移动到目标文件夹
                shutil.move(file_path, destination_folder)

# 使用方法
organize_files_by_type("/path/to/your/directory")

"""
这个脚本将遍历指定的目录，根据文件的扩展名创建子文件夹，并将相应的文件移动到对应的子文件夹中。

os库提供了很多操作文件和目录的函数。shutil库则提供了文件操作的高级接口，如复制和删除文件。
organize_files_by_type(directory)函数的参数directory是我们要整理的目录。
os.listdir(directory)返回指定目录下所有文件和文件夹的名称。我们遍历这个列表，对每个文件进行处理。
os.path.join(directory, filename)函数连接目录和文件名，得到文件的完整路径。
os.path.isfile(file_path)检查给定路径是否是一个文件。如果是，我们才处理它。
os.path.splitext(filename)函数分割文件名和扩展名。file_extension = file_extension[1:]这一行代码是为了去掉扩展名前面的点。
如果文件有扩展名，我们就创建一个名为该扩展名的子文件夹，然后将文件移动到那个文件夹。
os.path.exists(destination_folder)检查目标文件夹是否存在。如果不存在，我们使用os.makedirs(destination_folder)创建它。
最后，shutil.move(file_path, destination_folder)将文件移动到目标文件夹。
注意：这段代码将会移动你指定的文件夹中的文件，所以在运行之前最好备份一下数据，防止发生意外。
"""