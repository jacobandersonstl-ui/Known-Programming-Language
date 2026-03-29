!define APP_NAME "Known Language"
!define APP_VERSION "0.1.0"
!define INSTALL_DIR "$PROGRAMFILES(x86)\Known Language"

!include "MUI2.nsh"

Name "${APP_NAME}"
OutFile "Known_Language_Installer.exe"
InstallDir "${INSTALL_DIR}"
RequestExecutionLevel admin

; MUI Settings
; MUI Settings
!define MUI_BGCOLOR "FFFFFF"
!define MUI_ICON "C:\Users\jea_s\Known_Language.ico"
!define MUI_ABORTWARNING

; Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

Section "Install"
    SetOutPath "${INSTALL_DIR}"
    File "dist\interpreter.exe"
    Rename "${INSTALL_DIR}\interpreter.exe" "${INSTALL_DIR}\known.exe"

    EnVar::SetHKLM
    EnVar::AddValue "PATH" "${INSTALL_DIR}"

    WriteUninstaller "${INSTALL_DIR}\uninstall.exe"

    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\KnownLanguage" \
        "DisplayName" "${APP_NAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\KnownLanguage" \
        "UninstallString" "${INSTALL_DIR}\uninstall.exe"
SectionEnd

Section "Uninstall"
    Delete "${INSTALL_DIR}\known.exe"
    Delete "${INSTALL_DIR}\uninstall.exe"
    RMDir "${INSTALL_DIR}"

    EnVar::SetHKLM
    EnVar::DeleteValue "PATH" "${INSTALL_DIR}"

    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\KnownLanguage"
SectionEnd