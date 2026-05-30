import sys

def rodar_scan():
    print("\n" + "="*50)
    print("🛡️  SISTEMA DE SEGURANÇA KETELINE_CORE - SCAN DE VULNERABILIDADE")
    print("="*50 + "\n")
    
    print("[*] Iniciando varredura no alvo: keteline...")
    print("[+] Conexão estabelecida via Tinder/Instagram bypass.")
    print("[!] Alerta: Uma vulnerabilidade visual foi detectada nas fotos de perfil.\n")

    # Verifica se ele preencheu o campo de texto no GitHub
    if len(sys.argv) < 2 or sys.argv[1].strip() == "":
        print("🔴 [ERRO] Nenhuma senha foi enviada no input do Scan.")
        print("Dica: Você precisa digitar seu palpite no campo de texto antes de rodar o workflow!")
        sys.exit(1)
        
    senha_tentada = sys.argv[1].strip().lower()
    print(f"[*] Analisando payload enviado: '{senha_tentada}'...\n")

    # Validação da senha
    if senha_tentada == "pikachu":
        print("🎉" * 15)
        print("💥 CRITICAL BYPASS! SISTEMA TOTALMENTE INVASIDO!")
        print("🎉" * 15 + "\n")
        print("[+] Flag encontrada: SUCCESS_PART_2_INSTAGRAM")
        print("[+] Recompensa: Você desbloqueou o próximo nível.")
        print("👉 Volte ao Direct do Instagram e mande o código 'PIKACHU INVASOR' para receber seu prêmio (WhatsApp/Date).")
    else:
        print("🔴 [ALERTA DE INTRUSO] Senha incorreta. Payload bloqueado pelo Firewall.")
        print("Dica: Olhe atentamente para as fotos de perfil da dona do repositório (foco nos detalhes das pernas).")
        sys.exit(1)

if __name__ == "__main__":
    rodar_scan()
