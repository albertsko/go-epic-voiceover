import torch
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

device = "mps" if torch.backends.mps.is_available() else "cpu"
map_location = torch.device(device)

torch_load_original = torch.load


def patched_torch_load(*args, **kwargs):
    if "map_location" not in kwargs:
        kwargs["map_location"] = map_location
    return torch_load_original(*args, **kwargs)


torch.load = patched_torch_load

model = ChatterboxTTS.from_pretrained(device=device)
text = "Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo to take down the enemy's Nexus in an epic late-game pentakill."

# high exaggeration for intensity
# low cfg_weight for deliberate, dramatic pacing
wav = model.generate(text, exaggeration=2.0, cfg_weight=0.3)

ta.save("./output/test-lol-epic.wav", wav, model.sr)
