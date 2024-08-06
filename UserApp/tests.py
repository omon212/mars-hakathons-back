# import os
# from PIL import Image
# from rembg import remove
#
# # Rasmlar joylashgan papka yo'li
# input_folder = 'images/'
# output_folder = 'converted_images/'
#
# # Agar chiqish papkasi mavjud bo'lmasa, uni yaratish
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
# # Papkadagi barcha fayllarni ko'rib chiqish
# for filename in os.listdir(input_folder):
#     if filename.lower().endswith(('.jpg', '.jpeg')):
#         # Faylni ochish
#         with Image.open(input_folder + filename) as img:
#             # Rasmni PNG formatiga o'zgartirish va vaqtinchalik saqlash
#             img.save(output_folder + filename[:-4] + '.png', 'PNG')
#
#             # Fonni olib tashlash
#             with open(output_folder + filename[:-4] + '.png', 'rb') as f:
#                 input_image = f.read()
#             output_image = remove(input_image)
#
#             # Natijani saqlash
#             with open(output_folder + filename[:-4] + '_nobg.png', 'wb') as out:
#                 out.write(output_image)
#
#             # Vaqtinchalik .png faylni o'chirib tashlash
#             os.remove(output_folder + filename[:-4] + '.png')
