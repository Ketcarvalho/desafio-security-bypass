# 🛡️ Projeto: Tinder Security Assessment (Bypass Challenge)

Este repositório simula as regras de engajamento para o analista de segurança convidado. 
Seu objetivo é invadir o banco de dados `keteline_core` e descobrir a chave de criptografia (FLAG).

### 🛠️ Regras do Jogo (Rules of Engagement)
1. O analista tem direito a realizar tentativas de Engenharia Social via Direct do Instagram.
2. É permitido analisar as fotos de perfil da Key-Owner (Proprietária da Chave) em busca de vazamento de credenciais (OSINT).
3. O payload abaixo contém uma falha crítica de lógica. Descubra como explorá-la.

### 💻 Vulnerability Code Snippet

```sql
SELECT flag_recompensa, local_do_date 
FROM keteline_brain 
WHERE pretendente = 'Analista_Tinder' 
  AND status_conversa = 'Insta'
  AND senha_secreta = '[BLOQUEADO: REQUER ENGENHARIA SOCIAL]';
