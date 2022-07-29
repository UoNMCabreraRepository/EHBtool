# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/evxmc3/exe/ehbGUI_annpso.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/evxmc3/exe/Bolt.gif', '.'), ('C:/Users/evxmc3/exe/Column displacement_val_annpso.txt', '.'), ('C:/Users/evxmc3/exe/Column.gif', '.'), ('C:/Users/evxmc3/exe/Combined.gif', '.'), ('C:/Users/evxmc3/exe/finalised_ANNpso_Coldisp_model.pkl', '.'), ('C:/Users/evxmc3/exe/finalised_ANNpso_Stiffness_model.pkl', '.'), ('finalised_ANNpso_Strength_model.pkl', '.'), ('C:/Users/evxmc3/exe/Stiffness_val_annpso.txt', '.'), ('C:/Users/evxmc3/exe/Strength_val_annpso.txt', '.'), ('C:/Users/evxmc3/exe/valColumn displacement.eps', '.'), ('C:/Users/evxmc3/exe/valStiffness.eps', '.'), ('C:/Users/evxmc3/exe/valStrength.eps', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ehbGUI_annpso',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ehbGUI_annpso',
)
