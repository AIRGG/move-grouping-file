import os, shutil, random, string

todir = {
	"ziprar":['.zip','.rar','.7z'],
	"jpgjpegpng":['.jpg','.jpeg','.png'],
	"cdraieps":['.cdr','.ai','.eps','.svg'],
	"office":['.doc','.docx','.xls','.xlsx','.ppt','.pptx'],
	"pdf":['.pdf'],
	"fontsetc":['.ttf','.otf','.woff','.woff2'],
	"videosmusic":['.mp4','.mkv','.avi','.mpeg','.wmp','.3gp','.mp3','.wav','.aac','.ogg','.wma'],
}
desktopPath = os.path.expanduser('~\\Desktop')
for x in os.listdir(desktopPath):
	for y in todir:
		if x.lower().endswith(tuple(todir[y])):
			try:
				if os.path.exists(os.path.join(desktopPath, y)):
					# y+= f"{y}(1)"
					tmpx = x.split(".")
					extx = tmpx[1]
					nmfl = tmpx[0]
					y = f"{y}\\{nmfl} {''.join(random.sample(string.ascii_letters, 8))}.{extx}"
				shutil.move(os.path.join(desktopPath, x), os.path.join(desktopPath, y))
				print("[DONE]",x)
			except Exception as e:
				print("[FAILED]",e)
# for x in os.listdir():
# 	if x.endswith(".zip") or x.endswith(".rar") or x.endswith(".pptx"):
# 		shutil.move(x, os.path.join(os.getcwd(), todir))
# 		print("[DONE]",x)