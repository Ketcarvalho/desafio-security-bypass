# 🛡️ Projeto: Tinder Security Assessment (Bypass Challenge)

Este repositório simula um ambiente de testes para o analista de segurança convidado. 
Seu objetivo é decifrar a `senha_secreta` para obter a FLAG de acesso.

### 🛠️ Regras do Jogo (Rules of Engagement)
1. Para rodar um scan e liberar pistas de Engenharia Social, o analista deve abrir uma **New Issue** neste repositório com o título `/scan --target keteline`.
2. A proprietária do sistema (Key-Owner) responderá dentro da Issue liberando o acesso às perguntas.
3. Se o analista descobrir a senha nas fotos de perfil, ele deve enviar o palpite final na mesma Issue.

### 💻 Vulnerability Code Snippet

```sql
SELECT flag_recompensa, whatsapp 
FROM keteline_brain 
WHERE pretendente = 'Analista_Tinder' 
  AND senha_secreta = '[BLOQUEADO: REQUER SCAN VIA ISSUES]';
