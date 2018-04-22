# -*- mode: python -*-

block_cipher = None


a = Analysis(['frames.py'],
             pathex=['I:\\py_projects\\frames'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [('foldericon.ico','I:\\py_projects\\frames\\icons\\foldericon.ico','DATA'),('titleicon.ico','I:\\py_projects\\frames\\icons\\titleicon.ico','DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='frames.exe',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='appicon.ico')
