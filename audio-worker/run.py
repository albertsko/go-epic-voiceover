import os
import re
import torch
import torchaudio
from einops import rearrange
from stable_audio_tools import get_pretrained_model
from stable_audio_tools.inference.generation import generate_diffusion_cond
from huggingface_hub import login, hf_hub_download


def main():
    load_dotenv()

    hf_token = os.getenv("HUGGINGFACE_READ_TOKEN")
    if not hf_token:
        print("Hugging Face token not found :(")
        exit()

    login(token=hf_token)
    try:
        hf_hub_download(
            repo_id="stabilityai/stable-audio-open-1.0",
            filename="model.safetensors",
            token=hf_token,
        )
    except Exception as e:
        print(f"Model download error: {e}")

    # --- Main Logic ---
    if torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    model, model_config = get_pretrained_model("stabilityai/stable-audio-open-1.0")
    sample_rate = model_config["sample_rate"]
    sample_size = model_config["sample_size"]

    model = model.to(device)

    conditioning = [
        {
            "prompt": "reverse bass early hardstyle loop",
            "seconds_start": 0,
            "seconds_total": 30,
        }
    ]

    output = generate_diffusion_cond(
        model,
        steps=100,
        cfg_scale=7,
        conditioning=conditioning,  # pyright: ignore[reportArgumentType]
        sample_size=sample_size,
        sigma_min=0.3,
        sigma_max=500,
        sampler_type="dpmpp-3m-sde",
        device=device,
    )

    output = rearrange(output, "b d n -> d (b n)")

    output = (
        output.to(torch.float32)
        .div(torch.max(torch.abs(output)))
        .clamp(-1, 1)
        .mul(32767)
        .to(torch.int16)
        .cpu()
    )
    torchaudio.save("output.wav", output, sample_rate)
    print("Audio saved to output.wav")


def load_dotenv(filepath=".env"):
    try:
        with open(filepath) as f:
            for line in f:
                stripped = line.strip()

                if len(stripped) >= 3 and not stripped.startswith("#"):
                    key, value = re.split(r"\s*=\s*", stripped, maxsplit=1)
                    os.environ[key] = value.replace("'", "").replace('"', "")
    except FileNotFoundError:
        print(f"Warning: '{filepath}' not found. Skipping.")


if __name__ == "__main__":
    main()
