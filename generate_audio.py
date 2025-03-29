from gtts import gTTS

# Texto em português do Brasil
texto = "Avatares Avançados com IA. Integração Sem Interrupções. Soluções Personalizáveis. Revolucione a Interação Pública: Utilize avatares virtuais de última geração para transformar a forma como os cidadãos se conectam com os serviços do governo.Transparência e Confiança Aumentadas: Ofereça informações claras, consistentes e confiáveis diretamente de fontes aprovadas pelo governo. Uma Abordagem Moderna ao Serviço Público: Adote inovações que atendem às expectativas de uma população cada vez mais digital e exigente."

# Criar objeto TTS e salvar como arquivo MP3
tts = gTTS(text=texto, lang='pt-br')
tts.save("voz_avatares_governo.mp3")

print("Arquivo de áudio gerado com sucesso!")
