import openai
import matplotlib.pyplot as plt

openai.api_key = 'tu_api_key_aqui'  # reemplazar la api aca(con seguridad)

prompts = {
    "estrés": [
        "¿Qué situaciones de tu día te han generado más estrés?",
        "Si pudieras cambiar algo en tu rutina diaria para reducir el estrés, ¿qué cambiarías?"
    ],
    "mindfulness": [
        "Dedica 3 minutos a respirar lentamente. Inhala profundamente durante 4 segundos...",
        "Haz un escaneo corporal mental, comenzando desde tus pies hasta tu cabeza."
    ]
}

def generar_respuesta(prompt, temperatura=0.7):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=temperatura
    )
    return response.choices[0].text.strip()

# respuestas
respuestas = []
for tema, lista_prompts in prompts.items():
    for prompt in lista_prompts:
        respuesta = generar_respuesta(prompt)
        respuestas.append(respuesta)
        print(f"Prompt: {prompt}\nRespuesta: {respuesta}\n{'-'*40}")

# Análisis 
eficacia = [0.8, 0.85, 0.9]  # Este sería un ejemplo de datos
etiquetas = ['Bajo', 'Medio', 'Alto']

plt.bar(etiquetas, eficacia, color=['red', 'orange', 'green'])
plt.title('Eficacia de Prompts')
plt.ylabel('Proporción de Éxito')
plt.show()