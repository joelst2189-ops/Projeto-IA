' Cultura LAB.ia - Launcher
' Este script executa a aplicação

Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Obter o diretório onde este script está
Dim strScriptDir
strScriptDir = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Caminho do arquivo .bat
strScriptPath = strScriptDir & "\ABRIR_CULTURA_LAB.bat"

' Verificar se o arquivo .bat existe
If Not objFSO.FileExists(strScriptPath) Then
    MsgBox "Erro: Arquivo ABRIR_CULTURA_LAB.bat não encontrado!" & vbCrLf & "Caminho: " & strScriptPath, 16, "Cultura LAB.ia - Erro"
    WScript.Quit 1
End If

' Executar o .bat com working directory correto
objShell.CurrentDirectory = strScriptDir
objShell.Run chr(34) & strScriptPath & chr(34), 1, False
