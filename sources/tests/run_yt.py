import os
from yt_dlp import YoutubeDL, utils

def run():

        print("claire")
        # traitement de la video    
        ydl_opts = {
            'format': 'best[height=720]',
            #'format': 'best',
            'outtmpl': "claire_prefixe" + "%(title)s.%(ext)s",
            'restrictfilenames': True,
            'nocheckcertificate': True,
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info('https://www.youtube.com/watch?v=BaW_jenozKc')
                print(info_dict)
                #info_dict = ydl.extract_info(self.ba_url, download=True)
                # sanitize_filename est applique par YoutubeDL quand restrictfilenames=True
                # je le rappelle ici pour conserver le meme nom de fichier
                video_title = utils.sanitize_filename(info_dict.get("fulltitle", None), restricted=True)
                video_ext = info_dict.get('ext', None)
                filename = video_title + '.' + video_ext
                print("the file %s has been downloaded" % filename)

        except Exception as e:
            print("the file could not be dowloaded: " + str(e))
            raise


if __name__ == '__main__':
    run()