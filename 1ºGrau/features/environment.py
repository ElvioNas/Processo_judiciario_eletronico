# environment.py - Setup e Teardown para Behave

import os
import time
from pathlib import Path
from datetime import datetime

def before_all(context):
    """Executa antes de todos os testes"""
    print("\n" + "="*70)
    print("🧪 INICIANDO TESTES - PJe 1º e 2º Grau")
    print("="*70)
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("="*70 + "\n")
    
    # Configurações globais
    context.timeout = 30
    context.base_url_1g = "https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam"
    context.base_url_2g = "https://homologacao-pje.app.tjpe.jus.br/h06-2g/home.seam"
    
    # Diretório de screenshots
    context.screenshot_dir = Path("screenshots")
    context.screenshot_dir.mkdir(exist_ok=True)

def after_all(context):
    """Executa após todos os testes"""
    print("\n" + "="*70)
    print("✅ TESTES FINALIZADOS")
    print("="*70 + "\n")

def before_scenario(context, scenario):
    """Executa antes de cada cenário"""
    print(f"\n📌 Cenário: {scenario.name}")

def after_scenario(context, scenario):
    """Executa após cada cenário"""
    if hasattr(context, 'driver'):
        # Salvar screenshot em caso de falha
        if scenario.status == 'failed':
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = context.screenshot_dir / f"failure_{scenario.name}_{timestamp}.png"
            context.driver.save_screenshot(str(screenshot_path))
            print(f"📸 Screenshot salvo: {screenshot_path}")
        
        # Fechar o driver
        try:
            context.driver.quit()
            print("✔ Driver fechado com sucesso")
        except Exception as e:
            print(f"⚠ Erro ao fechar driver: {e}")

def before_feature(context, feature):
    """Executa antes de cada feature"""
    print(f"\n" + "="*70)
    print(f"🎯 Feature: {feature.name}")
    print("="*70)

def after_feature(context, feature):
    """Executa após cada feature"""
    pass

def after_step(context, step):
    """Executa após cada step"""
    # Adicione aqui lógica para logs ou capturas de tela após cada step
    pass
