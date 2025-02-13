from google import genai

client = genai.Client(api_key=<hidden_api_key>)  # Just a placeholder text, but the API could be hidden as a conf file or a system variable

def get_car_ai_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo que possam interessar a um possível comprador.
    '''
    prompt = prompt.format(brand, model, year)
    # gemini.api_key = [key]
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt
    )
    return response.text