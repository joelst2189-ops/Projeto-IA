' Criar Atalho no Desktop para Cultura LAB.ia
' Execute este script uma vez dentro da pasta do projeto

Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Obter o diretório onde este script está
Dim strScriptDir
strScriptDir = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Caminhos
strDesktop = objShell.SpecialFolders("Desktop")
strSourcePath = strScriptDir & "\ABRIR_CULTURA_LAB.bat"
strLinkPath = strDesktop & "\Cultura LAB.ia.lnk"

' Verificar se a origem existe
If Not objFSO.FileExists(strSourcePath) Then
    MsgBox "Erro: Arquivo ABRIR_CULTURA_LAB.bat não encontrado!" & vbCrLf & "Caminho esperado: " & strSourcePath, 16, "Erro"
    WScript.Quit 1
End If

' Criar atalho
On Error Resume Next
Set objLink = objShell.CreateShortCut(strLinkPath)
objLink.TargetPath = strSourcePath
objLink.WorkingDirectory = strScriptDir
objLink.Description = "Cultura LAB.ia - Sistema de Gestão de Editais"
objLink.IconLocation = "C:\Windows\System32\cmd.exe,1"
objLink.Save

If Err.Number = 0 Then
    MsgBox "✓ Atalho criado com sucesso!" & vbCrLf & vbCrLf & "Localização: " & strLinkPath, 64, "Cultura LAB.ia"
Else
    MsgBox "Erro ao criar atalho: " & Err.Description, 16, "Erro"
End If
