from datetime import datetime

from peewee import *

db = SqliteDatabase('limoonad_video_editior.db')


class BaseModel(Model):
    class Meta:
        database = db


class WhatToDo(BaseModel):
    id = BigAutoField()
    done = IntegerField(index=True)  # done==0 ==>should do something, done==1 ==>successfull, done==2 ==>error
    toDo = IntegerField()  # 1==> add logo, 2==> addTwoVideo, 3==>delete something
    video_Address = TextField()
    target_Address = TextField(null=True)
    videoStart_Address = TextField(default='start.mp4', null=True)
    logo_Address = TextField(default='logo.png', null=True)
    renderSize = TextField(null=True)
    mustDeleteVideo = IntegerField()
    mustDeleteRenderedVideo = IntegerField()
    errorMessage = TextField(null=True)
    insertDateTime = DateTimeField(default=datetime.now())  # tarikhe eijaade record
    doneDateTime = DateTimeField(null=True, default=datetime.now())  # tarikhe pardaazesh
    upId = IntegerField(null=True)
    logoX = TextField(default='right')  # right | left
    logoY = TextField(default='bottom')  # top | bottom
    logoX_margin = IntegerField(null=True)
    logoY_margin = IntegerField(null=True)
    LogoResizeHeight=IntegerField(default=0)
    VideoStartFrom=DecimalField(default=0)
    VideoEnd=DecimalField(default=0)
    VideoFramePerSecond=IntegerField(default=20)
    VideoHasNose=IntegerField(default=0)
    SetLogoOpacity=IntegerField(default=0)
    AudioBitRate=TextField(default='96k')
    RenderSpeed=TextField(default='slow')
    IsRendering=IntegerField(default=0)
    TryToRender=IntegerField(default=0)
db.connect()
db.create_tables([WhatToDo])
