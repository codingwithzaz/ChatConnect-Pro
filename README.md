## 🚀💬 ChatConnect-Pro Documentation
![GitHub Views](https://komarev.com/ghpvc/?username=ChatConnect-Pro&style=plastic)


💲Donation: Bitcoin (Binance🪙)
```py
195XfKjaHkBedXptLk2iRAL3Qip2YHqzHZ
```

### 🌟 Introduction

ChatConnect-Pro is an advanced integration project that seamlessly connects the WhatsApp platform with the OpenAI Chatbot, facilitating efficient communication and information exchange between the two platforms. Leveraging sophisticated automation tools and cutting-edge conversational AI capabilities, ChatConnect-Pro streamlines the interaction process without the need for OpenAI API keys, relying solely on the presence of a signed-in ChatGPT window.

### 📝 Requirements

Before deploying the ChatConnect-Pro project, ensure the following prerequisites are in place:

- **Python 3.x:** Ensure that the latest version of Python 3.x is installed on the system.
- **Flask:** Install the Flask web framework to facilitate server-side scripting and routing.
- **Playwright:** Set up the Playwright library for seamless automation and interaction with web pages.
- **Requests:** Install the Requests library to facilitate HTTP requests and streamline communication between the server and other components.
- **Golang:** Set up Golang to enable the deployment of middleware for WhatsApp integration.
- **Whatsmeow:** Install the Whatsmeow library, which acts as a bridge for communication with the WhatsApp platform.
- **SQLite:** Configure the SQLite database connector to support data storage and management within the project.

## :cloud: Pre-Installation
:accessibility: Required Softwares
<div align="center">
  <table>
    <tr>
      <th>Language</th>
      <th>Description</th>
      <th>Version</th>
      <th>Download Link</th>
    </tr>
    <tr>
      <td>Git</td>
      <td>Version control system</td>
      <td>2.42.1</td>
      <td><a href="https://www.git-scm.com/downloads">Download</a></td>
    </tr>
    <tr>
      <td>Python</td>
      <td>Programming language</td>
      <td>3.11.2</td>
      <td><a href="https://www.python.org/downloads">Download</a></td>
    </tr>
    <tr>
      <td>Go</td>
      <td>Programming language</td>
      <td>1.21.3</td>
      <td><a href="https://golang.org/dl/">Download</a></td>
    </tr>
    <tr>
      <td>Tdm-gcc</td>
      <td>MinGW-w64 based GCC for Windows</td>
      <td>10.3.0.2</td>
      <td><a href="https://jmeubank.github.io/tdm-gcc/download/">Download</a></td>
    </tr>
  </table>
</div>
    
> While Python Installation:  
> Add python to path, Use Admin Privileges > Disable Path Limit at the end  
> Make sure to Restart your PC after installation of above softwares

## :cloud: Installation

Fireup your terminal/cmd📟
```sh
# Using Git
git clone https://github.com/codingwithzaz/ChatConnect-Pro
```

```sh
cd ChatConnect-Pro
```

```sh
pip install -r requirements.txt
```

```sh
playwright install firefox # Regards server.py
```
if you want any other browser instead of firefox, such as webkit/chrome then you have to change the browser in server.py file also

```sh
python server.py
```
Login for the first time

> At the same time, you have to run the ```whatsapp``` client also, that is ```main.go``` file.
For this Fireup another terminal/cmd and goto the same folder "ChatConnect-Pro" and run the following command
```
go run main.go
```
> It will automatically install the required go packages

if you get the following error:
> panic: failed to upgrade database: Binary was compiled with 'CGO_ENABLED=0', go-sqlite3 requires cgo to work. This is a stub
> goroutine 1 [running]:
> main.main()
>        C:/Users/vmwar/ChatConnect-Pro/main.go:74 +0x46e
> exit status 2

Run the following command in the same terminal/cmd
```
set CGO_ENABLED=1
```

> If you get the 'gcc' error, make sure you have installed the correct version of TDM-GCC

```go
go run main.go
```
> First time it will take 5-10 to run completely!

### 🌐 Browser Configuration

To configure the browser settings for the ChatConnect-Pro project, follow these instructions:

- To switch the browser from Firefox to Chrome, locate the following line of code in the `server.py` script:

```python
BROWSER = PLAY.firefox.launch_persistent_context(user_data_dir=PROFILE_DIR, headless=True)
```

- Replace `firefox` with `chrome` to switch the browser to Chrome.

- Additionally, you can change the headless mode by modifying the `headless=True` parameter. Setting it to `True` enables headless mode, which runs the browser without a user interface, making it ideal for automated tasks. Setting it to `False` activates the browser's graphical interface, allowing real-time visualization during script execution.

### 💻 Headless Mode

The headless mode enables the browser to operate without a graphical user interface, allowing it to run in the background. This mode is particularly useful for automated tasks and server-side operations where a visible browser window is not required. It significantly reduces resource consumption and enhances the efficiency of the automation process.


### get_last_message function

time.sleep function at specific lines within the get_last_message function:

```python
# Wait for the latest message to appear on the page
while True:
    time.sleep(1)  # Delays the execution for 1 second
```

At this line, time.sleep(1) introduces a one-second delay in the loop. This delay allows the function to periodically pause its execution, enabling it to wait for the latest message to appear on the ChatGPT interface. This approach ensures that the function doesn't excessively consume system resources by continuously checking for updates and that it waits for a reasonable time before proceeding to retrieve the most recent message.

```python
time.sleep(0.2)  # Checks whether the message is being generated & adds Small delay to reduce CPU usage
# Increase the delay if ChatGPT is creating slow response in the browser, preferrably change it to '3'.
```

In this line, time.sleep(0.2) introduces a smaller delay of 0.2 seconds. This short pause is implemented to reduce CPU usage during the iterative process of checking and updating the latest message. By incorporating this small delay, the function optimizes its performance by reducing unnecessary computational load while ensuring that it captures the most recent non-empty message accurately.

The strategic use of time.sleep at these specific lines demonstrates the function's efficient and optimized approach to wait for and retrieve the latest non-empty message from the ChatGPT interface, enhancing the overall performance and resource management of the ChatConnect-Pro project.


### ⚙️ Usage

To effectively utilize the ChatConnect-Pro integration project, follow these steps:

1. **Environment Setup:**
   Ensure that the system environment is configured with the required dependencies and libraries specified in the project's documentation.

2. **Server Deployment:**
   - Launch the `server.py` script to initiate the connection with the OpenAI Chat platform. Modify the port and profile directory parameters as needed to suit your configuration.

3. **Middleware Activation:**
   - Run the `main.go` script to activate the middleware, facilitating the integration with the WhatsApp platform. Configure the appropriate database connector imports to establish seamless communication.

4. **Enhanced Functionality (Optional):**
   - For advanced functionality and multi-instance communication capabilities, deploy the `multichat.py` script. This script enables multiple instances of the OpenAI Chatbot to communicate with each other seamlessly, enhancing the overall system's conversational capabilities.

5. **Monitoring and Interaction:**
   - Monitor the ongoing communication and interaction between the WhatsApp platform and the OpenAI Chatbot through the integrated communication channel. Leverage the powerful capabilities of ChatConnect-Pro to streamline communication processes and enhance the overall user experience for both WhatsApp users and the OpenAI Chatbot.

### Server.py Introduction
The `server.py` file is a Python script that facilitates communication between the OpenAI Chatbot and the WhatsApp platform. It establishes a connection between these two platforms, allowing seamless integration for the exchange of messages. The script utilizes the Flask web framework for creating the server, and the Playwright library for web automation tasks.

### Dependencies
- Python 3.x
- Flask
- Playwright

### Code Structure

1. **Imports**:
    - `time`, `asyncio`, `os`, `flask`, `sys`: Python libraries for various functionalities.
    - `sync_playwright`: Provides synchronous API for Playwright.
2. **Constants**:
    - `PROFILE_DIR`: A string variable that stores the directory for the Playwright user data.
    - `PORT`: An integer variable that represents the port number for the Flask server.
3. **Initialization**:
    - The Flask application is initialized.
    - A new Playwright instance is launched with a Firefox browser in a persistent context.
    - A new page is created within the browser.
4. **Helper Functions**:
    - `get_input_box`: Finds the input box on the web page for sending messages.
    - `is_logged_in`: Checks if the user is logged in to the OpenAI Chat.
    - `send_message`: Sends a message to the OpenAI Chat.
    - `get_last_message`: Retrieves the latest message from the OpenAI Chat.
5. **Routes**:
    - The `/chat` route is defined for handling incoming messages from WhatsApp and sending them to the OpenAI Chat.
6. **Main Function**:
    - The `start_browser` function is called to initiate the browser and the Flask server.
    - If the user is not logged in, a message is displayed, and the script waits for the user to log in.
    - If the user is logged in, a success message is printed.

### Usage
Run the `server.py` script to initiate the server. Ensure that the required dependencies are installed before executing the script. The server listens on the specified port for incoming messages from WhatsApp, which are then sent to the OpenAI Chat for processing. The script handles the communication seamlessly between these two platforms.

## Main.go Documentation

### Introduction
The `main.go` file is a Golang script that serves as a middleware between the WhatsApp platform and the OpenAI Chatbot. It connects to the WhatsApp platform, listens for incoming messages, and forwards them to the OpenAI Chatbot for processing. Upon receiving the response from the OpenAI Chatbot, it sends the reply back to the WhatsApp platform. The script uses the Whatsmeow library for WhatsApp connectivity.

### Dependencies
- Go
- Whatsmeow

### Code Structure

1. **Imports**:
    - `bytes`, `context`, `fmt`, `http`, `net/url`, `os`, `os/signal`, `syscall`: Standard Go libraries for various functionalities.
    - Various imports related to Whatsmeow for WhatsApp functionalities.
2. **Struct Definition**:
    - `MyClient`: A struct that contains the Whatsmeow client and its event handler.
3. **Functions**:
    - `register`: Registers the event handler for the Whatsmeow client.
    - `eventHandler`: Handles the incoming WhatsApp messages, forwards them to the OpenAI Chatbot, and sends the response back to WhatsApp.
4. **Main Function**:
    - Initializes the SQLite database and Whatsmeow client.
    - If the client is not already logged in, it retrieves the QR code for authentication and waits for the user to scan the code.
    - If the client is already logged in, it connects to the WhatsApp platform.
    - Listens for interrupt signals and disconnects the client upon receiving the signal.

### Usage
Compile and run the `main.go` script to establish the connection between the WhatsApp platform and the OpenAI Chatbot. Make sure to install the required dependencies before running the script. The script listens for incoming messages from WhatsApp, forwards them to the OpenAI Chatbot, and sends the response back to WhatsApp.

## Multichat.py Documentation

### Introduction
The `multichat.py` script is designed to create a conversation between two instances of the `server.py` script, effectively allowing the OpenAI Chatbot to communicate with itself. By sending requests to two different instances of the server running on different ports, it simulates a conversation between two entities, each representing one side of the conversation.

### Dependencies
- Python 3.x
- Requests

### Code Structure

1. **Imports**:
    - `requests`: Python library for making HTTP requests.

2. **Constants**:
    - `metaprompt`: A string representing a specific message prompt.

3. **Functionality**:
    - The script initiates two instances of the `server.py` script on different ports, 5001 and 5002, respectively.
    - The script sends a request to the first instance, initiating the conversation by providing an initial message.
    - It then continuously exchanges messages between the two instances, allowing the OpenAI Chatbot to communicate with itself.
    - The `metaprompt` is used to identify and replace specific prompts during the conversation, ensuring the messages remain coherent and meaningful.

### Usage
Ensure that the `server.py` script is already running on ports 5001 and 5002 before executing the `multichat.py` script. The script simulates a conversation between two instances of the OpenAI Chatbot, with each instance communicating with the other in an alternating manner. The `metaprompt` helps in maintaining the coherence and flow of the conversation.

