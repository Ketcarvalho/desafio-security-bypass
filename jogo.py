import os
import sys

def rodar_scan():
    print("\n" + "="*50)
    print("🛡️  SISTEMA DE SEGURANÇA KETELINE_CORE - SCAN DE VULNERABILIDADE")
    print("="*50 + "\n")
    
    print("[*] Iniciando varredura no alvo: keteline...")
    print("[+] Conexão estabelecida via Tinder/Instagram bypass.")
    print("[!] Alerta: Uma vulnerabilidade visual foi detectada nas fotos de perfil.")
    print("[?] Engenharia Social ativa. Responda aos inputs do sistema.\n")

    # Primeira pergunta de Engenharia Social
    pergunta_1 = input("Módulo 01: Qual é o foco principal da rotina diária da Key-Owner (Ex: trabalho, academia, estudos)?\n> ").strip().lower()
    
    if "academia" in pergunta_1 or "malhar" in pergunta_1 or "treino" in pergunta_1:
        print("\n🟢 [ACESS GRANTED] Resposta correta! Você identificou o ambiente da vulnerabilidade.")
        print("Dica: Olhe atentamente para as pernas dela nas fotos desse ambiente...\n")
    else:
        print("\n🔴 [ACCESS DENIED] Resposta incorreta. O sistema de IA bloqueou sua tentativa.")
        sys.exit(1)

    # Input da Senha Final
    senha = input("Módulo 02: Digite o código da senha secreta (A vulnerabilidade física):\n> ").strip().lower()

    if senha == "pikachu":
        print("\n" + "🎉"*15)
        print("💥 CRITICAL BYPASS! SISTEMA TOTALMENTE INVASIDO!")
        print("🎉"*15 + "\n")
        print("[+] Flag encontrada: SUCCESS_PART_2_INSTAGRAM")
        print("[+] Recompensa: Você desbloqueou o próximo nível. Volte ao Direct do Instagram e mande o código 'PIKACHU INVASOR' para receber seu prêmio (WhatsApp/Date).")
    else:
        print("\n🔴 [ALERTA DE INTRUSO] Senha incorreta. Payload bloqueado pelo Firewall.")
        sys.exit(1)

if __name__ == "__main__":
    rodar_scan()
