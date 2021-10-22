from datetime import datetime, timedelta
from os import remove, path, makedirs, chdir
import sys
dir_path = path.dirname(path.realpath(__file__))
chdir(dir_path)
import moviepy.editor as mp
from models import WhatToDo

def close_clip(vidya_clip):
    # noinspection PyBroadException
    try:
        vidya_clip.reader.close()
        del vidya_clip.reader
        if vidya_clip.audio is not None:
            vidya_clip.audio.reader.close_proc()
            del vidya_clip.audio
        del vidya_clip
    except Exception:
        # sys.exc_clear()
        pass

def create_dir_if_not_exist(file_address):
    try:
        output_dir_addres = file_address[
                            :job.target_Address.rfind('\\')]  # for windows directory address, for linux use '/'
        if not path.isdir(output_dir_addres):
            makedirs(output_dir_addres)
    except:
        try:
            output_dir_addres = file_address[
                                :job.target_Address.rfind('/')]  # for windows directory address, for linux use '/'
            if not path.isdir(output_dir_addres):
                makedirs(output_dir_addres)
        except:
            pass

#def jus_render(video_address,  output_address,VideoStartFrom,VideoEnd,VideoFramePerSecond,VideoHasNose):
#    create_dir_if_not_exist(output_address)
#    if VideoStartFrom > 0 and VideoEnd > 0:
#        video = mp.VideoFileClip(video_address).subclip(float (VideoStartFrom,VideoEnd))
#    elif VideoStartFrom > 0:
#    	video = mp.VideoFileClip(video_address).subclip(float (VideoStartFrom))
#    elif VideoEnd > 0:
#        video = mp.VideoFileClip(video_address).subclip(float (0,VideoEnd))
#    else:
#    	video = mp.VideoFileClip(video_address)
#    video.write_videofile(output_address,codec='libx264',audio_codec='aac',fps=VideoFramePerSecond)
#    close_clip(video)


def add_water_mark(video_address, margin, position, logo_address, output_address, LogoResizeHeight,VideoStartFrom,VideoEnd,VideoFramePerSecond,VideoHasNose,SetLogoOpacity,AudioBitRate,RenderSpeed,TryToRender):
    create_dir_if_not_exist(output_address)
    print(video_address)
    FpsSource="fps"
    if TryToRender == 1:
        FpsSource="tbr"
    if VideoStartFrom > 0 and VideoEnd > 0:
        video = mp.VideoFileClip(video_address,fps_source=FpsSource).subclip(float (VideoStartFrom),float (VideoEnd))
    elif VideoStartFrom > 0:
    	video = mp.VideoFileClip(video_address,fps_source=FpsSource).subclip(float (VideoStartFrom))
    elif VideoEnd > 0:
        video = mp.VideoFileClip(video_address,fps_source=FpsSource).subclip(float (0),float (VideoEnd))
    else:
    	video = mp.VideoFileClip(video_address)
    if SetLogoOpacity<101	and	SetLogoOpacity>-1:
        if LogoResizeHeight == 0:
            logo = (mp.ImageClip(logo_address)
                .set_duration(video.duration)
                .margin(top=margin[0], right=margin[1], bottom=margin[0], left=margin[1],
                        opacity=0)
                .set_opacity(float(SetLogoOpacity/100))
                .set_pos((position[0], position[1])))
        else:
            logo = (mp.ImageClip(logo_address)
                .set_duration(video.duration)
                .resize(height=LogoResizeHeight) # if you need to resize...
                .margin(top=margin[0], right=margin[1], bottom=margin[0], left=margin[1],
                        opacity=0)
                .set_opacity(float(SetLogoOpacity/100))
                .set_pos((position[0], position[1])))
        final = mp.CompositeVideoClip([video, logo])
        var_audio_bitrate=AudioBitRate
        if AudioBitRate=='0k':
            var_audio_bitrate=None
        else:
            var_audio_bitrate=AudioBitRate
        if VideoFramePerSecond == 0:
            VideoFramePerSecond = None
        elif VideoFramePerSecond > 0 and VideoFramePerSecond < 18:
            VideoFramePerSecond=None
        if VideoFramePerSecond  is  None:
            print('\n  VideoFramePerSecond  is  None')
            final.write_videofile(output_address,codec='libx264',audio_codec='aac',threads=6,logger=None,verbose=False,preset='slow')
        else:
            if var_audio_bitrate is None:
                print('\n  VideoFramePerSecond  is not  None and var_audio_bitrate is')
                final.write_videofile(output_address,codec='libx264',audio_codec='aac',fps=VideoFramePerSecond,threads=6,logger=None,verbose=False,preset='slow')
            else:
                print('\n  VideoFramePerSecond  is not  None and var_audio_bitrate is not')
                final.write_videofile(output_address,codec='libx264',audio_codec='aac',fps=VideoFramePerSecond,threads=6,logger=None,verbose=False,audio_bitrate=var_audio_bitrate,preset='slow')
        close_clip(final)


def add_two_video(video1_address, video2_address, output_address,TryToRender):
    FpsSource="fps"
    if TryToRender==1:
        FpsSource="tbr"
    create_dir_if_not_exist(output_address)
    recorded_video = mp.VideoFileClip(video2_address,fps_source=FpsSource)
    start_video = mp.VideoFileClip(video1_address).resize((recorded_video.size[0], recorded_video.size[1]))
    final_clip = mp.concatenate_videoclips([start_video, recorded_video])
    final_clip.write_videofile(output_address,codec='libx264',audio_codec='aac',threads=6, logger=None,verbose=False,preset='slow')
    close_clip(recorded_video)

# read file to check its on work or not
#
txttorun="isrun.txt"
file1 = open(txttorun,"rt")
statusprogram=file1.readline()
print('\n'+statusprogram)
print(len(statusprogram))
file1.close()
if  len(statusprogram)>6:
    date_time_obj = datetime.strptime(statusprogram, '%Y-%m-%d %H:%M:%S.%f')
    date_time_obj2 = date_time_obj + timedelta(hours=3)
    if datetime.now()>date_time_obj2:
        # do what you want do
        file1 = open(txttorun,"wt")
        file1.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        file1.close()
        print('\n do what you want do')
    else:
        print('\n st exit')
        sys.exit()
else:
    print('\n the file was null')
    file1 = open(txttorun,"wt")
    file1.write('{}'.format(datetime.now()))
    file1.close()
    sys.exit()

# delete rendered video in mode 9
jobs = WhatToDo.filter(toDo=9)
count = jobs.count()
counter = 1
for job in jobs:
    try:
        remove(job.target_Address)
    except FileNotFoundError:
        print(FileNotFoundError)
    counter += 1
# delete record in mode 9
query = WhatToDo.delete().where(WhatToDo.toDo==9)
query.execute()

jobs = WhatToDo.filter(done=0)
count = jobs.count()
counter = 1
for job in jobs:

    if job.toDo == 1:  # add logo
        checkhasbefore  =   WhatToDo.filter(done=0  ,   toDo=2, upId=job.upId)
        if job.videoStart_Address is not None and job.videoStart_Address!=''    and    len(job.videoStart_Address)>1    and    checkhasbefore    is    None:
            print('\n_____________<<JOBAddStartObject: {}/{}>>_____________'.format(counter, count))
            new = WhatToDo(done=0,
                           toDo=2,
                           video_Address=job.target_Address,
                           target_Address=job.target_Address[0:job.target_Address.rfind('.')]
                                          + '_withstart'
                                          + job.target_Address[job.target_Address.rfind('.'):],
                           videoStart_Address=job.videoStart_Address,
                           logo_Address=job.logo_Address,
                           renderSize=job.renderSize,
                           mustDeleteVideo=job.mustDeleteVideo,
                           mustDeleteRenderedVideo=job.mustDeleteRenderedVideo,
                           errorMessage=job.errorMessage,
                           doneDateTime=None,
                           upId=job.upId,
                           logoX=job.logoX,
                           logoY=job.logoY,
                           logoX_margin=job.logoX_margin,
                           logoY_margin=job.logoY_margin,
                           LogoResizeHeight=0)
            new.save()
            job.videoStart_Address=None
            job.save()
            counter += 1

jobs = WhatToDo.filter(done=1)
count = jobs.count()
for job in jobs:
    if job.mustDeleteVideo == 1:
        print('\n_____________<<JOBdelete mustDeleteVideo: {}/{}>>_____________'.format(counter, count))
        try:
            remove(job.video_Address)
            job.mustDeleteVideo = 2
            job.doneDateTime = datetime.now()
            job.save()

        except FileNotFoundError:
            print(FileNotFoundError)
            job.mustDeleteVideo = 3
            job.errorMessage = FileNotFoundError
            job.save()
        counter += 1

    if job.mustDeleteRenderedVideo == 1:
        print('\n_____________<<JOBdelete mustDeleteRenderedVideo: {}/{}>>_____________'.format(counter, count))
        try:
            remove(job.target_Address)
            job.mustDeleteRenderedVideo = 2
            job.doneDateTime = datetime.now()
            job.save()


        except FileNotFoundError:
            print(FileNotFoundError)
            job.mustDeleteRenderedVideo = 3
            job.errorMessage = FileNotFoundError
            job.save()
        counter += 1





jobs = WhatToDo.filter(done=0,IsRendering=0).order_by(WhatToDo.insertDateTime).limit(2)
count = jobs.count()
print("app starting. {} jobs to left".format(count))
for job in jobs:
    print('\n_____________<<JOBaddlogo or start: {}/{}>>_____________'.format(counter, count))
    if job.toDo == 1:  # add logo
        try:
            job.IsRendering=1
            job.save()
            add_water_mark(job.video_Address,
                           [job.logoX_margin, job.logoY_margin],
                           [job.logoX, job.logoY],
                           job.logo_Address,
                           job.target_Address,
                           job.LogoResizeHeight,
                           job.VideoStartFrom,
                           job.VideoEnd,
                           job.VideoFramePerSecond,
                           job.VideoHasNose,
                           job.SetLogoOpacity,
                           job.AudioBitRate,
                           job.RenderSpeed,
                           job.TryToRender)
            job.done = 1
            job.IsRendering=0
            job.doneDateTime = datetime.now()
            job.renderSize = path.getsize(job.target_Address)
            job.save()

        except Exception as e:
            print(e)
            job.IsRendering=0
            job.done = 2
            job.errorMessage = e
            job.save()

    elif job.toDo == 2:  # video_start + video_address
        try:
            job.IsRendering=1
            job.save()
            add_two_video(job.videoStart_Address, job.video_Address, job.target_Address,job.TryToRender)
            job.done = 1
            job.IsRendering=0
            job.doneDateTime = datetime.now()
            job.renderSize = path.getsize(job.target_Address) / 1024 / 1000
            job.save()

        except Exception as e:
            print(e)
            job.IsRendering=0
            job.done = 2
            job.errorMessage = e
            job.save()
    counter+=1
file1 = open(txttorun,"wt")
date_time_now = datetime.now()
date_time_nowm2 = date_time_now + timedelta(minutes=-210)
file1.write('{}'.format(date_time_nowm2))
file1.close()
