# Poe-Bot

Poe-Bot is a chatbot developed using the python gradio framework that leverages the poe-api.

![Screenshot](https://github.com/smallnew666/Poe-Bot/assets/24582880/67d18969-29a4-4ba9-9e26-11e42ee2a2ca)

## Project Description

This repository contains the code for Poe-Bot, a chatbot created by reverse engineering the poe-api. The bot is built using Python and the Gradio library for the user interface.

## Main Features

* Chat interface: The bot communicates with the user through a simple and intuitive chat interface.
* Multiple models: The user can choose between different personalities for the bot using radio buttons.
* Clear history: The user has the option to clear the chat history at any time.

## Installation

Clone the repository:

<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span></div><code class="hljs code-block-body ">git clone https://github.com/smallnew666/Poe-Bot.git
</code></pre>

Navigate to the project directory:

<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span></div><code class="hljs code-block-body ">cd Poe-Bot
</code></pre>

Install the required dependencies:

<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span></div><code class="hljs code-block-body ">pip install -r requirements.txt
</code></pre>

Set the token:

On any desktop web browser, log in to [poe.com](http://poe.com/), then open the browser's developer tools (also called "inspect") and look for the value of the p-b cookie in the following menu:

Chromium: Devtools > Application > Cookies > [poe.com](http://poe.com/)

Update the token in [app.py](http://app.py/) to the value you retrieved:

<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span></div><code class="hljs code-block-body ">bot = PoeChatBot(&#39;your token&#39;) #your poe token
</code></pre>

Install project dependencies:

<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span></div><code class="hljs code-block-body ">pip install -r requirements.txt
</code></pre>

Run the application:

<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span></div><code class="hljs code-block-body ">python app.py
</code></pre>

The app will start a local server. You can access the chatbot at 0.0.0.0:8000 in your browser.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.aihublet.com/LICENSE) file for details.

## Contact

If you have any questions, feel free to contact the repository owner or file an issue.
