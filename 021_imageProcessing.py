from PIL import Image

# 打开一张图片
img = Image.open('path_to_your_image.jpg')

# 转换图片的颜色模式
img_gray = img.convert('L')

# 旋转图片
img_rotated = img_gray.rotate(45)

# 保存结果图片
img_rotated.save('path_to_save_image.jpg')

"""
我们将使用PIL库（Python Imaging Library，Python图像处理库）来打开一张图片，转换其颜色模式，旋转图片，然后保存结果。

Image.open('path_to_your_image.jpg')：使用PIL库的Image模块的open函数打开一张图片。你需要替换'path_to_your_image.jpg'为你要打开的图片的路径。
img.convert('L')：使用Image对象的convert方法转换图片的颜色模式。这里我们转换图片为灰度模式，'L'代表灰度模式。
img_gray.rotate(45)：使用Image对象的rotate方法旋转图片。这里我们将图片旋转45度。
img_rotated.save('path_to_save_image.jpg')：使用Image对象的save方法保存图片。你需要替换'path_to_save_image.jpg'为你要保存的图片的路径。
请注意，这只是PIL库的一个非常基础的使用示例。PIL库提供了很多强大的图像处理功能，比如裁剪图片、缩放图片、调整亮度对比度等。
"""