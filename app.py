import gradio as gr
from api import PoeChatBot
import json

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt_txt = "your question"
bot = PoeChatBot('z7AFmwEXmfd6lKzPBpHBNQ%3D%3D')#your poe token
bot_names = bot.get_bot_names()
bot_names = json.loads(bot_names)
reverse_bot_names = {v: k for k, v in bot_names.items()}
def openai_create(input, bot_choice):
    for msg in bot.chat(reverse_bot_names[bot_choice], input):
        pass
    return msg["text"]

def chatgpt_chat(input, history,radio,input_text):
    history = history or []
    output = openai_create(input, radio)
    history.append((input, output))
    return history, history, ""

def clear(input,output):
    history = []
    input = ''
    output = ''
    return "","",""

block = gr.Blocks()

with gr.Blocks() as block:
    gr.Markdown("""<h1><center>Poe-Bot</center></h1>""")
    
    with gr.Tab("聊天"):
        chatbot = gr.Chatbot()
        text_input  = gr.Textbox(placeholder=prompt_txt)
        radio = gr.Radio(list(reverse_bot_names.keys()), value=list(reverse_bot_names.keys())[0], label="choose bot")
        state = gr.State()
        with gr.Row():
            text_button = gr.Button("发送")
            clear_button = gr.Button("清空")
    text_button.click(chatgpt_chat, inputs=[text_input, state, radio], outputs=[chatbot, state, text_input])
    clear_button.click(clear, inputs=[text_input,state], outputs=[chatbot,state,text_input])

block.launch(debug=True, server_name="0.0.0.0", server_port=8000, share=True)
