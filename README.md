# Fine-tuning Open-Source LLMs to Small Languages

**Link**: bit.ly/praguellm

**Slides**:

* https://docs.google.com/presentation/d/1wyVwD4CwWV9fpiqGyoyeSIk0JpmPeb8HWg40gSMBOM4/edit?usp=sharing
* https://docs.google.com/presentation/d/1f8BQ6Dv1DUXLINoB2Mga4LjnPhL8OrsctCBoE9baHec/edit?usp=sharing

**Exercises:**

* [00_Sentiment_demo](00_Sentiment_demo.ipynb): Just to test Colab and explore the HF Hub.
* [01_Tokenizers](01_Tokenizers.ipynb): Explore how the ratio of the number of characters to the number of tokens varies by language and tokenizer.
* [02_Talk_to_open_models](https://labs.perplexity.ai/): Unlike ChatGPT and other large models, the comprehension of your language by smaller models might be limited.
* [03_Let_us_create_a_benchmark_together!](https://forms.gle/UPRYQ3bEriRdMyw36): Please submit 5 or more questions.hugging
* [04_ChatGPT_API](04_ChatGPT_API.ipynb): Benchmarking ChatGPT3.5 API.
* [05_Gemma7B](05_Gemma7B.ipynb): Benchmarking open models.
* [06_QLoRA_finetuning](06_QLoRA_finetuning.ipynb): Let us fine-tune a model to your dataset!
* [07_Save_Angelina](07_Save_Angelina.ipynb): Manipulating the model.
* [08_Run_your_model_in_the_cloud](deployment.py): You can get a free $30 on [modal.com](https://modal.com/docs/examples/vllm_inference) to deploy your model.

**Benchmarks:**

* [mlprague](https://huggingface.co/datasets/simecek/mlprague): The benchmark we created together during the workshop, 111 A/B/C/D questions (🇨🇿 41, 🇸🇰 27, 🇮🇹 8, 🇫🇷 7, 🇺🇦 6...)
* [synczech50](https://huggingface.co/datasets/simecek/synczech50): Synthetic dataset of 50 A/B/C/D questions for quick evaluation how the LMM understands Czech and Czech specific knowledge.

**Small Czech LLM**:
* [cswikimistral_0.1](https://huggingface.co/simecek/cswikimistral_0.1): Mistral7B model fine-tuned with 4bit-QLoRA on Czech Wikipedia data
