#!/usr/bin/env python3
"""
Тест работы с Gemini API
"""

import os
from word_processor import WordProcessor
from llm import GeminiClient

def test_gemini():
    """Тестируем работу с Gemini API"""
    
    # Проверяем переменные окружения
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY не найден в переменных окружения")
        print("💡 Установите переменную: set GEMINI_API_KEY=your_key_here")
        return
    
    print("✅ GEMINI_API_KEY найден")
    
    try:
        # Создаем клиент
        llm_client = GeminiClient()
        print("✅ GeminiClient создан успешно")
        
        # Создаем процессор
        processor = WordProcessor()
        print("✅ WordProcessor создан успешно")
        
        # Проверяем наличие файлов
        docs_files = [f for f in os.listdir("docs") if f.endswith(('.docx', '.doc'))]
        if not docs_files:
            print("❌ Нет файлов в папке docs/")
            return
        
        demo_file = docs_files[0]
        print(f"📄 Тестируем с файлом: {demo_file}")
        
        # Простой промт для теста
        prompt = "Измени все упоминания слова 'философия' на 'философствование' в тексте документа."
        
        # Обрабатываем документ
        result = processor.process_document(demo_file, prompt, llm_client)
        
        if result:
            print(f"✅ Документ обработан успешно: {result}")
        else:
            print("❌ Ошибка при обработке документа")
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_gemini()
