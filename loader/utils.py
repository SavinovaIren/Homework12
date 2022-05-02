from extentions import *

def save_pic(picture):
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in ["jpeg", "png", "jpg"]:
        raise WrongImageType('Неверный формат файла')
    picture_ = f'uploads/images/{picture.filename}'
    picture.save(picture_)
    return picture_
