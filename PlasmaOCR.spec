# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('src/ui/*.qml', 'src/ui'), ('assets/icons/*', 'assets/icons')],
    hiddenimports=['PySide6.QtQml', 'PySide6.QtQuick', 'PySide6.QtQuick.Controls', 'PySide6.QtQuick.Layouts', 'PySide6.QtQuick.Window'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PlasmaOCR',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# macOS .app Bundle
app = BUNDLE(
    exe,
    name='LexiclipOCR.app',
    icon=None, # TODO: Add .icns file here if available (e.g., 'assets/icons/app_icon.icns')
    bundle_identifier='com.lexiclip.ocr',
    info_plist={
        'NSHighResolutionCapable': 'True',
        'LSUIElement': 'True', # Makes it a "tray-only" app (hides from Dock) - User preference?
        # User PRD mentioned "tray-only nature requires LSUIElement=1"
    },
)
