# 🛡️ Tinder Security Assessment (Bypass Challenge)

Bem-vindo ao ambiente de testes para o analista de segurança convidado. Seu objetivo é realizar um bypass no sistema `keteline_core` e descobrir a senha secreta (FLAG) para liberar o acesso ao banco de dados principal.

---

### 🚀 Como Executar o Scan de Segurança (Instruções de Invasão)

Para rodar o script interativo e testar seus palpites de senha, siga os passos abaixo dentro da plataforma:

1. Vá até o menu superior deste repositório e clique na aba **"Actions"** (ao lado de Pull Requests).
2. Na barra lateral esquerda, selecione o fluxo **"Executar Scan de Segurança"**.
3. No lado direito da tela, clique no botão cinza **"Run workflow"**.
4. Um campo de texto será aberto. Digite ali o seu palpite de senha (payload) e clique no botão verde **"Run workflow"** para disparar o exploit.
5. Após o carregamento, clique na execução do teste para abrir o terminal e ler os logs do sistema.

---

### 🛠️ Regras do Jogo & Engenharia Social

* O analista tem direito a realizar tentativas de Engenharia Social via Direct do Instagram para pescar pistas.
* É permitido (e altamente recomendado) analisar as fotos de perfil da Key-Owner em busca de vazamento de credenciais (reconhecimento via OSINT).
* **Dica do Firewall:** A senha secreta é uma vulnerabilidade física real, visível aos olhos de quem repara nos detalhes. Está documentada visualmente em algum lugar das fotos.

### 💻 Vulnerability Code Snippet

```sql
SELECT flag_recompensa, whatsapp 
FROM keteline_brain 
WHERE pretendente = 'Analista_Tinder' 
  AND senha_secreta = '[REQUER INPUT VIA WORKFLOW ACTIONS]';
