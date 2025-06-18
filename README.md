# SmolAgent for Multimodal Reasoning and Evaluation

An autonomous agent powered by [`smolagents`](https://github.com/smol-ai/smolagents), designed to solve and submit answers to the GAIA Benchmark. This project evaluates agent reasoning, tool usage, and general intelligence through a structured challenge set.

## 🌟 Overview

This repository defines and runs a `CodeAgent` with selected tools that can:

- Analyze YouTube videos
- Search the web
- Reverse strings
- Handle various file formats
- Utilize packages like `cv2`, `numpy`, `pandas`, and more

It runs the agent on a list of benchmark questions from the GAIA backend and submits the answers automatically.

## 📦 Features

- ⚙️ **Modular Agent Setup** using `smolagents`
- 🔍 Tooling support: video analysis, web search, data processing
- 📤 Automated evaluation against the GAIA benchmark
- 🧠 Easy customization and extensibility
- 🔐 Hugging Face OAuth login integration