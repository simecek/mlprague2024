import os

import modal
from modal import Image, Secret, App, gpu

MODEL_DIR = "/model"
MODEL_NAME = "simecek/law_summarizer"


def download_model_to_image(model_dir, model_name):
    from huggingface_hub import snapshot_download
    from transformers.utils import move_cache

    os.makedirs(model_dir, exist_ok=True)

    snapshot_download(
        model_name,
        local_dir=model_dir,
        token=os.environ["HF_TOKEN"],
    )
    move_cache()



image = (
    Image.debian_slim()
    .pip_install(
        "torch==2.1.2",
        "transformers==4.40.0",
        "huggingface_hub==0.22.2",
        "hf-transfer==0.1.4",
        "sentencepiece==0.2.0",
    )
    # Use the barebones hf-transfer package for maximum download speeds. Varies from 100MB/s to 1.5 GB/s,
    # so download times can vary from under a minute to tens of minutes.
    # If your download slows down or times out, try interrupting and restarting.
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(
        download_model_to_image,
        secrets=[Secret.from_name("hf")],
        timeout=60 * 20,
        kwargs={"model_dir": MODEL_DIR, "model_name": MODEL_NAME},
    )
)

app = App(
    f"mlprague-{MODEL_NAME.split('/')[-1]}", image=image
)


GPU_CONFIG = gpu.A10G(count=1)

alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Response:
"""


@app.cls(gpu=GPU_CONFIG, secrets=[Secret.from_name("hf")])
class Model:
    @modal.enter()
    def load(self):
        from transformers import GemmaTokenizer, AutoModelForCausalLM

        self.tokenizer = GemmaTokenizer.from_pretrained(MODEL_DIR)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)

    @modal.method()
    def generate(self, prompts):
        ret = []
        for prompt in prompts:
            inputs = self.tokenizer(alpaca_prompt.format(prompt), return_tensors="pt")
            prompt_len = inputs["input_ids"].shape[-1]
            outputs = self.model.generate(**inputs, max_new_tokens=100)
            one_output = self.tokenizer.decode(outputs[0][prompt_len:])
            print(one_output)
            ret.append(one_output)

        return ret


@app.local_entrypoint()
def main():
    model = Model()
    questions = [
            "Ahoj, jak se máš?",
            "V jakém roce byl vynalezen knihtisk?",
    ]
    model.generate.remote(questions)
