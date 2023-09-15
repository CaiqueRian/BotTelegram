import requests
import json
import os
import telebot


class TelegramBot:

  def __init__(self):
    token = "6462186773:AAEEJAq148JPVITlzfGdsWh2YHN_emFf08w"
    self.bot = telebot.TeleBot(token)
    self.url_base = f"https://api.telegram.org/bot{token}/"

  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      mensagens = atualizacao["result"]
      if mensagens:
        for mensagem in mensagens:
          update_id = mensagem["update_id"]
          chat_id = mensagem["message"]["chat"]["id"]
          texto = mensagem["message"]["text"]
          resposta = self.criar_resposta(texto)
          self.responder(resposta, chat_id)

  def obter_mensagens(self, update_id):
    link_requisicao = f"{self.url_base}getUpdates?timeout=100"
    if update_id:
      link_requisicao = f"{link_requisicao}&offset={update_id + 1}"
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)

  def criar_resposta(self, mensagem):
    if mensagem == "/Oi":
      return f"""Olá funcionarios da Rede Forte Fibra, essa é a agenda do dia! 
1 - Leandro
2 - Carla
3 - Fabio
4 - Marcio
5 - Daniele
6 - Laura"""














#PARTE QUE GILBERTO TEM QUE ALTERAR
    if mensagem == "1":
      return f""" ficar no chat {os.linesep} Alguma duvida ? (s/n)"""
    elif mensagem == "2":
      return f""" ficar no chat e fazer prospecção de clientes{os.linesep} Alguma duvida ? (s/n)"""
    elif mensagem == "3":
      return f""" Ficar no chat e criar ChatBot {os.linesep} Alguma duvida ? (s/n)"""
    elif mensagem == "4":
      return f""" Cuidar do trabalho externo em cabula {os.linesep} Alguma duvida ? (s/n)"""
    elif mensagem == "5":
      return f""" Cuidar do trabalho externo em barra {os.linesep} Alguma duvida ? (s/n)"""
    elif mensagem == "6":
      return f""" auxiliar o técnico fabio a cuidar do trabalho externo no cabula{os.linesep} Alguma duvida ? (s/n)"""

    if mensagem.lower() in ("s", "sim"):
      return "Confirme com pedro pelo telegram: ... ou Whatsapp: ..."
    elif mensagem.lower() in ("n", "nao"):
      return "Tudo certo então, um bom dia e um ótimo trabalho"
    else:
      return "Tente novamente utilizando /Oi para iniciar a conversa com o Bot ou voce pode pressionar em mim /Oi"

  def responder(self, resposta, chat_id):
    self.bot.send_message(chat_id, resposta)


bot = TelegramBot()
bot.Iniciar()
