# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# 需要UnRAR.exe 或 pip3 install unrar

from pathlib import Path
import sys
import zipfile
import rarfile

def main(inputPath):
    del inputPath[0]
    for folder in inputPath:
        if Path.is_dir(Path(folder)):
            for file in Path(folder).glob('*'):
                if rarfile.is_rarfile(file):
                    rf = rarfile.RarFile(file)
                    fileNameList = []
                    print('Copying: ' + file.name)
                    for eachFile in rf.infolist():
                        if eachFile.is_file():
                            fileNameList.append(eachFile.filename)
                    fileNameList.sort()
                    rf.extract(fileNameList[0], path=folder)
                    if len(fileNameList[0].split('/')) == 1:
                        oldFilePath = Path(folder).joinpath(fileNameList[0])
                        #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[1])
                        coverFolder = Path(folder).joinpath('cover')
                        if not coverFolder.exists():
                            Path.mkdir(coverFolder)
                        newFilePath = Path(coverFolder).joinpath(file.stem + '.' + fileNameList[0].split('.')[-1])
                        Path(oldFilePath).replace(newFilePath)
                    if len(fileNameList[0].split('/')) == 2:
                        oldFilePath = Path(folder).joinpath(fileNameList[0])
                        #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[1])
                        coverFolder = Path(folder).joinpath('cover')
                        if not coverFolder.exists():
                            Path.mkdir(coverFolder)
                        newFilePath = Path(coverFolder).joinpath(file.stem + '.' + fileNameList[0].split('/')[-1].split('.')[-1])
                        Path(oldFilePath).replace(newFilePath)
                        Path.rmdir(Path(folder).joinpath(fileNameList[0].split('/')[0]))
                    if len(fileNameList[0].split('/')) == 3:
                        oldFilePath = Path(folder).joinpath(fileNameList[0])
                        #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[2])
                        coverFolder = Path(folder).joinpath('cover')
                        if not coverFolder.exists():
                            Path.mkdir(coverFolder)
                        newFilePath = Path(coverFolder).joinpath(file.stem + '.' + fileNameList[0].split('/')[-1].split('.')[-1])
                        Path(oldFilePath).replace(newFilePath)
                        tmpPath = Path(folder).joinpath(fileNameList[0].split('/')[0])
                        tmpPath = Path(tmpPath).joinpath(fileNameList[0].split('/')[1])
                        Path.rmdir(tmpPath)
                        Path.rmdir(Path(folder).joinpath(fileNameList[0].split('/')[0]))
                    rf.close()
                if zipfile.is_zipfile(file):
                    zf = zipfile.ZipFile(file)
                    fileNameList = []
                    print('Copying: ' + file.name)
                    for eachFile in zf.infolist():
                        #if zipfile.Path.is_file(eachFile):
                        if not eachFile.is_dir():
                            fileNameList.append(eachFile.filename)
                    fileNameList.sort()
                    zf.extract(fileNameList[0], path=folder)
                    if len(fileNameList[0].split('/')) == 1:
                        oldFilePath = Path(folder).joinpath(fileNameList[0])
                        #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[1])
                        coverFolder = Path(folder).joinpath('cover')
                        if not coverFolder.exists():
                            Path.mkdir(coverFolder)
                        newFilePath = Path(coverFolder).joinpath(file.stem + '.' + fileNameList[0].split('.')[-1])
                        Path(oldFilePath).replace(newFilePath)
                    if len(fileNameList[0].split('/')) == 2:
                        oldFilePath = Path(folder).joinpath(fileNameList[0])
                        #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[1])
                        coverFolder = Path(folder).joinpath('cover')
                        if not coverFolder.exists():
                            Path.mkdir(coverFolder)
                        newFilePath = Path(coverFolder).joinpath(file.stem + '.' + fileNameList[0].split('/')[-1].split('.')[-1])
                        Path(oldFilePath).replace(newFilePath)
                        Path.rmdir(Path(folder).joinpath(fileNameList[0].split('/')[0]))
                    if len(fileNameList[0].split('/')) == 3:
                        oldFilePath = Path(folder).joinpath(fileNameList[0])
                        #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[2])
                        coverFolder = Path(folder).joinpath('cover')
                        if not coverFolder.exists():
                            Path.mkdir(coverFolder)
                        newFilePath = Path(coverFolder).joinpath(file.stem + '.' + fileNameList[0].split('/')[-1].split('.')[-1])
                        Path(oldFilePath).replace(newFilePath)
                        tmpPath = Path(folder).joinpath(fileNameList[0].split('/')[0])
                        tmpPath = Path(tmpPath).joinpath(fileNameList[0].split('/')[1])
                        Path.rmdir(tmpPath)
                        Path.rmdir(Path(folder).joinpath(fileNameList[0].split('/')[0]))
                    zf.close()
        
        if Path.is_file(Path(folder)):
            if rarfile.is_rarfile(folder):
                rf = rarfile.RarFile(folder)
                fileNameList = []
                print('Copying: ' + Path(folder).name)
                for eachFile in rf.infolist():
                    if eachFile.is_file():
                        fileNameList.append(eachFile.filename)
                fileNameList.sort()
                rf.extract(fileNameList[0], path=Path(folder).parent)
                if len(fileNameList[0].split('/')) == 1:
                    oldFilePath = Path(folder).parent.joinpath(fileNameList[0])
                    #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[1])
                    coverFolder = Path(folder).parent.joinpath('cover')
                    if not coverFolder.exists():
                        Path.mkdir(coverFolder)
                    newFilePath = Path(coverFolder).joinpath(Path(folder).stem + '.' + fileNameList[0].split('.')[-1])
                    Path(oldFilePath).replace(newFilePath)
                if len(fileNameList[0].split('/')) == 2:
                    oldFilePath = Path(folder).parent.joinpath(fileNameList[0])
                    #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[1])
                    coverFolder = Path(folder).parent.joinpath('cover')
                    if not coverFolder.exists():
                        Path.mkdir(coverFolder)
                    newFilePath = Path(coverFolder).joinpath(Path(folder).stem + '.' + fileNameList[0].split('/')[-1].split('.')[-1])
                    Path(oldFilePath).replace(newFilePath)
                    Path.rmdir(Path(folder).parent.joinpath(fileNameList[0].split('/')[0]))
                if len(fileNameList[0].split('/')) == 3:
                    oldFilePath = Path(folder).parent.joinpath(fileNameList[0])
                    #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[2])
                    coverFolder = Path(folder).parent.joinpath('cover')
                    if not coverFolder.exists():
                        Path.mkdir(coverFolder)
                    newFilePath = Path(coverFolder).joinpath(Path(folder).stem + '.' + fileNameList[0].split('/')[-1].split('.')[-1])
                    Path(oldFilePath).replace(newFilePath)
                    tmpPath = Path(folder).parent.joinpath(fileNameList[0].split('/')[0])
                    tmpPath = Path(tmpPath).joinpath(fileNameList[0].split('/')[1])
                    Path.rmdir(tmpPath)
                    Path.rmdir(Path(folder).parent.joinpath(fileNameList[0].split('/')[0]))
                rf.close()
            if zipfile.is_zipfile(folder):
                zf = zipfile.ZipFile(folder)
                fileNameList = []
                print('Copying: ' + Path(folder).name)
                for eachFile in zf.infolist():
                    #if zipfile.Path.is_file(eachFile):
                    if not eachFile.is_dir():
                        fileNameList.append(eachFile.filename)
                fileNameList.sort()
                zf.extract(fileNameList[0], path=Path(folder).parent)
                if len(fileNameList[0].split('/')) == 1:
                    oldFilePath = Path(folder).parent.joinpath(fileNameList[0])
                    #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[1])
                    coverFolder = Path(folder).parent.joinpath('cover')
                    if not coverFolder.exists():
                        Path.mkdir(coverFolder)
                    newFilePath = Path(coverFolder).joinpath(Path(folder).stem + '.' + fileNameList[0].split('.')[-1])
                    Path(oldFilePath).replace(newFilePath)
                if len(fileNameList[0].split('/')) == 2:
                    oldFilePath = Path(folder).parent.joinpath(fileNameList[0])
                    #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[1])
                    coverFolder = Path(folder).parent.joinpath('cover')
                    if not coverFolder.exists():
                        Path.mkdir(coverFolder)
                    newFilePath = Path(coverFolder).joinpath(Path(folder).stem + '.' + fileNameList[0].split('/')[-1].split('.')[-1])
                    Path(oldFilePath).replace(newFilePath)
                    Path.rmdir(Path(folder).parent.joinpath(fileNameList[0].split('/')[0]))
                if len(fileNameList[0].split('/')) == 3:
                    oldFilePath = Path(folder).parent.joinpath(fileNameList[0])
                    #newFilePath = Path(folder).joinpath(fileNameList[0].split('/')[2])
                    coverFolder = Path(folder).parent.joinpath('cover')
                    if not coverFolder.exists():
                        Path.mkdir(coverFolder)
                    newFilePath = Path(coverFolder).joinpath(Path(folder).stem + '.' + fileNameList[0].split('/')[-1].split('.')[-1])
                    Path(oldFilePath).replace(newFilePath)
                    tmpPath = Path(folder).parent.joinpath(fileNameList[0].split('/')[0])
                    tmpPath = Path(tmpPath).joinpath(fileNameList[0].split('/')[1])
                    Path.rmdir(tmpPath)
                    Path.rmdir(Path(folder).parent.joinpath(fileNameList[0].split('/')[0]))
                zf.close()

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass
