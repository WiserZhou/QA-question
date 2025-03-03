# 🌍✨ **Intelligent Travel Assistant** ✨🌍

Welcome to the **Intelligent Travel Assistant**—your interactive guide to exploring **Ji'an City** in **Jiangxi Province, China**! 🏯🌿

Our system is built with cutting-edge AI technology, integrating **Large Language Models (LLMs)** 🤖, **Retrieval-Augmented Generation (RAG)** 📚, and **LangChain** 🔗 to ensure you receive **accurate, insightful, and contextually relevant** travel and cultural information. 🎒📍

![nothing](./pictures/UI.png)

------

## 🎥 **Demo Video**

You can find the demo video in the project directory:

📂 `./pictures/demo_video.mp4` 🎬🎶

------

## 🛠️ **Environment Setup**

To set up your environment smoothly, follow these steps: 🚀

```powershell
pip install -r requirements.txt
conda install -q ffmpeg  # Ensure ffmpeg==4.2.2
```

Since LLM models require **large memory**, they **cannot** be uploaded to GitHub. ❌💾 Please prepare your own models (both **LLM** and **GAN**) before running the application.

In our project, we primarily use:
 ✅ **Baichuan2** 🧠 for generating responses
 ✅ **Wav2Lip** 🗣️🎥 for producing digital human videos

------

## 🚀 **Running the Application**

We use **Vue 3** 🖥️ to build an intuitive UI, and **FastAPI** ⚡ to power the backend for digital human videos.

To start the application, simply run:

```powershell
python main.py
```

✨ **And you're good to go!** 🎉

------

## 📊 **Our Dataset**

We have collected a **rich dataset** about Ji'an City's **travel and cultural highlights** 🏕️🛶, sourced from various platforms. You can explore the details in the **`our_data`** directory.

To upload new data, use our convenient Python script: 🐍📤

```powershell
python ./upload_data_to_upload.py
```

📌 **Note:** If you face any issues, check the latest guidelines in the [Pinecone documentation](https://docs.pinecone.io/guides/data/upsert-data). 📖🔗

------

## 🖥️ **Our Web UI**

We built our **interactive web UI** with **Vue 3** 🏗️ to ensure a smooth and dynamic user experience.

To set up and run the frontend, install the necessary dependencies (**Node.js** required) and run:

```powershell
npm install
npm run dev
```

🎨 **Enjoy the seamless UI experience!** 🎭✨

🌐 **You can also explore the UI directly at** https://ff-ovo.fun/ 🚀🔗

------

## 📚 **References**

📖 **[Digital Human Intelligent Dialogue System - Linly-Talker: "Interactive Dialogue with Your Virtual Self"](https://github.com/Kedreamix/Linly-Talker)**

------

## 💖 **Acknowledgments**

🚀 **Co-creator:** [yxf203](https://github.com/yxf203)

🌟 Thank you for checking out our project! **We hope this project can be a valuable tool in your AI and tech journey!**  ✈️🏯✨
